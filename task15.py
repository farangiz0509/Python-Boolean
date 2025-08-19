from getpass import getpass

password = getpass("pasword:")
usage = getpass("usage_password:")
result = password == usage
print(result)
