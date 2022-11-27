import Sajat_modul


if __name__ == "__main__":
    print("Az első játékos a gép! \nTe pedig a második játékos!")
    print(
        "A játék szabályai:\n1. A nehézségi szint alapján lesz egy megadott számú próbálkozásod, hogy eltaláld a kitalált többszámjegyű számot!")
    print("2. Ha nem adsz meg elég számot, akkor számodra végetért a játék")
    print("\nSok sikert! Remélem minél előbb eltalálod a számot!!:)")
    difficulty_level = int(
        input("Add meg a játék néhezségi fokozatát: 1/2/3 Könnyű/Közepes/Nehéz fokok közül kell választanod: "))
    game = Sajat_modul.MasterMind(difficulty_level)
    game.random_digit_generator(game.digits)
    game.player2_turn(game.digits, game.random_digit_generator(game.digits), game.attempts)