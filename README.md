# Cybersecurity Log Analysis & Incident Investigation

## Overview

This project demonstrates a Python-based approach to analyzing authentication logs and identifying potentially suspicious login activity. A simulated security log was analyzed to identify repeated failed authentication attempts, targeted accounts, suspicious IP addresses, and successful logins following repeated failures.

## Project Type

* **Type:** Individual Cybersecurity Project
* **Tools:** Python, Git, GitHub
* **Focus:** Security Log Analysis & Incident Investigation

## Investigation

The analysis identified a suspicious authentication pattern involving the `admin` account.

The IP address `185.220.101.14` generated five consecutive failed login attempts against the `admin` account. Approximately one minute later, a successful login from the same IP address was recorded.

This pattern was flagged for further investigation because repeated failed authentication attempts followed by a successful login can be consistent with attempted password guessing or brute-force activity.

Because the dataset is simulated, the activity cannot be confirmed as a real attack.

## Python Analysis

The `analyze_logs.py` script:

* Reads authentication events from the security log.
* Identifies failed and successful login attempts.
* Counts failed attempts by IP address.
* Identifies targeted user accounts.
* Flags IP addresses with repeated failed authentication attempts.
* Detects successful logins originating from suspicious IP addresses.

## Key Finding

**Suspicious IP:** `185.220.101.14`

**Targeted Account:** `admin`

**Failed Attempts:** 5

**Successful Login After Failed Attempts:** Yes

The automated analysis successfully identified this event for additional investigation.

## Recommended Response

If this activity occurred in a real environment, recommended actions would include:

1. Verify whether the successful `admin` login was authorized.
2. Review additional authentication and system logs.
3. Reset the account credentials if unauthorized access is suspected.
4. Monitor the suspicious IP address for additional activity.
5. Consider account lockout or authentication rate-limiting controls.

## Skills Demonstrated

* Security Log Analysis
* Authentication Monitoring
* Incident Investigation
* Python
* Pattern Recognition
* Threat Identification
* Security Documentation
* Git & GitHub


## Project Structure

```text
cybersecurity-log-analysis-project/
│
├── README.md
├── analyze_logs.py
├── incident_report.md
└── security.log
```

### File Descriptions

* **`analyze_logs.py`** — Python script that analyzes authentication logs and identifies suspicious login patterns.
* **`security.log`** — Simulated authentication log containing successful and failed login events.
* **`incident_report.md`** — Security investigation report documenting the findings, analysis, and recommended response.
* **`README.md`** — Project overview, investigation methodology, key findings, and skills demonstrated.

