# Social-Media-Privacy-Risk-Assessment
Privacy-focused cybersecurity framework for assessing social-media exposure, account-security practices, social-engineering risk, digital-footprint risk, and personalized privacy improvements using synthetic/self-reported data.
# Social Media Privacy Risk Assessment Framework

> **Keywords (Copy-Paste for GitHub Topics & SEO):**
> `cybersecurity`, `privacy`, `social-media-privacy`, `privacy-risk`, `security-awareness`, `python`, `flask`, `react`, `typescript`, `digital-footprint`, `risk-assessment`, `grc`, `privacy-by-design`, `defensive-security`, `osint-awareness`, `identity-theft-prevention`, `mfa`, `exif-metadata`

---

## Overview
The **Social Media Privacy Risk Assessment Framework (SM-PRAF)** is an industry-grade, defensive cybersecurity and privacy engineering platform. Designed for students, security analysts, and enterprise awareness programs, it quantifies exposure across social media platforms, maps vulnerabilities to real-world Open Source Intelligence (OSINT) attack chains, and delivers actionable, prioritized remediation guidance.

The application operates on voluntary, self-reported behavioral inputs and synthetic benchmarks—strictly adhering to Privacy by Design principles by avoiding external scraping, intrusive profiling, or personal data collection.

---

## Problem Statement
Over 80% of targeted cyberattacks—including Business Email Compromise (BEC), SIM-swapping, credential stuffing, and spear-phishing—begin with Open Source Intelligence (OSINT) reconnaissance conducted against publicly available social media profiles.

Most users operate under a false sense of security, assuming that strong account credentials (such as complex passwords) make public oversharing benign. In reality, public birth dates, workplace photos, phone numbers, and live location check-ins create exploitable vectors for identity theft, physical stalking, and social engineering regardless of password strength.

---

## Objectives
- **Quantify Digital Exposure:** Calculate a normalized Privacy Risk Score (0–100) based on NIST CSF and ISO/IEC 27701 principles.
- **Categorize Threat Tiers:** Classify overall risk into four actionable categories: LOW (0–20), MODERATE (21–40), HIGH (41–70), and CRITICAL (71–100).
- **Map Threat Vectors:** Identify explicit adversary exploits (e.g., vacant-home burglary from vacation posts, SIM-swap via exposed mobile numbers, account takeover from disabled MFA).
- **Simulate Proactive Hardening:** Provide a dynamic "what-if" simulator demonstrating immediate risk reduction points (e.g., dropping 38+ points) when key defensive controls are applied.
- **Client-Side EXIF Sanitization:** Deliver an in-browser image metadata inspector and cleaner that removes GPS coordinates without transmitting bytes over the network.
- **Empower Students & Analysts:** Provide rigorous proof-of-work documentation, automated test suites, and career alignment for cybersecurity roles.

---

## Cybersecurity Relevance
This framework directly reflects core competencies across:
- **Governance, Risk & Compliance (GRC):** Privacy impact assessments (PIAs), control weighting, and audit reporting.
- **Privacy Engineering:** Data minimization, purpose limitation, and consent governance.
- **Security Operations Center (SOC) & Threat Intelligence:** Analyzing adversary reconnaissance methods and credential exposure spillover.
- **Identity & Access Management (IAM):** Multi-Factor Authentication (MFA) enforcement and third-party OAuth scope governance.
- **Security Awareness Training:** Converting technical risk indicators into practical behavioral habits.

Relevant Career Roles:
- Cybersecurity Analyst
- Privacy Analyst / Privacy Engineer
- GRC Analyst
- SOC Analyst
- Security Consultant
- IAM Analyst
- Security Awareness Specialist

---

## Privacy vs Security

| Dimension | Security (Confidentiality & Access) | Privacy (Data Minimization & Exposure) |
|---|---|---|
| **Core Definition** | Protects systems, networks, and accounts from unauthorized access or tampering. | Controls how personal information is collected, exposed, shared, and processed. |
| **Typical Controls** | Multi-Factor Authentication (MFA), AES-256 encryption, password managers, firewalls. | Audience scoping, timeline locking, EXIF stripping, pseudonymity, data minimization. |
| **Primary Failure** | Account Takeover (ATO), database credential dump, brute-force bypass. | Doxxing, SIM-swapping via PII recon, stalking, unsolicited surveillance. |
| **Example Scenario** | Account protected by a 64-character random password and hardware FIDO2 key. | User publicly posts photos of their company ID badge, car license plate, and child's school. |

> **Fundamental Rule:** Strong Account Security ≠ Strong Privacy. A mathematically unbreakable login does not protect a user whose public timeline broadcasts the answers to their banking security questions and their daily physical commute schedule.

