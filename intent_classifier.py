from transformers import pipeline

class IntentClassifier:
    def __init__(self):
        self.nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def classify_intent(self, query, candidate_labels):
        result = self.nlp(query, candidate_labels)
        return result['labels'][0]
