from fastapi import FastAPI
from datetime import datetime, timezone
import os

app = FastAPI(
    title="Ford Motor Company - Data Metrics",
    description="A FastAPI application for data metrics and health checks.",
    version="1.0.0",
)

@app.get("/")
def roo():
    return {
        "message": "FastAPI running on Google Cloud Run", "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/info")
def info():
    return {
        "app_name": app.title,
        "description": app.description,
        "version": app.version,
        "environment": os.getenv("ENVIRONMENT", "development"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/echo/{message}")
def echo(message: str):
    return {
        "message": message
    }
