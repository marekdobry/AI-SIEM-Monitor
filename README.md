# AI-SIEM-Monitor
A Python-based SIEM monitoring system that detects, classifies, and logs security alerts from Wazuh in real time using AI for severity analysis.

## Features

- **AI-powered classification**: Uses a trained AI model to classify alerts as **HIGH** or **LOW** severity.
- **Automated ticket creation**: Generates tickets for high-severity alerts and logs them in a CSV file.
- **Duplicate prevention**: Ensures that the same alert is not processed multiple times.

---

## Project Structure
| `main.py` | Entry point to load and classify Wazuh alerts. |
| `watch_alerts.py` | Continuously watches the Wazuh alerts file for new alerts. |
| `ai_model.py` | Contains the AI model for classifying alert severity. |
| `ticket_manager.py` | Handles ticket creation and logging. |
| `wazuh_reader.py` | Reads and parses Wazuh alerts from JSON. |
| `fake_alert.py` | Utility for testing alerts without generating real Wazuh alerts. |
| `requirements.txt` | Python dependencies for the project. |
| `.gitignore` | Excludes environment, logs, and sensitive files from the repo. |
| `README.md` | Project documentation. |
