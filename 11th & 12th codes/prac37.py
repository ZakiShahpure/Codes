import random
import string
password_length = 8
password_combination = string.ascii_letters + string.digits
random_password = ''.join(random.choices(password_combination, k=password_length))
print(random_password)