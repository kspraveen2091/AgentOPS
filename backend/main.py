from fastapi import FastAPI

from backend.api.routes.health import router as health_router


app = FastAPI(
    title="AgentOPS",
    description="Personalized AI Agent",
    version="0.1.0",
)


app.include_router(health_router)