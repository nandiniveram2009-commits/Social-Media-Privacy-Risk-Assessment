import pytest
from backend.services.assessment_engine import extract_privacy_features
from backend.services.scoring_engine import calculate_category_scores, calculate_overall_risk
from backend.services.improvement_simulator import simulate_improvements

def test_fully_private_profile():
    responses = {
        "profile_visibility": "PRIVATE",
        "search_engine_visible": "NO",
        "phone_public": "NO",
        "email_public": "NO",
        "mfa_enabled": "YES"
    }
    features = extract_privacy_features(responses)
    scores = calculate_category_scores(features)
    overall, level = calculate_overall_risk(scores)
    assert overall < 25
    assert level == "LOW"

def test_fully_public_profile():
    responses = {
        "profile_visibility": "PUBLIC",
        "search_engine_visible": "YES",
        "phone_public": "YES",
        "email_public": "YES",
        "location_public": "YES",
        "mfa_enabled": "NO",
        "unknown_connections": "YES",
        "tag_review_enabled": "NO",
        "third_party_apps_reviewed": "NO"
    }
    features = extract_privacy_features(responses)
    scores = calculate_category_scores(features)
    overall, level = calculate_overall_risk(scores)
    assert overall > 70
    assert level == "CRITICAL"

def test_improvement_simulator():
    res = simulate_improvements(85.0, ["enable_mfa", "hide_phone", "disable_realtime_location"])
    assert res['simulated_score'] < 85.0
    assert res['points_reduced'] > 0
