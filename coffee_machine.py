machine_enabled = True
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def remaining():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money')


def fill():
    global water, milk, beans, cups, money
    print('Write how many ml of water do you want to add:')
    water += int(input())
    print('Write how many ml of milk do you want to add:')
    milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    beans += int(input())
    print('Write how many cups do you want to add:')
    cups += int(input())


def take():
    global money
    print('I gave you $' + str(money))
    money -= money


def exit():
    global machine_enabled
    machine_enabled = False


def espresso():
    global water, milk, beans, cups, money
    if water >= 250 and beans >= 16 and cups >= 1:
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
        print('I have enough resources, making you a coffee!')
    elif water < 250:
        print('Sorry, not enough water!')
    elif beans < 16:
        print('Sorry, not enough coffee beans!')
    elif cups < 1:
        print('Sorry, not enough cups!')


def latte():
    global water, milk, beans, cups, money
    if water >= 350 and beans >= 20 and cups >= 1 and milk >= 75:
        water -= 350
        beans -= 20
        cups -= 1
        milk -= 75
        money += 7
        print('I have enough resources, making you a coffee!')
    elif water < 350:
        print('Sorry, not enough water!')
    elif beans < 20:
        print('Sorry, not enough coffee beans!')
    elif cups < 1:
        print('Sorry, not enough cups!')
    elif milk < 75:
        print('Sorry, not enough milk!')


def cappuccino():
    global water, milk, beans, cups, money
    if water >= 200 and beans >= 12 and cups >= 1 and milk >= 100:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
        print('I have enough resources, making you a coffee!')
    elif water < 200:
        print('Sorry, not enough water!')
    elif beans < 12:
        print('Sorry, not enough coffee beans!')
    elif cups < 1:
        print('Sorry, not enough cups!')
    elif milk < 100:
        print('Sorry, not enough milk!')


def buy_what():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    buy_this = input()
    if buy_this == '1':
        espresso()
    elif buy_this == '2':
        latte()
    elif buy_this == '3':
        cappuccino()
    elif buy_this == 'back':
        main_menu()


def main_menu():
    print('Write action (buy, fill, take, remaining, exit):')
    command = input()
    if command == 'buy':
        buy_what()
    elif command == 'fill':
        fill()
    elif command == 'take':
        take()
    elif command == 'remaining':
        remaining()
    elif command == 'exit':
        exit()


while machine_enabled:
    main_menu()
