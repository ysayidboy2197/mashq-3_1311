class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = None  
        self.set_password(password)

    def set_password(self, new_password):
        if len(new_password) < 8:
            print("❌ Parol kamida 8 ta belgidan iborat bo‘lishi kerak!")
        else:
            self.__password = new_password
            print(f"✅ {self.username} uchun parol o‘rnatildi.")

    
    def _check_password(self, password):
        return password == self.__password


class AuthenticationSystem:
    def __init__(self):
        self.accounts = {}

    def register_user(self, username, password):
        if username in self.accounts:
            print("❌ Bu foydalanuvchi allaqachon ro‘yxatdan o‘tgan!")
        else:
            account = UserAccount(username, password)
            self.accounts[username] = account

    def login(self, username, password):
        if username not in self.accounts:
            print("⚠️ Foydalanuvchi topilmadi.")
        else:
            account = self.accounts[username]
            if account._check_password(password):
                print(f"✅ Xush kelibsiz, {username}!")
            else:
                print("❌ Parol noto‘g‘ri.")

    def change_password(self, username, old_password, new_password):
        if username not in self.accounts:
            print("⚠️ Foydalanuvchi topilmadi.")
        else:
            account = self.accounts[username]
            if account._check_password(old_password):
                account.set_password(new_password)
            else:
                print("❌ Eski parol noto‘g‘ri.")



auth = AuthenticationSystem()

print("\n>>> Ro‘yxatdan o‘tish:")
auth.register_user("ali", "12345")         
auth.register_user("ali", "ali12345")     
auth.register_user("vali", "vali12345")   

print("\n>>> Tizimga kirish:")
auth.login("ali", "ali12345")             
auth.login("ali", "noto‘g‘ri")            
auth.login("salim", "test1234")            

print("\n>>> Parolni o‘zgartirish:")
auth.change_password("ali", "ali12345", "yangiParol1") 
auth.change_password("ali", "xato", "yangi1234")       
auth.login("ali", "yangiParol1")                  
