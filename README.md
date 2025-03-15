# Time Trek 🚀

Time Trek is an interactive web application that connects people with historical events from their birth month. By combining historical data with AI-powered insights, users can discover fascinating facts about what was happening in the world when they were born.

## 🌟 Features

- Birth date input interface
- Historical facts fetching for the specified month
- AI-enhanced explanations of historical events using ChatGPT
- Simple and intuitive API endpoint

## 🛠️ Technical Stack

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

- Node.js (Latest LTS version)
- API keys for:
  - Historical Events API
  - OpenAI API

### Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/time-trek.git
cd time-trek
```

2. Install dependencies

```bash
npm install
```

3. Set up environment variables

```bash
# Create a .env file with your API keys
OPENAI_API_KEY=your_openai_api_key
HISTORICAL_API_KEY=your_historical_api_key
```

4. Start the application

```bash
npm run dev
```

## 🔒 Environment Variables

Make sure to set up the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `HISTORICAL_API_KEY`: Your Historical Events API key

## 👥 Contributors

- [Your Name]

## 📝 License

This project is part of the Object-Oriented Programming course at Universidade Federal de Sergipe.

---

Made with 💻 for POO 2025.1
