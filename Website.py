
class Website:

    def __init__(self, name, description, company, upload_date, last_date, has_salary, hr_email):
        self.name = name
        self.description = description
        self.company = company
        self.upload_date = upload_date
        self.last_date = last_date
        self.has_salary = has_salary
        self.hr_email = hr_email

    def __str__(self):
        return f"""{self.name} {self.company} {self.upload_date} {self.last_date} {self.has_salary} {self.hr_email}"""
