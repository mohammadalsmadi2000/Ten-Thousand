import random
class GameLogic:
    @staticmethod
    def calculate_score(dice):
        """
        Calculate score for a dice roll.
        Args:
        - dice: tuple of integers that represent a dice roll.
        Returns:
        - integer representing the roll’s score according to rules of game.
        """
        score = 0
        freq = [0] * 7
        for d in dice:
            freq[d] += 1
        if freq.count(0) == 1 and freq.count(5) == 0: # zilch
            return 0
        elif freq.count(5) == 1 and freq.count(0) == 1: # five of a kind
            score = 2000
            d = freq.index(5)
            score += (d * 100) * (freq[d] - 5)
            if freq.count(1) == 2: # two triplets
                score += 2500
        elif freq.count(1) == 6: # straight
            score = 1500
        elif freq.count(2) == 4 and freq.count(0) == 2: # two triplets
            score = 1500
        else:
            for i in range(1, 7):
                if freq[i] >= 3:
                    if i == 1: # ones
                        score += 1000 + (100 * (freq[i] - 3))
                    elif i == 2: # twos
                        score += 200 * (freq[i] - 2)
                    elif i == 3: # threes
                        score += 300 * (freq[i] - 2)
                    elif i == 4: # fours
                        score += 400 * (freq[i] - 2)
                    elif i == 5: # fives
                        score += 50 * (freq[i] - 2)
                    elif i == 6: # sixes
                        score += 600 * (freq[i] - 2)
            if freq[1] < 3: # leftover ones
                score += 100 * freq[1]
            if freq[5] < 3: # leftover fives
                score += 50 * freq[5]
        return score
    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a given number of dice.
        Args:
        - num_dice: integer between 1 and 6 representing number of dice to roll.
        Returns:
        - tuple with random values between 1 and 6 with length num_dice.
        """
        dice = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice