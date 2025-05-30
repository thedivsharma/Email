Advanced Email Content Extraction Pipeline
A robust NLP-driven pipeline leveraging a state-of-the-art LLM API for semantic parsing of unstructured email corpora. Implements prompt engineering and schema-constrained generation to extract discrete entities (subject, teams) in JSON format.

Core Features:

Dynamic prompt orchestration: Contextualizes input for maximal extraction fidelity.

Schema validation: Enforces strict output conformance via Pydantic models.

Resilient parsing layer: Employs regex-driven JSON extraction and defensive error handling.

Extensible modular design: Decoupled components for prompt building, API interfacing, and parsing.