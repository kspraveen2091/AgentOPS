import asyncio

from backend.agent.graph import agent


async def main():

    try:

        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": (
                            "What are the latest developments "
                            "in generative AI?"
                        ),
                    }
                ]
            }
        )

        print("\nFinal response:\n")
        print(result["messages"][-1].content)

    except Exception as e:

        print("\n===== ERROR TYPE =====")
        print(type(e))

        print("\n===== ERROR =====")
        print(e)

        print("\n===== ERROR DETAILS =====")

        if hasattr(e, "response"):
            print(e.response)

        if hasattr(e, "body"):
            print(e.body)

        if hasattr(e, "response_data"):
            print(e.response_data)


if __name__ == "__main__":
    asyncio.run(main())
