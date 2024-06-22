class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.access = 'default'
    
    def change_username(self, new_username):
        self.username = new_username
    
    def change_role(self, new_role):
        if self.role == 'admin':
            self.role = new_role
        print("You don't have the necessary privileges...")
    
    def get_access(self):
        return self.access

class Admin(User):
    def __init__(self, username, privileges):
        super().__init__(self, username, role='admin')
        self.privileges = privileges
    
    def show_privileges(self):
        print("Privileges:\n")
        for privilege in self.privileges:
            print(f"\t{privilege}\n")
        