import random

points = 1000 #set default amount of points

print("High Low Game")
print(" ")
print("RULES:")
print(" ")
print("Numbers 1 through 6 are low")
print("Numbers 7 through 13 are high")

def hi_lo(points): 
  randomNumber = random.randint(1,13) #generate random number

  while points > 0: #loop which continously asks for user input until points are 0
    print("You have", points, "points")
    print(" ")
    user_pointsRisked = int(input("Enter points to risk: "))
    if user_pointsRisked <=0: #checking if user input is greater than 0
      print("Invalid input: Please enter a number greater than 0")
      print(" ")
      continue
    user_Prediction = input("Predict (1 = High, 0 = Low): ")

    def high(randomNumber, points, user_Prediction): #function for high prediction
      if randomNumber > 7 and user_Prediction == "1": #if statement that activates if user guesses correctly
        print("Number is", randomNumber)
        print("You win")
        points = points + user_pointsRisked * 2
        if points == 0:
          print("Game Over! You have no more points")
          exit()
        elif points > 0:
          playAgain = input("Play again? (y/n): ")
          if playAgain == "y":
            hi_lo(points)
          elif playAgain == "n":
            print("Final score:", points)
            exit()
      elif randomNumber > 7 and user_Prediction == "0": #elif statement that activates if user guesses incorrectly
        print("Number is", randomNumber)
        print("You lose")
        points = points - user_pointsRisked
        if points == 0:
          print("Game Over! You have no more points")
          exit()
        elif points > 0:
          playAgain = input("Play again? (y/n): ")
          if playAgain == "y":
            hi_lo(points)
          elif playAgain == "n":
            print("Final score:", points)
            exit()

    high(randomNumber, points, user_Prediction)

    def low(randomNumber, points, user_Prediction): #function for low prediction
      if randomNumber < 7 and user_Prediction == "0": #if statement that activates if user guesses correctly
        print("Number is", randomNumber)
        print("You win")
        points = points + user_pointsRisked * 2
        if points == 0:
          print("Game Over! You have no more points")
          exit()
        elif points > 0:
          playAgain = input("Play again? (y/n): ")
          if playAgain == "y":
            hi_lo(points)
          elif playAgain == "n":
            print("Final score:", points)
            exit()
      elif randomNumber < 7 and user_Prediction == "1": #elif statement that activates if user guesses incorrectly
        print("Number is", randomNumber)
        print("You lose")
        points = points - user_pointsRisked
        if points == 0:
          print("Game Over! You have no more points")
          exit()
        elif points > 0:
          playAgain = input("Play again? (y/n): ")
          if playAgain == "y":
            hi_lo(points)
          elif playAgain == "n":
            print("Final score:", points)
            exit()

    low(randomNumber, points, user_Prediction)

    if randomNumber == 7: #if statement that activates if the random number is 7
      print("Number is", randomNumber)
      print("Game Over! You automatically loose")
      points = 0
      exit()

hi_lo(points)