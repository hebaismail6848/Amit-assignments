from calc import add, sub, multi, div

con = 'yes'
while con == 'yes':
    op, n1, n2 = input("\nplease enter the operation from ['add', 'subtract','multiply'\
,'divide'] and two numbers seperate by commas\n").split(',')
    if op.lower() == 'add':
        print(add(int(n1),int(n2)))
    elif op.lower() == 'subtract':
        print(sub(int(n1),int(n2)))
    elif op.lower() == 'multiply':
        print(multi(int(n1),int(n2)))
    elif op.lower() == 'divide':
        try:
            print(div(int(n1),int(n2)))
        except:
            print('can\'t divide by zero' )
    else:
        print('Wrong choice. please try again')
    con = input('would you like to make another operation ?\n')