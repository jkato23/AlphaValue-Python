print("Hello")
statement = input("Enter a statement to convert: ")
statementArray = []
for i in statement:
    if i.isalpha() == True:
        statementArray.append(ord(i) - 96)
    else: 
        statementArray.append(i)
for i in statementArray:
    print(i, end=" ")