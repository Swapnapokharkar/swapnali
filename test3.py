#1. check if the number is prime or not)
def prime():
	Num = int(input(" Please Enter any Num: "))
	count = 0
	i = 2

	while(i <= Num//2):
		if(Num % i == 0):
			count = count + 1
			break
		i = i + 1

	if (count == 0 and Num != 1):
		print(" %d is a Prime" %Num)
	else:
		print(" %d is not a Prime" %Num)

#2. Calculate Factorial of given number
def factorial():
	num = int(input("\nEnter a number: "))
	factorial = 1
	if num < 0:
		print("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
		print("The factorial of 0 is 1")
	else:
		for i in range(1,num + 1):
			factorial = factorial*i
		print("The factorial of",num,"is",factorial)

#3. check given number is palindrome or not)
def palindrome():
	n=int(input("\nEnter number:"))
	temp=n
	rev=0
	while(n>0):
	     dig=n%10
	     rev=rev*10+dig
	     n=n//10
	if(temp==rev):
	    print("The number is a palindrome!")
	else:
	    print("The number isn't a palindrome!")

#4. check given number is Armstrong or not)
def armstrong():
	num = int(input("\nEnter Number="))
	sum = 0
	temp = num
	while temp>0:
		digit = temp%10
		sum += digit ** 3
		temp//=10
	if num == sum:
		print(num,"is an Armstrong Number")
	else:
		print(num,"is not an Armstrong Number")

#5.Exit Program
def ex():
	exit(0)

def default():
    print("Wrong Choice Try again!")
a=0
while a==0:
	ch=int(input("Enter Choice: "))
	if ch==1:
	    prime()
	elif ch==2:
		factorial()
	elif ch==3:
		palindrome()
	elif ch==4:
		armstrong()
	elif ch==5:
		ex()
	else:
		default()