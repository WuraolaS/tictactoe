list1=[['1','2','3'],
['4','5','6'],
['7','8','9']]

#The program collects the input of the user
#refracting = editing
#use variable
#create function
#use a counter
#a while with a counter of 9
#the odd numbers are
#determine whos turn using modulo
#have main function that calls all the other codes
#function that determine who win
test=input("firstmove\n")
#first move - make this into a function
if test == '1':
    print("it worked")
    list1[0][0]='x'
    print(list1)
elif test == '2':
    list1[0][1]='x'
    print(list1)
elif test == '3':
    list1[0][2]='x'
    print(list1)
elif test == '4':
    list1[1][0]='x'
    print(list1)
elif test == '5':
    list1[1][1]='x'
    print(list1)
elif test == '6':
    list1[1][2]='x'
    print(list1)
elif test == '7':
    list1[2][0]='x'
    print(list1)
elif test == '8':
    list1[2][1]='x'
    print(list1)
elif test == '8':
    list1[2][2]='x'
    print(list1)

else:
    print('please pick a number from 1-4')

#second move validates the users 2nd move
test2=input("2ndmove\n")
if test2 == '1' and list1[0][0] != 'x' and list1[0][0] != 'o':
    list1[0][0]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '2' and list1[0][1] != 'x' and list1[0][1] != 'o':
    list1[0][1]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '3' and list1[0][2] != 'x' and list1[0][2] != 'o':
    list1[0][2]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '4' and list1[1][0] != 'x' and list1[1][0] != 'o':
    list1[1][0]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '5' and list1[1][1] != 'x' and list1[1][1] != 'o':
    list1[1][1]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '6' and list1[1][2] != 'x' and list1[1][2] != 'o':
    list1[1][2]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '7' and list1[2][0] != 'x' and list1[2][0] != 'o':
    list1[2][0]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '8' and list1[2][1] != 'x' and list1[2][1] != 'o':
    list1[2][1]='o'
    print('2nd move worked')
    print (list1)
elif test2 == '9' and list1[2][2] != 'x' and list1[2][2] != 'o':
    list1[2][2]='o'
    print('2nd move worked')
    print (list1)
else:
    print("somethings there fool")

test3=input("3rdmove\n")
if test3 == '1' and list1[0][0] != 'x' and list1[0][0] != 'o':
    list1[0][0]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '2' and list1[0][1] != 'x' and list1[0][1] != 'o':
    list1[0][1]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '3' and list1[0][2] != 'x' and list1[0][2] != 'o':
    list1[0][2]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '4' and list1[1][0] != 'x' and list1[1][0] != 'o':
    list1[1][0]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '5' and list1[1][1] != 'x' and list1[1][1] != 'o':
    list1[1][1]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '6' and list1[1][2] != 'x' and list1[1][2] != 'o':
    list1[1][2]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '7' and list1[2][0] != 'x' and list1[2][0] != 'o':
    list1[2][0]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '8' and list1[2][1] != 'x' and list1[2][1] != 'o':
    list1[2][1]='x'
    print('2nd move worked')
    print (list1)
elif test3 == '9' and list1[2][2] != 'x' and list1[2][2] != 'o':
    list1[2][2]='x'
    print('2nd move worked')
    print (list1)
else:
    print("somethings there fool")

test4=input("4thmove\n")
if test4 == '1' and list1[0][0] != 'x' and list1[0][0] != 'o':
    list1[0][0]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '2' and list1[0][1] != 'x' and list1[0][1] != 'o':
    list1[0][1]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '3' and list1[0][2] != 'x' and list1[0][2] != 'o':
    list1[0][2]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '4' and list1[1][0] != 'x' and list1[1][0] != 'o':
    list1[1][0]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '5' and list1[1][1] != 'x' and list1[1][1] != 'o':
    list1[1][1]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '6' and list1[1][2] != 'x' and list1[1][2] != 'o':
    list1[1][2]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '7' and list1[2][0] != 'x' and list1[2][0] != 'o':
    list1[2][0]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '8' and list1[2][1] != 'x' and list1[2][1] != 'o':
    list1[2][1]='o'
    print('2nd move worked')
    print (list1)
