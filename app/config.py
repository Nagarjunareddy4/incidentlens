import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    PROMETHEUS_URL: str = os.getenv("PROMETHEUS_URL", "http://localhost:9090")
    SLACK_WEBHOOK_URL: str | None = os.getenv("SLACK_WEBHOOK_URL")

    APP_NAME: str = "IncidentLens"

settings = Settings()