---

## Features
1. **40-Question Defensive Questionnaire:** Comprehensive survey evaluating 10 privacy domains without ever asking for actual sensitive data.
2. **Weighted Scoring Engine:** Configurable category weighting to model custom threat environments.
3. **Cybersecurity Risk Dashboard:** High-fidelity SVG Radar chart, horizontal domain bars, and population percentile rankings.
4. **Hardening Simulator:** Interactive toggles showing real-time score drops and risk level transitions.
5. **Safe Photo EXIF Inspector & Cleaner:** 100% browser-based metadata parser and canvas-based stripper with zero server upload.
6. **1,000-Profile Synthetic Cohort:** Seeded benchmark dataset with CSV exporter and standalone Python generator.
7. **Official Privacy Impact Assessment (PIA) Report:** ISO/IEC 27701 compliant printable audit report with PDF formatting and interactive remediation checklists.
8. **Automated Verification Lab:** In-browser and command-line execution of 30 automated test cases.
9. **Dual-Stack Implementation:** Complete Python Flask REST backend paired with a modern React 19/TypeScript frontend.

---

## Architecture
```
                                 [ User / Browser ]
                                         │
                         ┌───────────────┴───────────────┐
                         ▼                               ▼
              [ 40-Question Assessment ]     [ Safe Client EXIF Lab ]
                         │                       (In-Memory Canvas)
                         ▼
             [ Feature Extraction Engine ]
             (23 Normalized Risk Weights)
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
┌───────────────────────────────┐  ┌───────────────────────────────┐
│ Category Risk Analyzers       │  │ Weighted Scoring Engine       │
│ - Category A: Profile (10%)   │  │   Sum(Score_i * Weight_i)     │
│ - Category B: Personal (15%)  │  │   -----------------------     │
│ - Category C: Location (15%)  │  │        Total Weight           │
│ - Category D: Content (10%)   │  └──────────────┬────────────────┘
│ - Category E: Connect (10%)   │                 │
│ - Category F: Tagging (5%)    │                 ▼
│ - Category G: Security (15%)  │     [ Overall Privacy Score ]
│ - Category H: 3rd-Party (5%)  │     [ Risk Level (LOW-CRIT) ]
│ - Category I: Social Eng (10%)│                 │
│ - Category J: Footprint (5%)  │                 ▼
└───────────────────────────────┘     [ Findings & Threat Engine ]
                                                  │
                                                  ▼
                                     [ Recommendation Engine ]
                                     (Immediate / Important)
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         ▼                                                 ▼
             [ Privacy Dashboard ]                            [ Hardening Simulator ]
             [ & Radar Analytics ]                            [ & PIA Audit Report  ]
```

---

## Technology Stack
- **Frontend:** React 19, TypeScript, Tailwind CSS v4, Lucide Icons.
- **Backend:** Python 3.11, Flask, Flask-CORS.
- **Database:** SQLite (Strict Privacy-by-Design schema; zero PII columns).
- **Data Analytics & Testing:** Python `csv`, `random`, `unittest`, `pytest`.

---

## Privacy Questionnaire
The framework features 40 structured questions divided evenly across 10 domains (4 questions per category). Questions utilize standardized options:
- `PUBLIC` / `FRIENDS` / `PRIVATE`
- `YES` / `NO` / `SOMETIMES` / `NOT_SURE`

Each response maps to an objective risk weight (0.0 for fully hardened to 1.0 for maximum exposure) accompanied by an adversary threat vector and remediation guidance.

---

## Risk Categories
1. **Category A: Profile Visibility (Weight: 10%)** — Search indexing, friend list discoverability, reverse lookups.
2. **Category B: Personal Information Exposure (Weight: 15%)** — Phone number, email, birth date, home neighborhood.
3. **Category C: Location Privacy & Geotagging (Weight: 15%)** — Real-time check-ins, vacation stories, routine paths.
4. **Category D: Posts & Content Sensitivity (Weight: 10%)** — Work badges, boarding passes, family details.
5. **Category E: Friends & Followers Controls (Weight: 10%)** — Accepting strangers, follower audits, close friends lists.
6. **Category F: Tagging & Mentions Governance (Weight: 5%)** — Tag approval gatekeepers, facial recognition suggestions.
7. **Category G: Authentication & Account Security (Weight: 15%)** — App-based MFA, password reuse, unrecognized login alerts.
8. **Category H: Third-Party Application Access (Weight: 5%)** — Dormant OAuth apps, over-permissioned scopes.
9. **Category I: Messaging & Social Engineering (Weight: 10%)** — Unsolicited DM links, OTP forward scams, fake job offers.
10. **Category J: Digital Footprint & Legacy Data (Weight: 5%)** — Archiving old posts, defunct accounts, OSINT self-checks.

