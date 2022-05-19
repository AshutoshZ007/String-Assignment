# Program to check if a string contains any special character.



# Sample Input :

# Python is a high level programming language



# Sample Output :

# String is accepted





# Sample Input :

# Python@is a&high level*programming language



# Sample Output :

# String is not accepted






import re

def run(string):
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	
	if(regex.search(string) == None):
		print("String is accepted")
		
	else:
		print("String is not accepted.")
	
if __name__ == '__main__' :
	
	string = input("Enter String to check\n")
	# string= "Python is a high level programming language"
    #string= "Python@is a&high level*programming language"
	run(string)