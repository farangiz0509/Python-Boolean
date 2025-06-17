secret_password = "000"
getting_password = input("enter password")
result = len(getting_password) == 0 or getting_password != secret_password
print(result)