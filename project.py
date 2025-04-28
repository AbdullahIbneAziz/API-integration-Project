from google import genai

client = genai.Client(api_key="AIzaSyAddU3zbH5jhb7kY0yR6udDsqkHIqb3Z1g")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="How can I be expert in Machine Learning",
)

print(response.text)