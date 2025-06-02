"""
    API Request Module
"""
import requests
from pydantic import BaseModel
from utils.constants import OLLAMA_URL, HEADERS

class APIHandler:
    """
        Class to Handle the API Calls
    """
    def __init__(self, model: str):
        self.model = model

    def send_request(self, messages: list[dict], schema: BaseModel) -> dict:
        """
            Code to Send the Request
        """
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0,
            "format": self.build_format(schema)
        }

        response = requests.post(OLLAMA_URL, json=payload, headers=HEADERS, timeout=20)
        response.raise_for_status()
        return response.json()

    def build_format(self, schema:BaseModel):
        """
            Code to Get the Format
        """
        res = schema.model_json_schema()
        res.pop('title', None)
        res.pop('description', None)
        return res
