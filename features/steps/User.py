class User:
    def __init__(self, username, password):
        if username == "None":
          username = None

        if password == "None":
           password = None

        self.username = username
        self.password = password
