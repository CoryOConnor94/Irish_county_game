# import turtle
# import pandas as pd
#
# screen = turtle.Screen()
# screen.title("Irish Counties Game")
# image = "ireland_blank3.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# data = pd.read_csv("irish_counties.csv")
# all_counties = data.County.to_list()
# guessed_counties = []
#
# while len(guessed_counties) < 32:
#     answer_county = screen.textinput(title=f"{len(guessed_counties)}/32 Counties Correct",
#                                      prompt="Whats another county name?").title()
#     if answer_county == "Exit":
#         missing_counties = [county for county in all_counties if county not in guessed_counties]
#         new_data = pd.DataFrame(missing_counties)
#         new_data.to_csv("counties_missed.csv")
#         break
#
#     elif answer_county in all_counties:
#         guessed_counties.append(answer_county)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         county_data = data[data.County == answer_county]
#         t.goto(int(county_data.x), int(county_data.y))
#         t.write(answer_county)

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Irish County Game")
image = "ireland_blank3.gif"
turtle.addshape(image)
turtle.shape(image)

irish_counties_data = pd.read_csv("irish_counties.csv")

irish_county_list = irish_counties_data.County.to_list()
named_counties = []

while len(named_counties) < 32:
    user_answer = screen.textinput(title=f"{len(named_counties)}/32 Counties Correct",
                                   prompt="Enter the name of a county")
    if user_answer == "exit":
        missing_counties = [county for county in irish_county_list if county not in named_counties]
        missed_counties_df = pd.DataFrame(missing_counties)
        missed_counties_df.to_csv("Counties_missed.csv")
        break
    elif user_answer in irish_county_list:
        named_counties.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = irish_counties_data[irish_counties_data.County == user_answer]
        t.goto(int(county_data.x), int(county_data.y))
        t.write(user_answer)

# def get_county_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_county_coordinates)

#user_answer = screen.textinput(title="Name a County", prompt="Enter the name of a county")

screen.mainloop()