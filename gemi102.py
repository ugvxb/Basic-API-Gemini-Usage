import google.genai as genai
API_KEY = ""
client = genai.Client(api_key=API_KEY)

def coding_helper_chatbot():
    system_prompt = (
        "You are an expert Python programmer. "
        "Provide clear, concise, and accurate answers. "
        "When you see a code error, first explain the error, "
        "then provide the corrected code. "
        "Here is the user's question: "
    )
    while True:
        user_query = input("Your: ")
        if user_query.lower() == "quit":
            break
        full_prompt = system_prompt + user_query
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt
            )
            if hasattr(response, "text"):
                print(f"Coding: {response.text}\n")
            else:
                print(f"Coding: {response.candidates[0].content.parts[0].text}\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")
if __name__ == "__main__":
    coding_helper_chatbot()

#VXB
