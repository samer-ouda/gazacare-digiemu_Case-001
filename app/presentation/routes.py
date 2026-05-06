from fastapi import APIRouter
from app.application.triage_service import run_triage
from app.application.verify_service import verify_snapshot

router = APIRouter()

@router.post("/triage")
def triage(data: dict):
    return run_triage(data)

@router.post("/verify")
def verify(payload: dict):
    snapshot = payload["snapshot"]
    receipt = payload["receipt"]
    return verify_snapshot(snapshot, receipt)