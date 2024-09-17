import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

EDEN_API_KEY = os.getenv("EDEN_API_KEY")


class Bot:
    def __init__(self, global_action: str) -> None:
        # Store the global action (bot personality) as an instance variable
        self._history = []  # Chat history for this bot instance
        self._global_action = global_action 

    def chat(self, prompt):
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "providers": "openai/gpt-4o-mini",
            "text": prompt,
            "chatbot_global_action": self._global_action,
            "previous_history": self._history,
            "temperature": 0.10,
            "max_tokens": 150,
        }

        response = requests.post(url, json=payload, headers=headers)
        answer = json.loads(response.text)["openai/gpt-4o-mini"]["generated_text"]


        self._history.append({"role": "user", "message": prompt})
        self._history.append({"role": "assistant", "message": answer})

        return answer
    

#Define the bots personality
# ChatGBG
GbGlenn_bot_action = """You are a funny guy from Gothenburg,sweden. You really love Gothgenburg and gets mad with an attitude if stockholm is mentioned.
            you love emojis and use them too much"""

# JokeTeller
JokeTeller_bot_action ="""You always tell a funny joke, most of the times they're really bad but you finds it funny"""

GbGlenn_bot = Bot(GbGlenn_bot_action)
JokeTeller_bot = Bot(JokeTeller_bot_action)

# Use Gothenburg bot
print(GbGlenn_bot.chat("Tell me about Gothenburg!"))

# Use Stockholm bot
print(JokeTeller_bot.chat("Tell me a joke!"))

class BotHandler:
    def __init__(self):
        self.bots = {}
        self.active_bot = None

    def add_bot(self, name, bot):
        self.bots[name] = bot

    def switch_bot(self, name):
        if name in self.bots:
            self.active_bot = self.bots[name]
            print(f"Switched to {name}")
        else:
            print(f"No bot named {name} found!")

    def chat(self, message):
        if self.active_bot:
            return self.active_bot.chat(message)
        else:
            return "No bot selected!"


bot_manager = BotHandler()

# Add bots
bot_manager.add_bot("GbGlenn_bot", GbGlenn_bot)
bot_manager.add_bot("JokeTeller_bot", JokeTeller_bot)

# Switch and chat with Gothenburg bot
bot_manager.switch_bot("GbGlenn_bot")
print(bot_manager.chat("What do you think about Stockholm?"))

# Switch and chat with Stockholm bot
bot_manager.switch_bot("JokeTeller_bot")
print(bot_manager.chat("What do you think about Gothenburg?"))
