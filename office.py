class office:
    def __init__(self, name, *employees):
        self.name = name
        self.employees = employees

    @staticmethod
    def get_all_employees():
        print(" Your skills is: ")
        for employee in office.employees:
            print(f" => {employee}")

    @staticmethod
    def display_office():
        print(f" your name is: {office.name}")


skills = ["html", "css", "js"]
office = office("abdo", *skills)
office.display_office()
office.get_all_employees()
