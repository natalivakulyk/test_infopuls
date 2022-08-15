from datetime import datetime


class User:
    def __init__(self, username="", password="", real_name="", email="", gender=None, birthday=None, is_admin=False):
        self.username = username
        self.password = password
        self.real_name = real_name
        self.email = email
        self.gender = gender
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S") if birthday is not None else None
        self.is_admin = is_admin

    def __str__(self):
        return f"User object: username={self.username}, real_name={self.real_name}"

    def __repr__(self):
        return f"User(username={self.username}, password={self.password}, real_name={repr(self.real_name)})"


if __name__ == '__main__':
    u = User(username="admin", real_name="Vasya")
    print(str(u))
    print(repr(u))
