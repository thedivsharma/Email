class PromptBuilder:
    @staticmethod
    def build_prompt(email_text: str):
        system_message = (
                "Extract the subject and the teams mentioned in the following email. "
                "Return only a JSON object, no extra text. "
                "If no teams are mentioned, intelligently infer,"
                "which teams should receive the email. "
                "Never leave teams empty. "
                "Multiple target teams are possible."
            )
        return [
                {"role": "system", "content": system_message},
                {"role": "user", "content": email_text}
            ]
