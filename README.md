# Time Trek 🚀

Time Trek is an interactive web application that connects people with historical events from their birth month. By combining historical data with AI-powered insights, users can discover fascinating facts about what was happening in the world when they were born.

## 🌟 Features

- Birth date input interface
- Historical facts fetching for the specified month
- AI-enhanced explanations of historical events using ChatGPT
- Simple and intuitive API endpoint

## 🛠️ Technical Stack

- Backend:
  - Python 3.8+
  - FastAPI
  - Uvicorn
- API Integration:
  - Historical Events API
  - OpenAI's ChatGPT API

## 📡 API Endpoint

The main endpoint will return historical facts and AI-enhanced explanations:

```http
GET /api/historical-facts?date=YYYY-MM-DD
```

Example Response:

```json
{
  "date": "1990-03-15",
  "historicalFacts": [
    {
      "fact": "Historical event description",
      "aiEnhancedExplanation": "Detailed context provided by ChatGPT"
    }
    // ... more facts
  ]
}
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- API keys for:
  - Historical Events API
  - OpenAI API

### Installation

1. Clone the repository

```bash
git clone https://github.com/josiasdev/time-trek
.git
cd time-trek

```

2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

```bash
# Create a .env file with your API keys
OPENAI_API_KEY=your_openai_api_key
HISTORICAL_API_KEY=your_historical_api_key
```

5. Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:9000`

## 📚 Project Structure

## 🔒 Environment Variables

Make sure to set up the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `HISTORICAL_API_KEY`: Your Historical Events API key

## 👥 Contributors

- [Your Name]

## 📝 License

This project is part of the Object-Oriented Programming course at Universidade Federal de Sergipe.

---

