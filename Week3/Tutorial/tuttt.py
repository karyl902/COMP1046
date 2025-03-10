class HospitalEmployee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def work(self):
        return self.name + " is working as a " + self.role + "."


class HospitalDepartment:
    def __init__(self, name, allowed_roles):
        self.name = name
        self.allowed_roles = allowed_roles

    def grant_access(self, role):
        if role in self.allowed_roles:
            return "Access granted to " + role + " in " + self.name + "."
        return "Access denied to " + role + " in " + self.name + "."



admin = HospitalEmployee("Alice", "Administrator")
nurse = HospitalEmployee("Bob", "Nurse")
surgeon = HospitalEmployee("Charlie", "Surgeon")


surgery = HospitalDepartment("Surgery", ["Surgeon", "Nurse"])
storage = HospitalDepartment("Storage", ["Administrator", "Cleaner"])


print(surgery.grant_access(nurse.role))  
print(storage.grant_access(surgeon.role))  
