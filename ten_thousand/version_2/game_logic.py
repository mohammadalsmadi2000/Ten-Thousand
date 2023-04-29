import random


class GameLogic:
    @staticmethod
    def roll_dice(number):
        _list = []
        if number > 6:
            print("wrong number, the number should be between 1 and 6")
        else:
            for i in range(number):
                rand = random.randint(1, 6)

                _list.append(rand)
            new_tuple = tuple(_list)
        return new_tuple
    @staticmethod
    def calculate_score(_tuple):
        array_counter = {
            "one": 0,
            "two": 0,
            "three": 0,
            "four": 0,
            "five": 0,
            "six": 0

        }
        unbank_score = 0
        bank_score = 0
        pairs=0
        for i in _tuple:
            if i == 1:
                array_counter["one"] += 1
            if i == 2:
                array_counter["two"] += 1
            if i == 3:
                array_counter["three"] += 1
            if i == 4:
                array_counter["four"] += 1
            if i == 5:
                array_counter["five"] += 1
            if i == 6:
                array_counter["six"] += 1
        
        for i in array_counter:
            
            if array_counter[i]==2:
                pairs+=1
            # print(pairs)

        if _tuple == (1, 6, 3, 2, 5, 4):
            unbank_score += 2000
        elif pairs==3:
            unbank_score+=1500
        else:
            # one
            if array_counter["one"] == 1:
                unbank_score += 100
            if array_counter["one"] == 2:
                unbank_score += 200
            if array_counter["one"] == 3:
                unbank_score += 1000
            if array_counter["one"] == 4:
                unbank_score += 2000
            if array_counter["one"] == 5:
                unbank_score += 4000
            if array_counter["one"] == 6:
                unbank_score += 8000
            # two
            if array_counter["two"] == 3:
                unbank_score += 200
            if array_counter["two"] == 4:
                unbank_score += 400
            if array_counter["two"] == 5:
                unbank_score += 800
            if array_counter["two"] == 6:
                unbank_score += 1600
            # three
            if array_counter["three"] == 3:
                unbank_score += 300
            if array_counter["three"] == 4:
                unbank_score += 600
            if array_counter["three"] == 5:
                unbank_score += 1200
            if array_counter["three"] == 6:
                unbank_score += 2400
            # four
            if array_counter["four"] == 3:
                unbank_score += 400
            if array_counter["four"] == 4:
                unbank_score += 800
            if array_counter["four"] == 5:
                unbank_score += 1600
            if array_counter["four"] == 6:
                unbank_score += 3200
            # five
            if array_counter["five"] == 1:
                unbank_score += 50
            if array_counter["five"] == 2:
                unbank_score += 100
            if array_counter["five"] == 3:
                unbank_score += 500
            if array_counter["five"] == 4:
                unbank_score += 1000
            if array_counter["five"] == 5:
                unbank_score += 2000
            if array_counter["five"] == 6:
                unbank_score += 4000

            # six

            if array_counter["six"] == 3:
                unbank_score += 600
            if array_counter["six"] == 4:
                unbank_score += 1200
            if array_counter["six"] == 5:
                unbank_score += 2400
            if array_counter["six"] == 6:
                unbank_score += 4800
        if unbank_score==0:
            return 0
        return unbank_score

if __name__=="__main__":
    class01=GameLogic()

    _tuple=(1,1,1,1,1,5)

    inst=class01.roll_dice(6)

    temp=class01.calculate_score(inst)
    print(inst)
    print(temp)




# import random
# class GameLogic:
#     @staticmethod
#     def calculate_score(dice):
#         """
#         Calculate score for a dice roll.
#         Args:
#         - dice: tuple of integers that represent a dice roll.
#         Returns:
#         - integer representing the roll’s score according to rules of game.
#         """
#         score = 0
#         freq = [0] * 7
#         for d in dice:
#             freq[d] += 1
#         if freq.count(0) == 1 and freq.count(5) == 0: # zilch
#             return 0
#         elif freq.count(5) == 1 and freq.count(0) == 1: # five of a kind
#             score = 2000
#             d = freq.index(5)
#             score += (d * 100) * (freq[d] - 5)
#             if freq.count(1) == 2: # two triplets
#                 score += 2500
#         elif freq.count(1) == 6: # straight
#             score = 1500
#         elif freq.count(2) == 4 and freq.count(0) == 2: # two triplets
#             score = 1500
#         else:
#             for i in range(1, 7):
#                 if freq[i] >= 3:
#                     if i == 1: # ones
#                         score += 1000 + (100 * (freq[i] - 3))
#                     elif i == 2: # twos
#                         score += 200 * (freq[i] - 2)
#                     elif i == 3: # threes
#                         score += 300 * (freq[i] - 2)
#                     elif i == 4: # fours
#                         score += 400 * (freq[i] - 2)
#                     elif i == 5: # fives
#                         score += 50 * (freq[i] - 2)
#                     elif i == 6: # sixes
#                         score += 600 * (freq[i] - 2)
#             if freq[1] < 3: # leftover ones
#                 score += 100 * freq[1]
#             if freq[5] < 3: # leftover fives
#                 score += 50 * freq[5]
#         return score
#     @staticmethod
#     def roll_dice(num_dice):
#         """
#         Roll a given number of dice.
#         Args:
#         - num_dice: integer between 1 and 6 representing number of dice to roll.
#         Returns:
#         - tuple with random values between 1 and 6 with length num_dice.
#         """
#         dice = tuple(random.randint(1, 6) for _ in range(num_dice))
#         return dice