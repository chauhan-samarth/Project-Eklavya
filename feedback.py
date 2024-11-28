from dynamic_sql_query import execute_dynamic_query

def record_feedback(user_id, conversation_log_id, feedback_text, rating):
    query = "INSERT INTO feedback (user_id, conversation_log_id, feedback, rating) VALUES (%s, %s, %s, %s)"
    execute_dynamic_query(query, (user_id, conversation_log_id, feedback_text, rating))
