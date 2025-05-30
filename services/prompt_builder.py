from services.preprocessor import EmailPreprocessor

class PromptBuilder:
    @staticmethod
    def build_prompt(email_text: str):
        system_message = (
            "Extract the subject and the teams mentioned in the following email. "
            "Return only a JSON object, no extra text. "
            "If no teams are mentioned, intelligently infer which teams should receive the email. "
            "Never leave teams empty. Multiple target teams are possible."
        )

        # Add inferred teams from preprocessor
        preprocessor = EmailPreprocessor()
        inferred_teams = preprocessor.classify_teams(email_text)
        
        if inferred_teams:
            email_text = f"[Likely teams: {', '.join(inferred_teams)}]\n\n" + email_text

        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": email_text}
        ]
