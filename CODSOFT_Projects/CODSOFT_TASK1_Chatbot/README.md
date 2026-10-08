# CODSOFT Task 1 - Rule-Based Chatbot

A simple chatbot that uses regular expressions (pattern matching) to detect what
the user is asking and reply with predefined responses.

## Run
```
python chatbot.py
```

## Try
- hello
- my name is Sujit
- tell me a joke
- what time is it
- what is machine learning
- bye

## How it works
`RULES` is a list of (regex, responses) pairs. `get_response()` checks the input
against each pattern in order and returns a random matching reply, or a fallback.
