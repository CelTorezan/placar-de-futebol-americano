# Define uma classe para o placar de futebol americano
class FootballScoreboard:
    def __init__(self):
        self.team1_score = 0
        self.team2_score = 0

    def touchdown(self, team):
        if team == 1:
            self.team1_score += 6
        else:
            self.team2_score += 6
        self.print_score()

    def extra_point(self, team):
        if team == 1:
            self.team1_score += 1
        else:
            self.team2_score += 1
        self.print_score()

    def two_point_conversion(self, team):
        if team == 1:
            self.team1_score += 2
        else:
            self.team2_score += 2
        self.print_score()

    def field_goal(self, team):
        if team == 1:
            self.team1_score += 3
        else:
            self.team2_score += 3
        self.print_score()

    def safety(self, team):
        if team == 1:
            self.team1_score += 2
        else:
            self.team2_score += 2
        self.print_score()

    def print_score(self):
        print(f"Placar - Time 1: {self.team1_score} | Time 2: {self.team2_score}")

def main():
    scoreboard = FootballScoreboard()
    print("Bem-vindo ao Placar de Futebol Americano!")
    scoreboard.print_score()

    while True:
        print("\nEscolha uma ação:")
        print("1: Touchdown Time 1")
        print("2: Touchdown Time 2")
        print("3: Extra Point Time 1")
        print("4: Extra Point Time 2")
        print("5: Two-Point Conversion Time 1")
        print("6: Two-Point Conversion Time 2")
        print("7: Field Goal Time 1")
        print("8: Field Goal Time 2")
        print("9: Safety Time 1")
        print("10: Safety Time 2")
        print("0: Sair")

        try:
            choice = int(input("Escolha uma ação (0-10): "))
            if choice == 0:
                print("Saindo...")
                break
            elif choice == 1:
                scoreboard.touchdown(1)
            elif choice == 2:
                scoreboard.touchdown(2)
            elif choice == 3:
                scoreboard.extra_point(1)
            elif choice == 4:
                scoreboard.extra_point(2)
            elif choice == 5:
                scoreboard.two_point_conversion(1)
            elif choice == 6:
                scoreboard.two_point_conversion(2)
            elif choice == 7:
                scoreboard.field_goal(1)
            elif choice == 8:
                scoreboard.field_goal(2)
            elif choice == 9:
                scoreboard.safety(1)
            elif choice == 10:
                scoreboard.safety(2)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número de 0 a 10.")

if __name__ == "__main__":
    main()
