# code_submission.py
# Decision Support Module — v0.9
# Submitted by: Junior Product Engineer
# Squad: Procurement Journey Squad
# Date: 2026-02-17

import json
from datetime import datetime


# -------------------------------------------------------
# FR-002: Explainable Recommendations — IMPLEMENTED
# Each decision output includes policy reference and OKR
# -------------------------------------------------------

POLICY_RULES = {
    "data_privacy": "NBK Regulation 168 — Customer Data Protection",
    "ui_change":    "Internal UX Policy v3.2",
    "api_change":   "API Governance Charter — Section 4",
    "payment_flow": "PCI-DSS Compliance Requirement 6.3",
}

def generate_recommendation(initiative_type: str, risk_score: int) -> dict:
    """
    Returns an explainable recommendation for a given initiative.
    References the relevant internal policy and OKR alignment.
    """
    policy = POLICY_RULES.get(initiative_type, "General Product Policy v1.0")
    return {
        "initiative_type": initiative_type,
        "risk_score": risk_score,
        "policy_reference": policy,
        "okr_alignment": "Reduce Approval Cycle Time by 40%",
        "recommendation": "Proceed with standard squad review.",
        "confidence": "High",
        "generated_at": datetime.utcnow().isoformat(),
    }


# -------------------------------------------------------
# FR-001: Risk-Calibrated Escalation — PARTIAL (FAILS)
# BUG: ALL initiatives are sent to committee regardless
# of risk level. Should only escalate high-risk (score > 70).
# -------------------------------------------------------

def evaluate_initiative(initiative_type: str, risk_score: int) -> dict:
    """
    Evaluates a proposed product change and determines escalation path.
    """
    recommendation = generate_recommendation(initiative_type, risk_score)

    # INCORRECT IMPLEMENTATION:
    # All initiatives are routed to the Governance Committee.
    # The risk_score threshold logic was deferred to v1.1.
    escalation_required = True  # Should be: risk_score > 70

    return {
        "initiative": initiative_type,
        "risk_score": risk_score,
        "escalation_required": escalation_required,
        "recommendation": recommendation,
    }


# -------------------------------------------------------
# FR-003: Real-Time Customer Signal Aggregation — MISSING
# BUG: Uses a static Brand Health Tracking PDF report.
# Should connect to live Kafka stream: app.user.events
# -------------------------------------------------------

def get_customer_signals() -> dict:
    """
    Returns customer insight data for the squad dashboard.
    """
    # INCORRECT IMPLEMENTATION:
    # Reading from a static monthly export file.
    # Real-time Kafka integration was deprioritized this sprint.
    report_path = "data/brand_health_tracking_jan2026.pdf"

    # Simulated static data from the monthly PDF report
    return {
        "source": report_path,
        "report_type": "Brand Health Tracking (Monthly PDF)",
        "last_updated": "2026-01-31",
        "nps_score": 42,
        "csat_score": 3.8,
        "warning": "Data is 17 days old. Real-time stream not connected."
    }


# -------------------------------------------------------
# FR-004: OKR-to-Outcome Translation — IMPLEMENTED
# Maps OKRs to measurable product outcomes
# -------------------------------------------------------

OKRS = [
    {
        "objective": "Improve Super App onboarding experience",
        "key_results": [
            {"metric": "Task completion rate", "target": "85%", "current": "71%"},
            {"metric": "Drop-off reduction", "target": "-30%", "current": "-12%"},
            {"metric": "NPS delta post-release", "target": "+8", "current": "+3"},
        ]
    },
    {
        "objective": "Reduce internal approval cycle time",
        "key_results": [
            {"metric": "Avg days to approval", "target": "2 days", "current": "7 days"},
            {"metric": "Auto-approved initiatives %", "target": "60%", "current": "0%"},
        ]
    }
]

def get_okr_dashboard() -> dict:
    """
    Returns current OKR progress mapped to customer outcome metrics.
    Feature delivery counts are excluded.
    """
    return {
        "okrs": OKRS,
        "tracking_mode": "customer_outcomes",
        "feature_count_tracking": False,
    }


# -------------------------------------------------------
# MAIN: Run the full Decision Support Module
# -------------------------------------------------------

if __name__ == "__main__":
    print("=== Decision Support Module — Halyk Bank ===\n")

    # Evaluate a sample initiative
    result = evaluate_initiative("payment_flow", risk_score=45)
    print("Initiative Evaluation:")
    print(json.dumps(result, indent=2))

    print("\nCustomer Signals:")
    signals = get_customer_signals()
    print(json.dumps(signals, indent=2))

    print("\nOKR Dashboard:")
    okrs = get_okr_dashboard()
    print(json.dumps(okrs, indent=2))
