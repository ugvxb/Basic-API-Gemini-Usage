import google.genai as genai

API_KEY = ""

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works"
)

if hasattr(response, "text"):
    print(response.text)
else:
    print(response.candidates[0].content.parts[0].text)
