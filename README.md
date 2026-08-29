# Phishing-awairness# Phishing Awareness Simulation Using Social Engineering Techniques

## Academic Project

This repository contains a **controlled, local-only phishing awareness simulation** for an academic cybersecurity project.

### Safety design
- No real company is impersonated.
- No email is sent automatically.
- No external network service is contacted by the web application.
- Password values are never stored, transmitted, or logged.
- The login form records only that a demonstration data-entry attempt occurred.
- Participants should be informed and give consent before testing.
- The sample CSV is **demonstration data**, not real participant data.

## Project structure

```text
Phishing_Awareness_Simulation_Project/
├── web/
│   ├── index.html
│   ├── email.html
│   ├── login.html
│   ├── result.html
│   ├── styles.css
│   └── app.js
├── data/
│   └── demo_results.csv
├── analysis/
│   └── analyze.py
├── docs/
│   ├── Project_Report.docx
│   ├── Project_Presentation.pptx
│   ├── Participant_Consent_Form.docx
│   └── demonstration_results_chart.png
├── screenshots/
├── run_local.bat
├── run_local.sh
├── requirements.txt
└── README.md
```

## Run locally

### Windows
Double-click `run_local.bat`, then open the displayed local address.

### Linux/macOS
Run:

```bash
bash run_local.sh
```

Then open the local address shown in the terminal.

## Testing workflow

1. Read the consent form and obtain informed consent.
2. Open `index.html` through the local server.
3. Open the simulated email.
4. Observe whether a participant reports it, clicks it, or proceeds to the demonstration page.
5. If the participant reaches the login page, explain that it is a simulation.
6. Never ask for or retain a real password.
7. Use the Results page to view local counters.
8. Replace `data/demo_results.csv` with properly anonymized, consented results if you conduct a real classroom test.
9. Re-run `analysis/analyze.py` to generate the chart.

## Ethical boundaries

Do not send this simulation to people without authorization. Do not use a real organization name, real login page, real credentials, credential harvesting, malware, tracking pixels, or deceptive external links.

## Learning outcomes

The project demonstrates:
- Social-engineering principles
- Phishing indicators
- Safe simulation design
- Client-side HTML/CSS/JavaScript
- Basic metrics and data analysis
- Security awareness and mitigation
- Ethical considerations in cybersecurity testing
