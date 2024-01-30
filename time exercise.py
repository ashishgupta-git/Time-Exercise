import time

name = input("Enter Your Name: ")

Hour = int(time.strftime("%H"))
Min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

print("TIME: ",Hour,":",Min,":",sec)

if (Hour < 12):
    print("Good Morning",name,"Sir")

elif (Hour > 12 and Hour < 17):
    print("Good evening",name,"Sir")

else:
    print("Good night",name,"Sir")