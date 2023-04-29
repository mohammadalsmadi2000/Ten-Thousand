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
            # print("Starting round 1\nRolling 6 dice...")
            # roll_instance=game.roll_dice(6)
            # print(f"*** {roll_instance} ***")
            roll,input_2=new_round(counter)
            counter+=1
            # print("Enter dice to keep, or (q)uit:")
            # input_2=input("> ")
            if input_2=="q":
                return f"Thanks for playing. You earned {bank} points"
            else:
                input_22= int(input_2)
                roll_instance_1=list(roll) 
                empty = []
                    
                while input_22 > 0:
                    input_22, remd = divmod(input_22, 10)
                    empty.append(remd)
                integer_tuple=tuple(empty)
                    
                my_result = set(integer_tuple).issubset(roll_instance_1)
                if my_result==False:
                    return "cheating"
                else:
                    calculate=game.calculate_score(integer_tuple)
                    length_myresult=len(integer_tuple)
                    length_full_array=len(roll_instance_1)
                    result_length=length_full_array-length_myresult
                    for i in integer_tuple[:]:
                        if i in roll_instance_1:
                            roll_instance_1.remove(i)
                            empty.remove(i)
                    # unbank+=calculate
                    # print(type(unbank))
                    print(f"You have {calculate} unbanked points and {result_length} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    input_3=input("> ")
                    bank+=int(calculate)
                    if input_3=="b":
                        # print(type(bank))
                        # print(type(calculate))
                        # bank+=int(calculate)
                        # print(type(bank))
                        # print(type(unbank))
                        print(f"You banked {calculate} points in round 1\nTotal score is {bank} points")
                        unbank=0
                    elif input_3=='q':
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