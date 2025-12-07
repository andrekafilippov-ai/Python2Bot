import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-OCR:novita",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in one sentence."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://i.pinimg.com/736x/6d/8e/38/6d8e3897307cc2ce11a4dd8baa52dc2f.jpg"
                    }
                }
            ]
        }
    ],
)

print(completion.choices[0].message)