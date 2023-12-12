class Person:
    def __init__(self, person_id, name, phone_num):
        self.id = person_id
        self.name = name
        self.phone_num = phone_num

    def printinfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Phone Number: {self.phone_num}")


class Employee(Person):
    def __init__(self, person_id, name, phone_num, title):
        super().__init__(person_id, name, phone_num)
        self.title = title

    def printinfo(self):
        super().printinfo()
        print(f"Title: {self.title}")


class Alba(Person):
    pass


class Manager(Person):
    def __init__(self, person_id, name, phone_num, skill):
        super().__init__(person_id, name, phone_num)
        self.skill = skill

    def printinfo(self):
        super().printinfo()
        print(f"Skill: {self.skill}")


# 샘플 코드
people_list = [
    Employee("E001", "John Doe", "123-456-7890", "Software Engineer"),
    Manager("M001", "Jane Smith", "987-654-3210", "Project Management"),
    Alba("A001", "Kim Lee", "111-222-3333"),
    Employee("E002", "Alice Johnson", "555-123-4567", "Data Analyst"),
    Manager("M002", "Bob Wilson", "333-444-5555", "Leadership"),
    Alba("A002", "Park Choi", "999-888-7777"),
    Employee("E003", "Charlie Brown", "777-888-9999", "Web Developer"),
    Manager("M003", "David Kim", "444-555-6666", "Communication"),
    Alba("A003", "Lee Han", "666-777-8888"),
    Employee("E004", "Eva Davis", "222-333-4444", "UX Designer"),
]

# 출력
for person in people_list:
    person.printinfo()
    print()
