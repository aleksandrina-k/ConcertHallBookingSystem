class User:

    def __init__(self, username: str, password: str, email: str, age: int):
        self.__id = None
        self.__username = username
        self.__password = password
        self.__email = email
        self.__age = age

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age
