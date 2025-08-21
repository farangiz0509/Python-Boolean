from getpass import getpass
secret_password = "0444yu"
getting_password = getpass("enter password")
result = len(getting_password) == 0 or getting_password != secret_password
print(result)