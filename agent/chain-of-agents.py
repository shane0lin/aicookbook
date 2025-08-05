import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)

# Define a Blog Writer agent
blog_agent = Agent(
    name="Blog Writer",
    instructions=(
        "You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post "
        "that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    recipe_result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    conversation_context = recipe_result.to_input_list() 

    msg_blog_request = "Write a blog post about the recipe."


    result = await Runner.run(
        starting_agent=blog_agent,
        input=conversation_context + [{"role":"user", "content": msg_blog_request}]
    )


    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())