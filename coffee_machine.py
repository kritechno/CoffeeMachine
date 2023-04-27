class CoffeeMachine:

    def __init__(self):
        self.storage = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

    def main(self):
        while True:
            action = str(input("\nWrite action (buy, fill, take, remaining, exit):\n")).lower()
            if action == "exit":
                break
            else:
                self.do_action(action)

    def do_action(self, action):
        if action == "remaining":
            self.status()
        elif action == "buy":
            self.buy_coffee()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()

    def status(self):
        print('The coffee machine has:')
        for item, amount in self.storage.items():
            print(f"${amount} of {item}" if item == 'money' else f"{amount} of {item}")

    def buy_coffee(self):
        coffee_choices = {
            '1': {'water': 250, 'beans': 16, 'cups': 1, 'money': -4},
            '2': {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'money': -7},
            '3': {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'money': -6},
        }
        choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "back":
            return
        else:
            for item, amount in coffee_choices[choice].items():
                if self.storage[item] - amount < 0:
                    print(f'Sorry, not enough {item}!')
                    return

            print('I have enough resources, making you a coffee!')
            for item, amount in coffee_choices[choice].items():
                self.storage[item] -= amount

    def fill(self):
        self.storage['water'] += int(input("Write how many ml of water you want to add:\n"))
        self.storage['milk'] += int(input("Write how many ml of milk you want to add:\n"))
        self.storage['beans'] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.storage['cups'] += int(input("Write how many disposable cups you want to add:\n"))

    def take(self):
        print(f"\nI give you ${self.storage['money']}")
        self.storage['money'] = 0


if __name__ == '__main__':
    CoffeeMachine().main()

