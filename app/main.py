from fastapi import FastAPI
from app.api.alerts import router as alerts_router
from app.config import settings


# Initialize the application
app = FastAPI(
    title="IncidentLens",
    description="AI-Powered Incident Explainer for DevOps",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the service is operational.
    """
    return {"status": "ok"}

app.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])

print("OpenAI key loaded:", bool(settings.OPENAI_API_KEY))
print("Prometheus URL:", settings.PROMETHEUS_URL)
print("Slack webhook URL loaded:", bool(settings.SLACK_WEBHOOK_URL))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)