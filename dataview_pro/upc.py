from hashlib import md5

username = "test"
pswd = "123"

my_pwd = md5(pswd.encode()).hexdigest()

print(f"insert into user_login_userinfo (uname, upwd) value('{username}', '{my_pwd}');")