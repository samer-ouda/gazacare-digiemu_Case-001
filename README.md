🏥 GazaCare DigiEmu System
GazaCare DigiEmu is a clinical decision-support and digital emulation system designed to simulate patient triage, validate data integrity, and support structured healthcare decision-making using rule-based logic and verification mechanisms.

🚀 Project Overview
GazaCare AI — Case 001 Documentation (Proof of Concept)
This document describes Case 001 as a technical proof-of-concept for deterministic verification and traceability in GazaCare AI. It demonstrates how a fixed input leads to a reproducible decision and a consistent cryptographic hash, and how any modification leads to a mismatch.
Step 1: Input Definition
The system receives structured patient input including symptoms, red flags, and vital signs.
{
  "case_id": "GZC-CASE-001",
  "symptoms": ["cough", "fever"],
  "red_flags": {
    "chest_pain": false,
    "confusion": false,
    "severe_breathing_difficulty": false,
    "unconscious": false
  },
  "vitals": {
    "oxygen_saturation_percent": 97,
    "respiratory_rate_per_min": 18
  }
}
Step 2: Decision Generation
"decision": {
      "triage_level": "non_urgent_clinical_review",
      "matched_rule_id": "R002"
    }

Decision Output:
- Triage Level: non_urgent_clinical_review
- Matched Rule ID: R002
Step 3: Snapshot Creation
A full snapshot is created combining input, policy, and decision. This ensures reproducibility.
"snapshot": {
    "triage_input": {
      "case_id": "GZC-CASE-001",
      "symptoms": [
        "cough",
        "fever"
      ],
      "red_flags": {
        "chest_pain": false,
        "confusion": false,
        "severe_breathing_difficulty": false,
        "unconscious": false
      },
      "vitals": {
        "oxygen_saturation_percent": 97,
        "respiratory_rate_per_min": 18
      }
    },
    "policy": {
      "policy_id": "gaza_policy_v1"
    },
    "decision": {
      "triage_level": "non_urgent_clinical_review",
      "matched_rule_id": "R002"
    }
 
Step 4: Hash Generation (state_hash)
The snapshot is normalized and hashed using SHA-256 to produce a unique state hash.
Generated state_hash:
963f6672c539fe51c2d85450e8a83410f12fc88b604cbebcf8374a9c1edc0fd4

Step 5: Receipt Generation
A receipt is generated to store references to each component hash for traceability.
Receipt:
- input_ref: e62d5ed237f2c6be763a8c7bfe36bec8b200b213f50a8e943e7097db95b9c7f4
- output_ref: 53eed24df8bacf6c732e6097de36838e913ba60425bec00737fe663a9d393cc4
- policy_ref: 58078aa261b884ec04f662953e8e76586a17a8bd01752ffe8818ea08386adfd2
- state_hash: 963f6672c539fe51c2d85450e8a83410f12fc88b604cbebcf8374a9c1edc0fd4

Step 6: Verification Logic
If the same input is used again, the same hash is generated → PASS.
If any small change is made, the hash changes → FAIL.
{  "result": "PASS"}

Step 7: Modification in input 
When we make a modification in input for example in respiratory_rate_per_min": 19 
},
      "vitals": {
        "oxygen_saturation_percent": 97,
        "respiratory_rate_per_min": 19
      }
    },

Its result change in hash cause Failed in verification 
{  "result": "FAIL"}
Conclusion
This case demonstrates deterministic behavior, reproducibility, and integrity verification.

Important: This is a technical proof-of-concept only and not a medical diagnostic system.
🛠️ Tech Stack
Python 3.x
FastAPI / Flask
Pydantic
SHA-256 hashing
Uvicorn

⚙️ Installation & Setup
1. Clone repository
git clone https://github.com/samer-ouda/gazacare-digiemu_Case-001.git
cd gazacare-digiemu_Case-001
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run server
uvicorn app.main:app --reload

📌 Example Usage (cURL)
Triage
curl -X POST "http://127.0.0.1:8000/triage" \
-H "Content-Type: application/json" \
-d '{...}'
Verify
curl -X POST "http://127.0.0.1:8000/verify" \
-H "Content-Type: application/json" \
-d '{...}'

📈 Future Improvements
AI-based triage prediction (ML integration)
FHIR compatibility
PostgreSQL database integration
JWT authentication
Audit logging system
Web dashboard UI

👨‍💻 Author
Samer Ouda & Bruno Baumgartner
GazaCare DigiEmu Project

📄 License
For educational and research purposes only.
