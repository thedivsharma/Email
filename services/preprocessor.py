from transformers import pipeline

class EmailPreprocessor:
    def __init__(self):
        # Option 1: Named Entity Recognition
        self.ner = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)
         
        # Option 2: Zero-Shot Classification
        self.zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.team_labels = [
            "Engineering", "IT Support", "Cloud Team", "Sales", "Product", 
            "Finance", "Marketing", "HR", "Security", "Data Science"
        ]

    def extract_entities(self, email_text: str):
        """Extract entities (names, orgs, etc.) using NER."""
        entities = self.ner(email_text)
        return list(set(ent["word"] for ent in entities if ent["entity_group"] in {"ORG", "PER"}))

    def classify_teams(self, email_text: str):
        """Infer likely teams using zero-shot classification."""
        result = self.zero_shot(email_text, self.team_labels, multi_label=True)
        return [label for label, score in zip(result["labels"], result["scores"]) if score > 0.5]
