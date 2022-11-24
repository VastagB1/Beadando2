import random

class MasterMind():
    """
    Osztály, mely kezeli a Kitalálós játék példányát.

    """

    def __init__(self, level: int):
        """
        Constructor for setting up the difficulty level, number of digits and iterations of the game
        Nehezségi szintet, számok mennyiségét és a játék ismetlését felállító konstruktor
        """
        self.level = level
        if level == 1:
            print("Ezen a szinten egy kétszámjegyű számot kell kitalálj!")
            self.digits = 2
            self.attempts = 4
        elif level == 2:
            print("Ezen a szinten egy háromszámjegyű számot kell kitalálj!")
            self.digits = 3
            self.attempts = 6
        elif level == 3:
            print("Ezen a szinten egy négyszámjegyű számot kell kitalálj!")
            self.digits = 4
            self.attempts = 10
        else:
            print("Helytelen bemeneti adat! Kérlek a felsoroltak közül válassz:[1,2,3]")
            quit()

    def checker(self, guess: int, digits: int):
        """
        checks if the guess of Player 2 matches the length of the set value
        Itt nézzük meg, hogy a második játékos(te) által beírt szám hossza megfelelő e
        """

        if len(str(guess)) != digits:
            print("You havent entered desired number of digits, hence you are disqualified from the game"
                  "Nem megfelelő mennyiségű számot adtál meg, ezért számodra végetért a játék")
            quit()

    @staticmethod
    def random_digit_generator(digits: int) -> int:
        """
        Generates a random multi digit number from the Player 1's side
        Generál egy random többszámjegyű számot az első játékosnak(gép)
        """
        try:
            lower_limit = int("1" + "0" * (digits - 1))
            upper_limit = int("9" * (digits))
            randomly_generated_value = random.randrange(lower_limit, upper_limit)
            return randomly_generated_value
        except Exception as e:
            print(e)

    def player2_turn(self, digits: int, set_value: int, attempts: int):
        """
        Attempts of the Player 2
        Itt kezdődik a második játékos(te) próbálkozásai
        """
        print("Enter a number"
              "Adjon meg egy számot")
        guess = int(input(": "))
        self.checker(guess, digits)

        if guess == set_value:
            print("You are a mastermind! Guessed the number in the very first attempt!"
                  "Egy zseni vagy! Első próbálkozásra eltaláltad a számot!")
            quit()

        else:
            ctr = 1
            while ctr != attempts:
                guess = str(guess)
                set_value = str(set_value)
                count = 0
                output = ["X"] * digits

                for i in range(digits):
                    if guess[i] == set_value[i]:
                        output[i] = guess[i]
                        count += 1

                if count != 0 and count < digits:
                    print(f"Not quite the number! You did get {count} digit(s) right"
                          f"Csak részlegesen találtad el a számot! {count} szám(ot) találtál el")
                    print(output)
                    print("\nEnter your next choice of numbers:"
                          "\nÍrd be a következő próbálkozásod:")
                    guess = int(input(": "))
                    self.checker(guess, digits)

                elif count == 0:
                    print("None of the numbers in your input match"
                          "Egyetlen számot sem találtál el")
                    print("\nEnter your next choice of numbers:"
                          "\nÍrd be a következő próbálkozásod:")
                    guess = int(input(": "))
                    self.checker(guess, digits)

                elif count == digits:
                    print("You've become a mastermind!"
                          "Nagyon ügyes vagy!! Eltaláltad a számot")
                    print(f"You guessed the number in {ctr} attempts"
                          f"{ctr} próbálkozás alatt eltaláltad a számot!")
                    quit()
                ctr += 1
            print("Game Over!")
            print(f"A szám a {set_value} volt")
