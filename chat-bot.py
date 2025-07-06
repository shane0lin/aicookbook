from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "Hi, can you tell me a joke?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
# Extract and print the AI's response
ai_response = response.choices[0].message.content

print("Prompt:", prompt)
print("Response:", ai_response)
