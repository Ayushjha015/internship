import random as rand
#random function is imported as rand
#email id genrator
domain = str(input("enter the domain of you choise from(gmail,hotmail and email)"))
#domain selection 
#example mail id xyz123@gmail.com
list = range(97,123)
#list contains AACII values for small alphabets 
part1 = ''
#part 1 of email is declared as a string using '' quots
for i in range(0,3):
    char = chr(rand.choice(list))
    part1+=char
#for loop is genrated to pick a ASCII valur randomly from the list and chr()
#function is used to convert it to small alphabets
list2 = ["0","1","2","3","4","5","6","7","8","9"]
#list2 is made to genrate second part of email ie. numeral part
part2 = ''
#same as part1 part2 is defined
for i in range(0,3):
    num = rand.choice(list2)
    part2 +=num
#this for loop picks randomly a number from the list 2 and concat it to part 2
email  =   part1+part2+"@"+domain+".com"
#full lenght email is made by concating part1 , part2 , '@' , domain & .com
print(email)