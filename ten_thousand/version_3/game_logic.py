
import random
from collections import Counter
class GameLogic:
    @staticmethod
    def calculate_score(dice):
        """
        This function receives a tuple of dice values and calculates the score for the roll, based on the game rules.
        """
        score = 0
        counts = Counter(dice)
        # Score 1's and 5's
        score += counts[1] * 100
        score += counts[5] * 50
        # Score three-of-a-kind
        for value in range(1, 7):
            if counts[value] >= 3:
                score += value * 100 if value != 1 else 1000
        # Score four-of-a-kind or better
        for value in range(1, 7):
            if counts[value] >= 4:
                score += value * 100
            elif counts[value] == 5:
                score += 2 * value * 100
            elif counts[value] == 6:
                score += 4 * value * 100
        # Score straights
        if len(counts) == 6:
            score += 2000
        # Score three pairs
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            score += 1500
        return score
    @staticmethod
    def roll_dice(num_dice):
        """
        This function receives the number of dice to roll and returns a tuple of random values between 1 and 6.
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))
    @staticmethod
    def validate_keepers(roll, keepers):
        """
        This function receives a roll and a set of keepers and returns True if the keepers are valid for the roll,
        or False otherwise.
        """
        roll_counts = Counter(roll)
        keepers_counts = Counter(keepers)
        # Check that all keepers are present in the roll
        for value in keepers_counts:
            if keepers_counts[value] > roll_counts[value]:
                return False
        return True
    @staticmethod
    def get_scorers(roll):
        """
        This function receives a roll and returns a tuple of the dice that contribute to the score.
        """
        return tuple(value for value in roll if value in [1, 5] or roll.count(value) >= 3)