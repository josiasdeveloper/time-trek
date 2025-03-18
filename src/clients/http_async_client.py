import asyncio
import ssl
from typing import Dict, Optional

import aiohttp
import backoff
from aiohttp import ClientResponse


class HttpAsyncClient:
    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        max_retries: int = 3,
        headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.max_retries = max_retries
        self.headers = headers or {}
        self.verify_ssl = verify_ssl
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        await self.create_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close_session()

    async def create_session(self):
        if not self._session:
            if not self.verify_ssl:
                # Create a custom SSL context that doesn't verify certificates
                ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
                connector = aiohttp.TCPConnector(ssl=ssl_context)
                self._session = aiohttp.ClientSession(
                    timeout=self.timeout,
                    headers=self.headers,
                    connector=connector,
                )
            else:
                self._session = aiohttp.ClientSession(
                    timeout=self.timeout, headers=self.headers
                )

    async def close_session(self):
        if self._session:
            await self._session.close()
            self._session = None

    @backoff.on_exception(
        backoff.expo,
        (aiohttp.ClientError, asyncio.TimeoutError),
        max_tries=3,
        giveup=lambda e: isinstance(e, aiohttp.ClientResponseError)
        and e.status >= 400,
    )
    async def request(
        self, method: str, endpoint: str, **kwargs
    ) -> ClientResponse:
        if not self._session:
            await self.create_session()

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = None
        try:
            if not self._session:
                raise RuntimeError("Session not created")
            response = await self._session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except Exception:
            raise

    async def get(self, endpoint: str, **kwargs) -> ClientResponse:
        return await self.request("GET", endpoint, **kwargs)

    async def post(self, endpoint: str, **kwargs) -> ClientResponse:
        return await self.request("POST", endpoint, **kwargs)

    async def put(self, endpoint: str, **kwargs) -> ClientResponse:
        return await self.request("PUT", endpoint, **kwargs)

    async def delete(self, endpoint: str, **kwargs) -> ClientResponse:
        return await self.request("DELETE", endpoint, **kwargs)

    async def patch(self, endpoint: str, **kwargs) -> ClientResponse:
        return await self.request("PATCH", endpoint, **kwargs)


#
