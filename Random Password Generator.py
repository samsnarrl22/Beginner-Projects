


from random import randint
# password = ""
# for i in range(10):
 #   i = chr(randint(65, 90))
  #  password = str(password + i)
# print("Your random password is: ", password)

# Alternating Upper and Lower case Password
password = ""
print("How long is your password?")
x = int(int(input())/2)
for i in range(x):
    i = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print("Your random password is: ", password)