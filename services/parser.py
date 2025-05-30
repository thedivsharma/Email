"""
Parser module to clean and parse raw model output into structured data.
"""
import json
from typing import Any, Dict

class Parser:
    """
    Parser class to handle cleaning and parsing of model output.
    """

    def __init__(self, raw_text: str):
        self.raw_text = raw_text.strip().replace("\n", "").strip()

    def parse(self) -> Dict[str, Any]:
        """
        Parse the raw text into a dictionary.

        Returns:
            dict: Parsed output if valid; otherwise, error message and details.
        """
        try:
            parsed_json = json.loads(self.raw_text)
            #convert to pytohn dictionary
            if 'subject' not in parsed_json or 'teams' not in parsed_json:
                return {
                    "error": "Missing 'subject' or 'teams' in response.",
                    "details": parsed_json
                }

            return parsed_json

        except json.JSONDecodeError:
            return {"error": "Invalid JSON format", "details": self.raw_text}

        except (TypeError, ValueError) as e:
            return {"error": str(e), "details": self.raw_text}
