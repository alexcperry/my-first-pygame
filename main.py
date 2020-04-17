import game

print("Hit enter to start game?")
play = input()
score = game.play_game()

print("Your final score was: " + str(score))