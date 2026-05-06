def apply_rules(data):
    red_flags = any(data["red_flags"].values())
    fever = "fever" in data["symptoms"]
    cough = "cough" in data["symptoms"]
    spo2 = data["vitals"]["oxygen_saturation_percent"]
    rr = data["vitals"]["respiratory_rate_per_min"]

    if red_flags:
        return "urgent_referral", "R001"

    if fever and cough and not red_flags and spo2 >= 95 and rr <= 20:
        return "non_urgent_clinical_review", "R002"

    return "unknown", None