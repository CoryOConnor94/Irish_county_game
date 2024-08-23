import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Irish Counties Game")
image = "ireland_blank.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("irish_counties.csv")
all_counties = data.County.to_list()
guessed_counties = []

while len(guessed_counties) < 32:
    answer_county = screen.textinput(title=f"{len(guessed_counties)}/32 Counties Correct",
                                     prompt="Whats another county name?").title()
    if answer_county == "Exit":
        missing_counties = [county for county in all_counties if county not in guessed_counties]
        new_data = pd.DataFrame(missing_counties)
        new_data.to_csv("counties_missed.csv")
        break

    elif answer_county in all_counties:
        guessed_counties.append(answer_county)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = data[data.County == answer_county]
        t.goto(int(county_data.x), int(county_data.y))
        t.write(answer_county)