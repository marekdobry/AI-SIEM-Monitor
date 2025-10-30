import csv
from datetime import datetime
import os

def create_ticket(alert):
    ticket_file = "tickets.csv"
    file_exists = os.path.isfile(ticket_file)
    description = alert.get('rule', {}).get('description', 'No description available')

    with open(ticket_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Alert_Description", "Action", "Status"])
        
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            description,
            "Escalate to SOC analyst",
            "Open"
        ])
    print(f"🪪 Ticket created for: {description}")
