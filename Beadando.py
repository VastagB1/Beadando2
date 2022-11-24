import Sajat_modul


if __name__ == "__main__":
    print("Player 1 is the computer!\nYou are the second player!"
          "Az első játékos a gép! \n Te pedig a második játékos!")
    print(
        "Rules of the game:\n1. The number of attempts that you will get to guess the multi-digit number will depend on the difficulty level of the game that you will opt for"
        "A játék szabályai:\n1. A nehézségi szint alapján lesz egy megadott számú próbálkozásod, hogy eltaláld a kitalált többszámjegyű számot!")
    print("2. If your guess doesnt consist of the desired number of digits then you will be disqualified from the game"
          "2. Ha nem adsz meg elég számot, akkor számodra végetért a játék")
    print("\nGood luck! Hope you turn up to be the Mastermind of the game!!"
          "\nSok sikert! Remélem minél előbb eltalálod a számot!!:)")
    difficulty_level = int(
        input("Enter the difficulty level of the game as 1/2/3 for Easy/Moderate/Hard respectively: "
              "Add meg a játék néhezségi fokozatát: 1/2/3 Könnyű/Közepes/Nehéz fokok közül kell választanod: "))
    game = Sajat_modul.MasterMind(difficulty_level)
    game.random_digit_generator(game.digits)
    game.player2_turn(game.digits, game.random_digit_generator(game.digits), game.attempts)