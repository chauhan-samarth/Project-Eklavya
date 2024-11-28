from flask import Flask, request, jsonify
from intent_classifier import IntentClassifier
from context_manager import ContextManager
from dynamic_sql_query import execute_dynamic_query
from feedback import record_feedback

app = Flask(__name__)

intent_classifier = IntentClassifier()
context_manager = ContextManager()

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    user_id = 1 
    context_manager.update_context(user_id, user_message, "Bot response here")

    # Process user intent
    intent = intent_classifier.classify_intent(user_message, ["faq", "search", "help"])

    if intent == "faq":
        response = "This is a response from the FAQ database"
    elif intent == "search":
        response = execute_dynamic_query("SELECT * FROM faqs WHERE question LIKE %s", (user_message,))
    else:
        response = "How can I help you?"

    return jsonify({'response': response})

@app.route('/feedback', methods=['POST'])
def feedback():
    user_id = 1
    feedback_text = request.form.get('feedback')
    rating = int(request.form.get('rating'))
    conversation_log_id = 1

    record_feedback(user_id, conversation_log_id, feedback_text, rating)
    return jsonify({'status': 'Feedback recorded'})

if __name__ == '__main__':
    app.run(debug=True)