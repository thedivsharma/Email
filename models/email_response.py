"""
Data model for the email analysis response.
"""
from typing import List
from pydantic import BaseModel

class EmailAnalysisResponse(BaseModel):
    """
    This is the parsed response for an analyzed email:
        subject (str): The email subject
        teams (List[str]): List of teams to send the email to
    """
    subject: str
    teams: List[str]
