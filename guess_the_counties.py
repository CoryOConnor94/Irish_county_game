import turtle
import pandas as pd
from tkinter import messagebox

# Constants
TOTAL_COUNTIES = 32
IMAGE_PATH = "ireland_blank3.gif"
COUNTIES_DATA_PATH = "irish_counties.csv"
MISSED_COUNTIES_OUTPUT = "Counties_missed.csv"


def setup_screen():
    """Sets up the turtle screen with the Ireland map image."""
    screen = turtle.Screen()
    screen.title("Irish County Game")
    turtle.addshape(IMAGE_PATH)
    turtle.shape(IMAGE_PATH)
    return screen


def read_county_data(file_path):
    """Reads the Irish counties data from a CSV file."""
    return pd.read_csv(file_path)


def write_missing_counties(missing_counties):
    """Writes the list of missing counties to a CSV file."""
    pd.DataFrame(missing_counties).to_csv(MISSED_COUNTIES_OUTPUT, index=False)


def get_user_input(screen, named_counties_count):
    """Prompts the user to enter the name of a county."""
    return screen.textinput(
        title=f"{named_counties_count}/{TOTAL_COUNTIES} Counties Correct",
        prompt="Enter the name of a county"
    ).strip().lower()


def place_county_name(county_name, county_data):
    """Places the county name on the map at the specified coordinates."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    county_info = county_data[county_data.County.str.lower() == county_name]
    t.goto(int(county_info.x), int(county_info.y))
    t.write(county_name.capitalize())


def main():
    # Setup screen and read data
    screen = setup_screen()
    county_data = read_county_data(COUNTIES_DATA_PATH)

    # Initialize variables
    irish_county_list = set(county_data.County.str.lower().to_list())
    named_counties = set()

    # Main game loop
    while len(named_counties) < TOTAL_COUNTIES:
        user_answer = get_user_input(screen, len(named_counties))

        if user_answer == "exit":
            missing_counties = [county.capitalize() for county in irish_county_list if county not in named_counties]
            write_missing_counties(missing_counties)
            break
        elif user_answer in irish_county_list and user_answer not in named_counties:
            named_counties.add(user_answer)
            place_county_name(user_answer, county_data)
        else:
            messagebox.showinfo("Invalid County", "That's not a valid county name. Try again.")

    # Keep the screen open until the user clicks
    screen.mainloop()


if __name__ == "__main__":
    main()
