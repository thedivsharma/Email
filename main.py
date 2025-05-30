"""
Main script to analyze an email's content using the analyze_email function
and print the response.
"""

import json
from services.analyzer import EmailAnalysisResponse, Analyzer
from utils.constants import DEFAULT_MODEL


if __name__ == "__main__":
    EMAIL_CONTENT = """
        Listen up,
        We wanted a demo with your cloud product and also the integration of it.
    """
    analyzer = Analyzer(DEFAULT_MODEL) 
    result = analyzer.analyze(EMAIL_CONTENT)
    
    if isinstance(result, EmailAnalysisResponse): 
        print(result.model_dump_json(indent=2))
    else:
        print(json.dumps(result, indent=2))  
