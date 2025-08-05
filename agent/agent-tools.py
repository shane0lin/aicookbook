import asyncio
from agents import Agent, WebSearchTool, Runner

# Create an agent with the WebSearchTool
agent = Agent(
    name="Research Assistant",
    instructions="You are a research assistant who can search the web to answer questions.",
    model="gpt-4.1",
    # Add the WebSearchTool to the tools list
    tools=[WebSearchTool()]
)


async def main():

    result = await Runner.run(
        starting_agent=agent,
        input="Where are most recent wild fire in washinton?"
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())