---

## Risk Scoring
Category Score = (Sum of Risk Weights / Question Count) * 100
Overall Risk Score = Sum(Category Score * Category Weight) / Sum(Category Weights)

### Classification Tiers:
- **0–20 (LOW):** Hardened posture; minimal public exposure.
- **21–40 (MODERATE):** Standard user posture; common exposure points.
- **41–70 (HIGH):** Significant exposure; actionable OSINT attack vectors detected.
- **71–100 (CRITICAL):** Immediate vulnerability; high probability of exploitation.

---

## Privacy Findings
Findings are automatically triggered when question risk weights meet or exceed 0.5. Each finding includes:
- **Severity Tag:** `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`.
- **Adversary Threat Vector:** The concrete exploitation technique (e.g., SIM-swap, spear-phishing, PNR extraction).
- **Threat Consequence:** Real-world impact if exploited.

---

## Recommendation Engine
Remediations are prioritized dynamically based on blast radius:
- **IMMEDIATE:** High-impact mitigations requiring under 5 minutes (enabling MFA, hiding phone number, disabling live check-ins).
- **IMPORTANT:** Systematic hardening (hiding birth year, enabling tag review, revoking stale OAuth tokens).
- **GOOD PRACTICE:** Ongoing cyber hygiene (archiving posts older than 24 months, conducting quarterly self-searches).

---

## Improvement Simulator
The "What happens if I improve my settings?" simulator models the outcome of adopting defensive recommendations. By toggling specific security controls, users see:
- Real-time score recalculation (e.g., 78/100 CRITICAL -> 32/100 MODERATE).
- Quantified **Risk Reduction Points** (e.g., -46 points).
- Count of neutralized vulnerabilities.

---

## Digital Footprint
Evaluates self-reported practices regarding:
- **Active Digital Footprint:** Intentional status updates, photos, and public forum comments.
- **Passive Digital Footprint:** Involuntary metadata, third-party tags, and search engine cache snapshots.
- **Mitigation:** Retrospective data minimization through periodic archival and decommissioning of dormant services.

---

## Social Engineering Awareness
Explains how adversaries synthesize disparate public facts to craft high-conviction pretexting campaigns:
- **Workplace/Title:** Exploited for Business Email Compromise (BEC) and fake executive urgency.
- **High School/Hometown:** Exploited to answer banking security questions.
- **Travel Announcements:** Signals home vacancy and unavailability to verify wire requests.
- **Family Connections:** Exploited for emergency grandparent scams and voice cloning scams.

---

## Account Security
Assesses defensive authentication practices:
- Multi-Factor Authentication: Hardware keys/Authenticator apps (gold standard) vs. SMS OTP (vulnerable to SIM-swap) vs. Disabled.
- Password hygiene and breach spillover isolation via password managers.
- Active session inspection and unauthorized login alert configuration.

---

## Privacy Dashboard
Provides an interactive visualization suite:
- 5 Executive KPI Cards (Overall Risk, Level, High-Risk Domains, Active Controls, Population Percentile).
- Custom 10-Spoke SVG Radar Chart displaying exposure perimeter.
- Horizontal Domain Progress Bars showing weighted contribution points.
- Core Defense-in-Depth verification checklist.

---

## Privacy Report
Generates formal ISO/IEC 27701 compliant **Privacy Impact Assessment (PIA)** audit documents:
- Unique Assessment ID (e.g., PIA-2026-X8491) and ISO timestamp.
- Executive summary, domain breakdown tables, and critical findings roadmap.
- Formatted for print/PDF export (`window.print()`), standalone HTML download, and Markdown copy.

---

## Privacy by Design
1. **Data Minimization:** No personal phone numbers, emails, passwords, or street addresses are ever collected or stored.
2. **Purpose Limitation:** Inputs are processed strictly in-memory for risk calculation.
3. **Least Privilege:** Database schemas record only assessment IDs and score integers.
4. **Privacy by Default:** Zero tracking telemetry; EXIF stripping occurs entirely client-side.
5. **Right to Erasure:** Dedicated `DELETE /api/assessment/<id>` endpoint purges audit records on demand.

---

## Installation

### Prerequisites
- Node.js 18+ & npm
- Python 3.10+ & pip

