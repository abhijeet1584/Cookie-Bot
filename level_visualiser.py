def showlvl(score, total):
    # black_circle
    scoreOutOf90 = total - score
    # Since the level is increased every 90 messages
    percentage = (scoreOutOf90/90) * 10.0 # Display it in the range of 1 to 10
    percentage = round(percentage)
    if percentage == 1:
        return ":white_large_square: :cookie: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 2:
        return ":white_large_square: :cookie: :cookie: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 3:
        return ":white_large_square: :cookie: :cookie: :cookie: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 4:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 5:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :cookie: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 6:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :black_circle: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 7:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :black_circle: :black_circle: :black_circle: :blue_square:"

    elif percentage == 8:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :black_circle: :black_circle: :blue_square:"

    elif percentage == 9:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :black_circle: :blue_square:"

    elif percentage == 10:
        return ":white_large_square: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :cookie: :blue_square:"