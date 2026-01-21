from fastapi import FastAPI

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
    return {"status": "ok", "service": "IncidentLens"}

# ------------------------------------------------------------------------------
# Router Inclusion
# ------------------------------------------------------------------------------
# TODO: Import and include routers once created
# from app.routers import alerts
# app.include_router(alerts.router, prefix="/webhook", tags=["Alerts"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)