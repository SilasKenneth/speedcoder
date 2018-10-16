from werkzeug.security import generate_password_hash

class User(object):
    def __init__(self, fullname, username, email, password):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = generate_password_hash(password)
        self.role = "attendant"

    def promote(self):
        self.role = "admin"

    def save(self):
        db.users.update({self.username: self})
        db.user_emails_index.update({self.email: self.username})