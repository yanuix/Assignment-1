#Exercise 3-Biography

name= input ("Enter Full Name:")
hometown = input ("Enter Hometown:")

while True:
    age = input ("Enter Age:")
    if age. isdigit():
        age= int(age)
        break
    else :
        print("Wrong Age. Enter Age in number")

dict = {'Name' : name, 'Hometown' : hometown, 'Age' : age}
print(dict)