elif test4 == '9' and list1[2][2] != 'x' and list1[2][2] != 'o':
    list1[2][2]='o'
    print('2nd move worked')
    print (list1)
else:
    print("somethings there fool")

test5=input("5thmove\n")
if test5 == '1' and list1[0][0] != 'x' and list1[0][0] != 'o':
    list1[0][0]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '2' and list1[0][1] != 'x' and list1[0][1] != 'o':
    list1[0][1]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '3' and list1[0][2] != 'x' and list1[0][2] != 'o':
    list1[0][2]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '4' and list1[1][0] != 'x' and list1[1][0] != 'o':
    list1[1][0]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '5' and list1[1][1] != 'x' and list1[1][1] != 'o':
    list1[1][1]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '6' and list1[1][2] != 'x' and list1[1][2] != 'o':
    list1[1][2]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '7' and list1[2][0] != 'x' and list1[2][0] != 'o':
    list1[2][0]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '8' and list1[2][1] != 'x' and list1[2][1] != 'o':
    list1[2][1]='x'
    print('2nd move worked')
    print (list1)
elif test5 == '9' and list1[2][2] != 'x' and list1[2][2] != 'o':
    list1[2][2]='x'
    print('2nd move worked')
    print (list1)
else:
    print("somethings there fool")

#Test for a horizontal win
if list1[0][0] == list1[0][1] and list1[0][2] == list1[0][0]:
    print(f"{list1[0][0]} won game over")
elif list1[1][0] == list1[1][1] and list1[1][2] == list1[1][0]:
    print (f"{list1[1][0]} won game over")

elif list1[2][0] == list1[2][1] and list1[2][2] == list1[2][0]:
    print (f"{list1[2][0]} won game over")
else:
    test6=input("6thmove\n")
    if test6 == '1' and list1[0][0] != 'x' and list1[0][0] != 'o':
        list1[0][0]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '2' and list1[0][1] != 'x' and list1[0][1] != 'o':
        list1[0][1]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '3' and list1[0][2] != 'x' and list1[0][2] != 'o':
        list1[0][2]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '4' and list1[1][0] != 'x' and list1[1][0] != 'o':
        list1[1][0]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '5' and list1[1][1] != 'x' and list1[1][1] != 'o':
        list1[1][1]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '6' and list1[1][2] != 'x' and list1[1][2] != 'o':
        list1[1][2]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '7' and list1[2][0] != 'x' and list1[2][0] != 'o':
        list1[2][0]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '8' and list1[2][1] != 'x' and list1[2][1] != 'o':
        list1[2][1]='o'
        print('2nd move worked')
        print (list1)
    elif test6 == '9' and list1[2][2] != 'x' and list1[2][2] != 'o':
        list1[2][2]='o'
        print('2nd move worked')
        print (list1)

    test7=input("6thmove\n")
    if test6 == '1' and list1[0][0] != 'x' and list1[0][0] != 'o':
        list1[0][0]='o'
        print (list1)
    elif test6 == '2' and list1[0][1] != 'x' and list1[0][1] != 'o':
        list1[0][1]='o'
        print (list1)
    elif test6 == '3' and list1[0][2] != 'x' and list1[0][2] != 'o':
        list1[0][2]='o'
        print (list1)
    elif test6 == '4' and list1[1][0] != 'x' and list1[1][0] != 'o':
        list1[1][0]='o'
        print (list1)
    elif test6 == '5' and list1[1][1] != 'x' and list1[1][1] != 'o':
        list1[1][1]='o'
        print (list1)
    elif test6 == '6' and list1[1][2] != 'x' and list1[1][2] != 'o':
        list1[1][2]='o'
        print (list1)
    elif test6 == '7' and list1[2][0] != 'x' and list1[2][0] != 'o':
        list1[2][0]='o'
        print (list1)
    elif test6 == '8' and list1[2][1] != 'x' and list1[2][1] != 'o':
        list1[2][1]='o'
        print (list1)
    elif test6 == '9' and list1[2][2] != 'x' and list1[2][2] != 'o':
        list1[2][2]='o'
        print (list1)
    else:
        print("somethings there fool")
