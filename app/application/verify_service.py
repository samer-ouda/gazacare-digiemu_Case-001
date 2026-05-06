from app.infrastructure.hashing import compute_hash

def verify_snapshot(snapshot, receipt):
    new_hash = compute_hash(snapshot)

    if new_hash == receipt["state_hash"]:
        return {"result": "PASS"}
    else:
        return {"result": "FAIL"}