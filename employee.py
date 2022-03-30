import person


class employee(person):
    mood = ("happy", "tired", "lazy")

    def __init__(self, iid, car, email, salary, distance_to_work):
        self.iid = iid
        self.car = car
        self.email = email
        self.salary = salary
        if salary < 1000:
            self.salary = 1000
        else:
            self.salary = salary
        self.distance_to_work = distance_to_work

    @staticmethod
    def work(hours):
        if hours == 8:
            employee.mood = employee.mood[0]
        elif hours > 8:
            employee.mood = employee.mood[1]
        elif hours < 8:
            employee.mood = employee.mood[2]

    @classmethod
    def drive(cls, time, distance):
        return distance / time

    @staticmethod
    def refuel(fuel_rate, gasAmount=100):
        return gasAmount + fuel_rate

    @classmethod
    def send_mail(cls, fromm, to, msg, receiver_name):
        cls.fromm = fromm
        cls.to = to
        cls.msg = msg
        cls.receiver_name = receiver_name

        print(
            f" ------------------------------\n -------------MAIL-------------\n From: {fromm} \n To: {to} \n Hi, {receiver_name} "
            f" \n {msg} \n thanks\n ------------------------------\n ------------------------------")

    @staticmethod
    def display():
        print(f"your id is => {employee.iid}")
        print(f"your email is => {employee.email}")
        print(f"your car model is => {employee.car}")
        print(f"your salary (from 1000 to more) is => {employee.salary} LE")
        print(f"the distance to work is => {employee.distance_to_work} Km")
        print(f"your Velocity (from drive method) is => {employee.drive(5, employee.distance_to_work)} Km/s")
        print(f"your mood (from work method) is => {employee.mood}")


employee = employee(5, "fait", "abdoraddad@gmail.com", 500, 20)
employee.work(8)
employee.refuel(50)

print((" " * 40) + "FROM EMPLOYEE CLASS")
print((" " * 25) + ("*" * 50))
employee.display()
print(employee.send_mail(employee.email, "mohammed@gmail.com", "This is an email template", "Mohammed"))
