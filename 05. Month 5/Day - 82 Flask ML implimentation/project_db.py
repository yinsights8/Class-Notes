def get_login_details(user_id,password):

    if user_id == 'anawle@gmail.com' and password == '123456':
        print('User id and Password is in DB')

        return "Login Successful"

    else:
        return "User id and Password is Incorrect"