from transformers import pipeline

class EmailPreprocessor:
    def __init__(self):
        
        self.zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.team_labels = [
            "IT Department", "Sales", "Product", 
            "Finance", "Marketing", "HR team","Quality Assurance",
            "Testing"
        ]

    def classify_teams(self, email_text: str):
        """Infer likely teams using zero-shot classification."""
        result = self.zero_shot(email_text, self.team_labels, multi_label=True)
        print("zero shot class", [label for label, score in zip(result["labels"], result["scores"]) if score > 0.9])
        return [label for label, score in zip(result["labels"], result["scores"]) if score > 0.9]
