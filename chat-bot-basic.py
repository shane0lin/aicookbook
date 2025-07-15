from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "Hi, can you tell me a joke?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,  # Controls response creativity
    max_tokens=100,   # Limits response length
    presence_penalty=0.6,  # Encourages new topics
    frequency_penalty=0.3  # Reduces repetition
)
# Extract and print the AI's response
ai_response = response.choices[0].message.content

print("Prompt:", prompt)
print("Response:", ai_response)
