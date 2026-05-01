from fastapi import FastAPI

# Initialize the API with our Enterprise name
app = FastAPI(
    title="Meridian Spatial Engine",
    description="Event-driven, geospatial routing system for crisis response.",
    version="1.0.0"
)

# A simple health-check endpoint
@app.get("/health")
async def system_health():
    return {
        "status": "online",
        "engine": "FastAPI",
        "database_connected": False # We will fix this next!
    }