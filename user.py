class User:
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = self.pass_hash(password)

    def pass_hash(self, __password):
        return __password + '@;dko! $'

    def verify(self, password):
        return self.__password == self.pass_hash(password)

    def get_login(self):
        return self.__login

    def set_login(self, new_log):
        if len(new_log) < 2 or len(new_log) > 20:
            raise ValueError('Неверное имя')
        self.__login = new_log



    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        if len(new_pass) < 3 or len(new_pass) > 10:
            raise ValueError('Неккоректный пароль')
        self.__password = self.pass_hash(new_pass)

#    def change_pass(self, new_pass: str):
#        self.__password = self.pass_hash(new_pass)


vasya = User('Vasya','jdiw2uh22c')
vasya.password = '1234'
print(vasya.verify('1234'))
vasya.set_login('Kolya')
print(vasya.get_login())