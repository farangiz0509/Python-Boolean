correct_pin = "1234"
pin = input("PIN kodni kiriting: ")

tekshirish  = pin != correct_pin or len(pin) != 4

print(tekshirish)