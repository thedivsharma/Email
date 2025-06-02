"""
Main script to analyze an email's content using the analyze_email function
and print the response.
"""

import json
from services.analyzer import EmailAnalysisResponse, Analyzer
from utils.constants import DEFAULT_MODEL


if __name__ == "__main__":
    EMAIL_CONTENT = """
        Hi team,  
    We’re facing deployment issues on the cloud server.  
    Please coordinate with the team for an urgent fix.  
    Regards,  
    blah blah blah

    """
    analyzer = Analyzer(DEFAULT_MODEL) 
    result = analyzer.analyze(EMAIL_CONTENT)
    
    if isinstance(result, EmailAnalysisResponse): 
        print(result.model_dump_json(indent=2))
    else:
        print(json.dumps(result, indent=2)) 