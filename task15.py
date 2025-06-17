from getpass import getpass

password = getpass("password:")
usage = getpass("usage_password:")
result = password == usage
print(result)
