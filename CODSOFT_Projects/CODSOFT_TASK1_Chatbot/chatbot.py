"""
CodSoft AI Internship - Task 1: Rule-Based Chatbot
Uses regex pattern matching to map user input to predefined responses.
"""
import random
import re
from datetime import datetime

# Each rule: (regex pattern, list of possible responses)
RULES = [
    (r"\b(hi|hello|hey|namaste|good (morning|afternoon|evening))\b",
     ["Hello! How can I help you today?", "Hey there! What's on your mind?", "Hi! Nice to see you."]),

    (r"\bmy name is (\w+)",
     ["Nice to meet you, {0}!", "Hello {0}, great to have you here!"]),

    (r"\bwhat('?s| is) your name\b|\bwho are you\b",
     ["I'm MyChatbot, a simple rule-based chatbot.", "People call me MyChatbot. I live in a Python file!"]),

    (r"\bhow are you\b|\bhow('?s| is) it going\b",
     ["I'm doing great, thanks for asking! How about you?", "All systems running smoothly!"]),

    (r"\b(i am|i'm|im) (fine|good|great|okay|ok|well)\b",
     ["Glad to hear that!", "Awesome! Let's keep the good vibes going."]),

    (r"\b(i am|i'm|im) (sad|upset|tired|bored|stressed)\b",
     ["Sorry to hear that. Want to talk about it, or should I tell a joke?", "Hang in there! Maybe a short break would help."]),

    (r"\b(what can you do|help)\b",
     ["I can chat, tell jokes, tell the time and date, and answer a few basic questions. Try 'tell me a joke'!"]),

    (r"\b(time|what time)\b",
     ["__TIME__"]),

    (r"\b(date|today|what day)\b",
     ["__DATE__"]),

    (r"\bjoke\b",
     ["Why do programmers prefer dark mode? Because light attracts bugs!",
      "Why did the Python programmer wear glasses? Because they couldn't C!",
      "There are 10 kinds of people: those who understand binary and those who don't."]),

    (r"\b(what is|define|explain) (ai|artificial intelligence)\b",
     ["AI is the field of building machines that can perform tasks that normally need human intelligence, like learning, reasoning and perception."]),

    (r"\b(what is|define|explain) (ml|machine learning)\b",
     ["Machine learning is a subset of AI where models learn patterns from data instead of being explicitly programmed."]),

    (r"\b(what is|define|explain) python\b",
     ["Python is a popular, easy-to-read programming language widely used in AI, data science and web development."]),

    (r"\b(thank you|thanks|thx)\b",
     ["You're welcome!", "Happy to help!", "Anytime!"]),

    (r"\b(bye|goodbye|exit|quit|see you)\b",
     ["Goodbye! Have a great day!", "See you later!"]),
]

FALLBACKS = [
    "Hmm, I'm not sure I understand. Could you rephrase that?",
    "I don't know that one yet. Try asking for help to see what I can do.",
    "Sorry, I only know a few things. Type 'help' to see them.",
]


def get_response(user_input: str) -> str:
    text = user_input.lower().strip()
    for pattern, responses in RULES:
        match = re.search(pattern, text)
        if match:
            reply = random.choice(responses)
            if reply == "__TIME__":
                return "It's " + datetime.now().strftime("%I:%M %p") + "."
            if reply == "__DATE__":
                return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
            if "{0}" in reply:
                return reply.format(match.group(1).capitalize())
            return reply
    return random.choice(FALLBACKS)


def main():
    print("MyChatbot: Hi! I'm a rule-based chatbot. Type 'bye' to exit.")
    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nMyChatbot: Goodbye!")
            break
        if not user.strip():
            continue
        print("MyChatbot:", get_response(user))
        if re.search(r"\b(bye|goodbye|exit|quit|see you)\b", user.lower()):
            break


if __name__ == "__main__":
    main()
