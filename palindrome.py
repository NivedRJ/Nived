str1 = input("Enter a string:")
 
for i in range(0,int(len(str1)/2)):
    if str1[i] != str1[len(str)-i-1]:
        print("Palindrome")
    else:
        print("not palindrome")