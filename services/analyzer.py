"""Analyzer module for processing and interpreting email content."""

from typing import Union
from models.email_response import EmailAnalysisResponse
from services.prompt_builder import PromptBuilder
from services.api import APIHandler
from services.response_handler import ResponseHandler

class Analyzer:
    """Analyzer class that processes email content using LLMs."""

    def __init__(self, model: str):
        self.model = model
        self.api_handler = APIHandler(model)

    def analyze(self, email_text: str) -> Union[EmailAnalysisResponse, dict]:
        """Analyze the given email text and return structured response."""
        try:
            messages = PromptBuilder.build_prompt(email_text)
            response_data = self.api_handler.send_request(messages, EmailAnalysisResponse)
            content = response_data["choices"][0]["message"]["content"].strip()

            return ResponseHandler().parse_response(content)

        except Exception as e: # pylint: disable=broad-exception-caught
            return {"error": str(e)}
