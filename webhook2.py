from flask import Flask, request, jsonify
import os
import json
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


SENDER_EMAIL = "fatemeh.saeedi2001@gmail.com"
SENDER_PASSWORD = "ohpg hjqf qqlc shnc" 
RECIPIENT_EMAIL = "sd.fatemeh2002@gmail.com"


def send_email_alert(summary, description):
    subject = f"[ALERT] {summary}"
    body = f"{summary}\n\n{description}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print(" Email sent successfully.")
    except Exception as e:
        print(f" Failed to send email: {e}")


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        if not data or "alerts" not in data:
            return jsonify({"error": "Invalid payload"}), 400

        for alert in data["alerts"]:
            team = alert.get("labels", {}).get("team", "unknown_team")
            severity = alert.get("labels", {}).get("severity", "unknown_severity")
            summary = alert.get("annotations", {}).get("summary", "No summary")
            description = alert.get("annotations", {}).get("description", "No description")

           
            print(f" ALERT: [{team.upper()}] [{severity.upper()}]\n{summary}\n{description}\n")

           
            send_email_alert(summary, description)

            
            dir_path = os.path.join("alerts", team)
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, f"{severity}.json")

            alert_data = {
                "summary": summary,
                "description": description
            }

            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    existing_alerts = json.load(f)
            else:
                existing_alerts = []

            existing_alerts.append(alert_data)

            with open(file_path, "w") as f:
                json.dump(existing_alerts, f, indent=2)

        return jsonify({"message": "Alerts received"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
