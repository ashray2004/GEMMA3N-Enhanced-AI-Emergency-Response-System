from app.database import engine
from sqlalchemy import text

names = [
    ("Jennifer Davis", "Anjali Singh"),
    ("Jennifer Smith", "Anjali Patel"),
    ("John Smith", "Rahul Sharma"),
    ("Jane Doe", "Priya Singh"),
    ("Robert Johnson", "Amit Kumar"),
    ("Robert Miller", "Suresh Yadav"),
    ("Mary Williams", "Sunita Verma"),
    ("James Brown", "Vijay Gupta"),
    ("Michael Brown", "Ravi Tiwari"),
    ("Linda Wilson", "Kavita Yadav"),
    ("Sarah Williams", "Anjali Singh"),
    ("David Johnson", "Deepak Joshi"),
    ("Lisa Wilson", "Rekha Gupta"),
    ("Maria Garcia", "Neha Sharma"),
]

doctors = [
    ("Dr. Williams", "Dr. Gupta"),
    ("Dr. Johnson", "Dr. Verma"),
    ("Dr. Smith", "Dr. Sharma"),
    ("Dr. Brown", "Dr. Patel"),
    ("Dr. Davis", "Dr. Singh"),
    ("Dr. Jones", "Dr. Mishra"),
    ("Dr. Miller", "Dr. Kumar"),
    ("Dr. Wilson", "Dr. Yadav"),
]

with engine.connect() as conn:
    for old, new in names:
        conn.execute(text(f"UPDATE triage_patients SET name = '{new}' WHERE name LIKE '%{old}%'"))
    for old, new in doctors:
        conn.execute(text(f"UPDATE triage_patients SET assigned_doctor = '{new}' WHERE assigned_doctor LIKE '%{old}%'"))
    conn.commit()
    print('Done!')
