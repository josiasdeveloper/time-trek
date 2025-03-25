from fastapi import FastAPI

app = FastAPI()

@app.get("/api/historical-facts")
async def get_historical_facts(date: str):
    events = [
        {"fact": f"Em {date}, algo histórico aconteceu."},
        {"fact": f"Outro evento em {date}."}
    ]
    enhanced_facts = []
    for event in events:
        explanation = f"Explicação por IA: {event['fact']} Isso mudou o mundo!"
        enhanced_facts.append({
            "fact": event["fact"],
            "aiEnhancedExplanation": explanation
        })
    return {"date": date, "historicalFacts": enhanced_facts}