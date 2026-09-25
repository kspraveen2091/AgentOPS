from fastapi import APIRouter
from pydantic import BaseModel

from backend.agent.graph import agent


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message,
                }
            ]
        }
    )

    response = result["messages"][-1]

    return {
        "response": response.content
    }
