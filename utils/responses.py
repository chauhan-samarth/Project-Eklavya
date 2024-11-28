def generate_response(intent):
    if intent == "faq":
        return "Here is an answer from the FAQ database."
    elif intent == "search":
        return "Searching for your query..."
    else:
        return "I'm here to help you with anything!"
