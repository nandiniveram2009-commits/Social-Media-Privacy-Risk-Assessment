"""
PURPOSE: Main Flask application and REST API routing layer.
"""

import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from services.assessment_engine import extract_privacy_features
from services.scoring_engine import calculate_category_scores, calculate_overall_risk
from services.findings_engine import generate_privacy_findings
from services.recommendation_engine import generate_recommendations
from services.improvement_simulator import simulate_improvements

app = Flask(__name__, template_folder="../frontend", static_folder="../frontend")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/assessment")
def assessment_page():
    return render_template("assessment.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/api/assessment", methods=["POST"])
def api_assessment():
    data = request.json or {}
    features = extract_privacy_features(data)
    category_scores = calculate_category_scores(features)
    overall_score, risk_level = calculate_overall_risk(category_scores)
    findings = generate_privacy_findings(features)
    recommendations = generate_recommendations(findings)
    
    return jsonify({
        "status": "success",
        "overall_score": overall_score,
        "risk_level": risk_level,
        "category_scores": category_scores,
        "findings": findings,
        "recommendations": recommendations,
        "privacy_disclaimer": "Educational privacy risk assessment framework."
    })

@app.route("/api/assessment/simulate-improvement", methods=["POST"])
def api_simulate():
    data = request.json or {}
    current_score = float(data.get("current_score", 50.0))
    changes = data.get("changes", [])
    result = simulate_improvements(current_score, changes)
    return jsonify(result)

@app.route("/api/dashboard/stats", methods=["GET"])
def api_dashboard_stats():
    # Return aggregated metrics for synthetic demo dashboard
    return jsonify({
        "total_assessments_evaluated": 1245,
        "average_risk_score": 58.4,
        "risk_distribution": {"LOW": 180, "MODERATE": 310, "HIGH": 512, "CRITICAL": 243},
        "top_weaknesses": [
            {"weakness": "MFA Disabled", "percentage": 68.5},
            {"weakness": "Public Phone Number", "percentage": 42.1},
            {"weakness": "Real-time Location", "percentage": 51.3}
        ]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)