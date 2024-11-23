def solution(string):
    max_streak_X, max_streak_O = 0, 0
    current_streak_X, current_streak_O = 0, 0

    for char in string:
        if char == 'X':
            current_streak_X += 1
            current_streak_O = 0
        elif char == 'O':
            current_streak_O += 1
            current_streak_X = 0
        else:
            current_streak_X, current_streak_O = 0, 0

        max_streak_X = max(max_streak_X, current_streak_X)
        max_streak_O = max(max_streak_O, current_streak_O)

    if max_streak_X >= 3 or max_streak_O >= 3:
        return "X" if max_streak_X >= 3 else "O"
    else:
        return "Tie"


