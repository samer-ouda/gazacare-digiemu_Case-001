from app.domain.rules import apply_rules
from app.domain.models import build_snapshot
from app.infrastructure.hashing import compute_hash
from app.infrastructure.receipt import build_receipt

def run_triage(data):
    decision_value, rule_id = apply_rules(data)

    decision = {
        "triage_level": decision_value,
        "matched_rule_id": rule_id
    }

    policy = {"policy_id": "gaza_policy_v1"}

    snapshot = build_snapshot(data, policy, decision)
    state_hash = compute_hash(snapshot)

    receipt = build_receipt(data, decision, policy, state_hash)

    return {
        "decision": decision,
        "snapshot": snapshot,
        "state_hash": state_hash,
        "receipt": receipt
    }