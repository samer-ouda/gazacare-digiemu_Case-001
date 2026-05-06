from .hashing import compute_hash

def build_receipt(input_data, decision, policy, state_hash):
    return {
        "input_ref": compute_hash(input_data),
        "output_ref": compute_hash(decision),
        "policy_ref": compute_hash(policy),
        "state_hash": state_hash
    }