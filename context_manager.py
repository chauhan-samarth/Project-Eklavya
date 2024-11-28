class ContextManager:
    def __init__(self):
        self.context = {}

    def update_context(self, user_id, message, response):
        if user_id not in self.context:
            self.context[user_id] = []
        self.context[user_id].append((message, response))

    def get_last_message(self, user_id):
        return self.context[user_id][-1] if user_id in self.context and self.context[user_id] else None
