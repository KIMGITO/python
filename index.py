print('hello world')
name = input('what is your name?')
#python strings

print("hello "+ name)#string methods....
try:
    amount = float(input('How much money do you  have? '))
    currency = input('select k for kesh and $ for usd')
    if(currency == 'K' or currency =='k'):
        amount =amount// 135
        print("You have "+ str(amount) + " $(USD)")
    elif(currency == '$'):
        amount *=135
        print("You have "+ str(amount) + " Kesh")
    else:
        print("Wrong currency convertion")
except ValueError as e:
    print("Error", str(e))



