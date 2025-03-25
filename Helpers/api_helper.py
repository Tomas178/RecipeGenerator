import os
import sys


def is_valid_APIs() -> None:
    """Checks if the API keys are valid."""
    check_OpenAI_API_key()
    check_rapid_API_key()
    check_OpenAI_org_id()
    check_OpenAI_project_id()


def check_OpenAI_API_key() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OpenAI API key not found!")


def check_rapid_API_key() -> None:
    api_key = os.getenv("RAPID_API_KEY")
    if not api_key:
        sys.exit("Rapid API key not found!")


def check_OpenAI_org_id() -> None:
    api_key = os.getenv("OPENAI_ORG_ID")
    if not api_key:
        sys.exit("OpenAI org ID not found!")


def check_OpenAI_project_id() -> None:
    api_key = os.getenv("OPENAI_PROJECT_ID")
    if not api_key:
        sys.exit("OpenAI project ID not found!")
