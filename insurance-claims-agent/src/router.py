def route_claim(fields, missing_fields):
    if missing_fields:
        return "Manual Review", "Missing mandatory fields"

    description = fields.get("description", "").lower()

    try:
        damage = float(fields.get("estimated_damage", "0").replace(",", ""))
    except:
        damage = 0

    if any(word in description for word in ["fraud", "inconsistent", "staged"]):
        return "Investigation", "Suspicious keywords detected"

    if "injury" in description:
        return "Specialist Queue", "Injury-related claim"

    if damage < 25000:
        return "Fast-track", "Low estimated damage"

    return "Manual Review", "High damage amount"
