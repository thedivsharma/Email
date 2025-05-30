from typing import Union
import re
from services.parser import Parser
from models.email_response import EmailAnalysisResponse

class ResponseHandler:
    def parse_response(self, content: str) -> Union[EmailAnalysisResponse, dict]:
        reformatted = re.search(r"```(?:json)?\n(.*?)\n```", content, re.DOTALL)
        if not reformatted:
            return {"error": "Unable to parse JSON block from response"}

        json_text = reformatted.group(1)
        parsed_result = Parser(json_text).parse()

        if "error" not in parsed_result:
            return EmailAnalysisResponse(**parsed_result)

        return parsed_result
