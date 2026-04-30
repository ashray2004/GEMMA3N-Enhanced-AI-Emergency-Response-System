from app.database import engine
from sqlalchemy import text
with engine.connect() as conn:
    conn.execute(text("UPDATE crowd_reports SET location = 'Lucknow, UP' WHERE location LIKE '%San Francisco%'"))
    conn.execute(text("UPDATE crowd_reports SET location = 'Lucknow, UP' WHERE location LIKE '%CA%'"))
    conn.commit()
    print('Done!')
