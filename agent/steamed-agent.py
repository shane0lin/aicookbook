import asyncio
from agents import Agent, Runner

# Create a simple agent with a name, instructions and model
agent = Agent(
    name="Recipe Chef",
    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",
    model="gpt-4.1"
)


async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Give me a quick recipe for a healthy smoothie"
    )
    
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())