import re

def extract_fields(text):
    patterns = {
        "policy_number": r"Policy Number[:\s]+(.+)",
        "policyholder_name": r"Name of Insured[:\s]+(.+)",
        "date_of_loss": r"Date of Loss[:\s]+(.+)",
        "location": r"Location of Loss[:\s]+(.+)",
        "description": r"Description of Accident[:\s]+(.+)",
        "estimated_damage": r"Estimate Amount[:\s]+(.+)"
    }

    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        extracted[key] = match.group(1).strip() if match else None

    return extracted
