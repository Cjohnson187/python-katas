"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
Note: your solution must not modify the input list.

"""
from collections import Counter

def score(dice: list) -> int:
    # create map for dice values
    triple_points = {
        1: 1000,
        2: 200,
        3: 300,
        4: 400,
        5: 500,
        6: 600,
    }
    single_points = {
        1: 100,
        5: 50,
    }
    die_list = dice[:]
    # sort dice
    die_list.sort()
    # check for three similar in the list
    counts = Counter(die_list)
    triple = [num for num, count in counts.items() if count >= 3]
    result_list = []
    points = 0
    if len(triple) > 0:
        triple_index = die_list.index(triple[0])
        result_list = die_list[:triple_index] + die_list[triple_index+3:]
        points = sum(triple_points[die] for die in triple if die in triple_points)
    else:
        result_list = die_list[:]
    points += sum(single_points[die] for die in result_list if die in single_points)
    return points