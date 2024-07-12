import turtle
import pandas

score = 0
screen = turtle.Screen()
screen.title("U.S States Guessing Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
states = data["state"].str.lower()
listOfStates = states.tolist()
guessedState = []
while(len(guessedState) < 50):
    answer = screen.textinput(f"{len(guessedState)} / 50 States Correct", "Enter another valid State name:")
    if (answer.lower() in listOfStates):
        guessedState.append(answer.lower())
        index = listOfStates.index(answer.lower())
        x_cor = int(data["x"][index])
        y_cor = int(data["y"][index])
        name = data["state"][index]

        newTurtle = turtle.Turtle()
        newTurtle.penup()
        newTurtle.hideturtle()
        newTurtle.goto(x_cor, y_cor)
        newTurtle.write(f"{name}", align="center", font=("Arial", 8, "normal"))
    elif(answer.lower() == "exit"):
        missedStates = []
        for state in listOfStates:
            if(state not in guessedState):
                missedStates.append(state)
        df = pandas.DataFrame(missedStates)
        df.to_csv("missed_States.csv")
        break
screen.exitonclick()
