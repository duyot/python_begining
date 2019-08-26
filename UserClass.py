class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("Inited")

    def toString(self):
        print(self.username + self.password)


user1 = User("duyot", "123456")
user1.toString()
