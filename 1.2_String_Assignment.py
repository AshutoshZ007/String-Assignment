# Python program to count the number of vowels in a given string.



# Sample Input :

# Python is a high level programming language



# Sample Output :

# Vowels :13


string="Python is a high level programming language"
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)