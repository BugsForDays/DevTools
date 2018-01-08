import random

while True:
    print('**************\nPROB SIMULATOR\n**************\n1. Coin Flip\n2. Dice Roll\nEXIT\n')
    choice = input('What is your choice?   >>>>> ')
    if choice == '1':
        randcoin = random.randrange(1 ,3, 1)
        if randcoin == 1:
            coin = 'heads'
        else:
            coin = 'tails'
        print('\nYou flipped a ' + coin + '\n')
    elif choice == '2':
        randdice = random.randrange(1,7,1)
        print('\nYou rolled a ' + str(randdice) + '\n')
    elif choice == 'exit':
        exit()
    else:
        print('\nPlease try again.\n')
        input('Press enter to continue.')
