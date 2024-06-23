class person:
    def __init__(self, name, yob):
        self._name = name

        if not isinstance(yob, int):
            print("Year of birth must be an integer")
            return
        self._yob = yob
    # abstract method

    def describe(self):
        pass


class student(person):
    def __init__(self, name, yob, grade):
        person.__init__(self, name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name : {self._name} - YoB : {self._yob} - Grade : {self._grade}")


class teacher(person):
    def __init__(self, name, yob, subject):
        person.__init__(self, name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name : {self._name} - YoB : {self._yob} - Subject : {self._subject}")


class doctor(person):
    def __init__(self, name, yob, specialist):
        person.__init__(self, name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name : {self._name} - YoB : {self._yob} - Specialist : {self._specialist}")


class ward:
    def __init__(self, name, capacity=10000):
        if not isinstance(capacity, int):
            print("Capacity must be an integer")
            return
        self._name = name
        self._capacity = capacity
        self._people = []

    def describe(self):
        print(f"Ward Name : {self._name}")
        for person in self._people:
            person.describe()

    def add_person(self, person):
        if (len(self._people) < self._capacity):
            self._people.append(person)
        else:
            print("Ward is full")

    def count_doctor(self):
        count = 0
        for person in self._people:
            if isinstance(person, doctor):
                count += 1
        return count

    def sort_age(self):
        self._people.sort(key=lambda x: x._yob, reverse=True)

    def compute_average(self):
        total, count = 0, 0
        for person in self._people:
            if isinstance(person, teacher):
                total += person._yob
                count += 1
        return total / count


if __name__ == "__main__":
    student1 = student(name=" studentA ", yob=2010, grade="7")
    teacher1 = teacher(name=" teacherA ", yob=1969, subject=" Math ")
    doctor1 = doctor(name=" doctorA ", yob=1945,
                     specialist=" Endocrinologists ")
    teacher2 = teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor2 = doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")

    ward1 = ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    print(f"\nNumber of doctors : {ward1.count_doctor()}")
    print("\nAfter sorting Age of Ward1 people ")
    ward1.sort_age()
    ward1.describe()
    print(f"\nAverage year of birth ( teachers ): {ward1.compute_average()}")
