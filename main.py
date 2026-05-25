class User:
    def __init__(self,login):
        self.login = login #public
        self._email = "login@mail.ru"
        self.__password = "qwert2026"
        
    def set_password(self, oldpasswrod, newpassword):
        if oldpasswrod == self.__password:
            self.__password = newpassword
            print("Пароль успешно изменен")
        else:
            print("Уйди!")
            
    def get_password(self):
        print(self.__password)
    
        
user = User("Alex2026")
user.set_password("qwert2026", "onetime2026")
user.get_password()

print()


