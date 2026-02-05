import json
import os
from pdf_reader import extract_text_from_pdf, extract_text_from_txt
from field_extractor import extract_fields
from validator import find_missing_fields
from router import route_claim

INPUT_FILE = "data/sample_fnol.txt"

def process_claim(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_txt(file_path)

    fields = extract_fields(text)
    missing_fields = find_missing_fields(fields)
    route, reasoning = route_claim(fields, missing_fields)

    result = {
        "extractedFields": fields,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reasoning
    }

    return result

if __name__ == "__main__":
    output = process_claim(INPUT_FILE)

    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w") as f:
        json.dump(output, f, indent=4)

    print("✅ Claim processed successfully")
    print(json.dumps(output, indent=4))
