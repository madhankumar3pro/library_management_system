class User:
    def __init__(self, name, user_id,mobile_num):
        self.name = name
        self.user_id = user_id
        self.mobile_num = mobile_num

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id},mobile_num:{self.mobile_num}"


# Storage for users
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id,mobile_num):
        user = User(name, user_id,mobile_num)
        self.users.append(user)

    def list_users(self):
        return self.users

    def search_users(self, keyword, by='name'):
        try:
            if by == 'name':
                return [user for user in self.users if keyword.lower() in user.name.lower()]
            elif by == 'user_id':
                return [user for user in self.users if keyword.lower() in user.user_id.lower()]
            else:
                return []
        except Exception as e:
            print('Please search valid user details')

    def update_user(self, user_id, mobile_num=None,name=None,late_fees = None):
        try:

            for user in self.users:
                if user.user_id == user_id:
                    if name:
                        user.name = name
                    if late_fees:
                        user.late_fees = late_fees
                    if mobile_num:
                        user.mobile_num = mobile_num 
                    break
        except Exception as e:
            print(' Please update valid user details')

    def delete_user(self, user_id):
        try: 
            self.users = [user for user in self.users if user.user_id != user_id]
        except Exception as e:
            print(e)