```bash
# 1. Clone repository
git clone https://github.com/your-username/Social-Media-Privacy-Risk-Assessment.git
cd Social-Media-Privacy-Risk-Assessment

# 2. Setup Python Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install backend dependencies
pip install -r requirements.txt

# 4. Generate synthetic dataset (1,000 profiles)
python data/generate_dataset.py

# 5. Start Flask backend server
python backend/app.py

# 6. Install frontend dependencies and start Vite dev server (in separate terminal)
npm install
npm run dev
```

---

## Usage
1. Open your browser to `http://localhost:3000`.
2. Navigate to **Privacy Assessment** and answer the 40 questions across Categories A through J (or select a preset demo persona).
3. Click **Generate Risk Analysis & Dashboard** to view your score, SVG radar chart, and findings.
4. Explore the **Hardening Simulator** to test how changing settings reduces your score.
5. Use the **Photo EXIF Inspector** to upload an image, review embedded GPS tags, and download a sanitized copy.
6. Generate and print your official **Audit PIA Report**.
7. Run the **Verification Lab** to execute the 30 automated test cases.

---

## API Documentation

### `POST /api/assessment`
Evaluates answers and returns risk score, findings, and recommendations.

### `GET /api/assessment/<assessment_id>`
Retrieves a previously stored assessment record by ID.

### `DELETE /api/assessment/<assessment_id>`
Deletes an assessment record (enforcing GDPR Right to Erasure).

### `POST /api/assessment/simulate-improvement`
Calculates delta reduction points between current answers and hardened overrides.

### `GET /api/dashboard/stats`
Returns population statistics from the 1,000 synthetic cohort records.

### `GET /api/privacy-checklist`
Returns the standardized 18-point privacy checklist.

---

## Testing
The project includes 30 automated unit and integration tests covering:
- Fully private and fully public profile baselines.
- Explicit PII and threat vector triggers (phone, birthday, check-ins, MFA).
- Score threshold boundary transitions (20, 40, 70).
- Database persistence and right-to-erasure deletion.
- Schema validation verifying zero PII columns exist.

Run automated tests via CLI:
```bash
python -m unittest backend/tests/test_privacy_assessment.py
```
Or execute them interactively inside the web application via the **Verification Lab (30 Tests)** tab.

---

## Security & Privacy Testing
- **Schema Sanitization:** SQLite `PRAGMA table_info(assessments)` validates that no columns exist for names, phones, emails, passwords, or locations.
- **Input Validation:** REST endpoints sanitize and validate survey options against strict whitelists.
- **Local EXIF Processing:** Verified via browser network inspect tools that zero bytes of uploaded images leave the local browser context.

---

## Results
- **Synthetic Cohort Mean Score:** 52 / 100 (HIGH Risk).
- **Synthetic Cohort Median Score:** 51 / 100.
- **MFA Adoption Rate:** 34% across synthetic profiles.
- **Public Phone Exposure Rate:** 41% across synthetic profiles.
- **Simulated Hardening Efficacy:** Average observed risk reduction of 40–50 points following adoption of top recommendations.

---

## Limitations
- **Self-Reported Data:** Assessments rely on the accuracy of user-reported settings.
- **Educational Model:** Assigned weights represent educational frameworks, not an absolute guarantee against targeted zero-day exploits.
- **Platform Variability:** Specific platform settings menus change over time; recommendations focus on conceptual controls rather than ephemeral UI paths.

---

## Future Improvements
- Automated parser for GDPR/CCPA data export archives (JSON/ZIP).
- Multi-account correlation analysis across federated profiles.
- Automated quarterly email reminders to re-evaluate privacy postures.
- Browser extension for live privacy settings verification.

---

## Screenshots
- `screenshots/01_dashboard_radar.png` — Threat Radar and Executive Scorecards
- `screenshots/02_assessment_survey.png` — 40-Question Defensive Questionnaire
- `screenshots/03_hardening_simulator.png` — Before & After Improvement Simulator
- `screenshots/04_exif_inspector.png` — Safe Photo Metadata Inspector & Cleaner
- `screenshots/05_pia_report.png` — Official ISO/IEC 27701 Audit PIA Report
- `screenshots/06_verification_lab.png` — 30 Automated Test Cases Runner

---

## Learning Outcomes
- Practical application of the **NIST Privacy Framework** and **ISO/IEC 27701**.
- Engineering Privacy-by-Design software architectures.
- Translating cyber threat intelligence into user-centric risk reduction metrics.
- Building full-stack defensive cybersecurity tools with automated test suites.

---

## Ethical Disclaimer
> “This project is designed for defensive cybersecurity and privacy education. It uses synthetic or voluntarily provided assessment responses and does not scrape, track, or profile real social-media users.”

---

## Author

* **GitHub:** [nandiniverma2009](https://github.com)
* **LinkedIn:** [Nandini Verma](https://linkedin.com)
*
