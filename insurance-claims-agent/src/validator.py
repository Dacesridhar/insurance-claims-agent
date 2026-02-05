MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "date_of_loss",
    "description"
]

def find_missing_fields(fields):
    return [field for field in MANDATORY_FIELDS if not fields.get(field)]
