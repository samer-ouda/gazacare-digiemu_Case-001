def build_snapshot(input_data, policy, decision):
    return {
        "triage_input": input_data,
        "policy": policy,
        "decision": decision
    }