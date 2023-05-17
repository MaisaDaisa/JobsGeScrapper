from Website import Website
import sqlite3


class WebsiteDB:

    def __init__(self, namedb):
        self.conn = sqlite3.connect(namedb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS websitedb(
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                company TEXT,
                upload_date TEXT,
                last_date TEXT,
                has_salary TEXT,
                hr_email TEXT
                );
            """)

    def add_website(self, website):
        self.cursor.execute("""
            INSERT INTO websitedb VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.get_last_id()+1, website.name, website.description, website.company, website.upload_date, website.last_date, website.has_salary, website.hr_email))
        self.conn.commit()
    def get_last_id(self):
        self.cursor.execute("""
            SELECT id FROM websitedb ORDER BY id DESC LIMIT 1
        """)
        row = self.cursor.fetchone()
        if row is None:
            return 0
        return row[0]