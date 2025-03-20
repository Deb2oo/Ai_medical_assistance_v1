from dotenv import load_dotenv
load_dotenv()

import os
import base64
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in environment variables.")

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {str(e)}")
        return None


# Multimodal LLM
query = "what is the name of the decease on my face in the image?"
model = "llama-3.2-90b-vision-preview"


def analyze_image_with_query(query, model, encoded_image):
    if encoded_image is None:
        return "Failed to encode image."

    client = Groq(api_key=GROQ_API_KEY)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]

    try:
        chat_completion = client.chat.completions.create(
            model=model,
            messages=messages
        )
        response = chat_completion.choices[0].message.content
        print(f"API Response: {response}")
        return response
    except Exception as e:
        print(f"Error calling API: {str(e)}")
        return f"Error: {str(e)}"


# Step 4: Run the analysis
image_path = "acne.jpg"
encoded_image = encode_image(image_path)

if encoded_image:
    result = analyze_image_with_query(query, model, encoded_image)
    print("Final Output:", result)
