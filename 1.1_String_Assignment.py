# Python program to capitalize the first and last character of each word in a string (input string should be a statement)



# Sample Input :

# Python is a high level programming language



# Sample Output :

# PythoN IS A HigH LeveL ProgramminG LanguagE


ch="Python is a high level programming language"
j=0
str=list(ch)
str+='\0'
for i in range(len(str)):
    if i==0 or str[i-1]==' ':
        str[i]=str[i].upper()
    elif str[i]==' ' or str[i]=='\0':
        str[i-1] = str[i-1].upper()

print("Your Output String is:", "".join(str))
