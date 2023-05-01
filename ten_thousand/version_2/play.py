from game_logic import GameLogic

game=GameLogic()
def play():
    unbank=0
    bank=0
    counter=1
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
    input_1=input("> ")
    while True:
        if input_1=="n":
            return "OK. Maybe another time"
        elif input_1=="y":
            roll,input_2=new_round(counter)
            counter+=1
            if input_2=="q":
                return f"Thanks for playing. You earned {bank} points"
            else:
                dice_to_reroll = []
                while input_2 != "b":
                    input_2_list = list(input_2)
                    dice_to_reroll = []
                    for char in input_2_list:
                        dice_to_reroll.append(int(char))
                    if len(dice_to_reroll) > 0:
                        roll = tuple([random.randint(1, 6) if i+1 in dice_to_reroll else roll[i] for i in range(len(roll))])
                        print(f"*** {roll} ***")
                        print("Enter dice to keep, or (q)uit:")
                        input_2=input("> ")
                    else:
                        print("You must select at least one die to reroll")
                        input_2=input("> ")
                calculate=game.calculate_score(roll)
                bank+=calculate
                print(f"You banked {calculate} points in round {counter-1}\nTotal score is {bank} points")
                unbank=0
                if bank >= 10000:
                    return f"Congratulations! You won with a score of {bank} points!"
                print("Enter (y)es to play another round or (n)o to quit:")
                input_1=input("> ")
                if input_1 == "n":
                    return f"Thanks for playing. You earned {bank} points"


def new_round(counter):
    print(f"Starting round {counter}\nRolling 6 dice...")
    roll_instance=game.roll_dice(6)
    print(f"*** {roll_instance} ***")
    print("Enter dice to keep, or (q)uit:")
    input_2=input("> ")
    return roll_instance,input_2


def calc():
    pass


ahmad=play()
print(ahmad)