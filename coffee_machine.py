# Write your code here


class Machine:
    state = "idle"

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cup_num = 9
        self.money = 550
        self.choice = ""

    def do(self, string):
        if self.state == "choosing an action":
            if string == "buy":
                self.state = "choosing a variant of coffee"
                self.do(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "))
            elif string == "fill":
                self.water += int(input("Write how many ml of water do you want to add: "))
                self.milk += int(input("Write how many ml of milk do you want to add: "))
                self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
                self.cup_num += int(input("Write how many disposable cups of coffee do you want to add: "))
            elif string == "take":
                print("I gave you $" + str(self.money))
                self.money = 0
            elif string == "remaining":
                print("The coffee machine has:")
                print(str(self.water) + " of water")
                print(str(self.milk) + " of milk")
                print(str(self.beans) + " of beans")
                print(str(self.cup_num) + " of disposable cups")
                print("$" + str(self.money) + " of money")
            elif string == "exit":
                self.state = "exiting"
        elif self.state == "choosing a variant of coffee":
            if string == "1":  # espresso
                if self.water >= 250 and self.beans >= 16:
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                    self.cup_num -= 1
                    print("I have enough resources, making you a coffee!")
                else:
                    if self.water < 250:
                        print("Sorry, not enough water!")
                    if self.beans < 16:
                        print("Sorry, not enough coffee beans!")
            elif string == "2":  # latte
                if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                    self.cup_num -= 1
                    print("I have enough resources, making you a coffee!")
                else:
                    if self.water < 350:
                        print("Sorry, not enough water!")
                    if self.milk < 75:
                        print("Sorry, not enough milk!")
                    if self.beans < 20:
                        print("Sorry, not enough coffee beans!")
            elif string == "3":  # cappuccino
                if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                    self.cup_num -= 1
                    print("I have enough resources, making you a coffee!")
                else:
                    if self.water < 200:
                        print("Sorry, not enough water!")
                    if self.milk < 100:
                        print("Sorry, not enough milk!")
                    if self.beans < 12:
                        print("Sorry, not enough coffee beans!")
            elif string == "back":  # back to choosing
                my_machine.do(input("Write action (buy, fill, take, remaining, exit): "))
                my_machine.state = "choosing an action"
        return self.state


my_machine = Machine()
while True:
    if my_machine.state == "exiting":
        break
    my_machine.state = "choosing an action"
    my_machine.do(input("Write action (buy, fill, take, remaining, exit): "))
