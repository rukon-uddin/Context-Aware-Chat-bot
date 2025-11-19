from openai import OpenAI
import os

class ChatGPTClient:
    def __init__(self, model="gpt-4.1-mini"):
        self.client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        self.model = model
        self.history = []
        
    

    def add_user_message(self, text):
        """Add a user message to history."""
        self.history.append({"role": "user", "content": text})


    def ask(self, prompt):
        """Send a prompt and return the assistant's reply."""
        # self.add_user_message(prompt)

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=prompt
        )
        reply = completion.choices[0].message.content

        # Save assistant reply in history
        # self.history.append({"role": "assistant", "content": reply})

        return reply

    def reset(self):
        """Clear the conversation."""
        self.history = []
