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
    # Access the underlying tkinter root window
    root = screen._root
    # Set the window to full screen
    root.attributes('-fullscreen', True)
    turtle.addshape(IMAGE_PATH)
    turtle.shape(IMAGE_PATH)
    return screen


def read_county_data(file_path):
    """Reads the Irish counties data from a CSV file."""
    return pd.read_csv(file_path)


def write_missing_counties(missing_counties, county_data):
    """Writes the list of missing counties to the map using Turtle graphics."""
    # Save the list of missing counties to a CSV file
    pd.DataFrame(missing_counties).to_csv("Counties_missed.csv", index=False)

    # Create a turtle to write the missing counties on the map
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    for county in missing_counties:
        # Find the corresponding row in the DataFrame for the missing county
        county_info = county_data[county_data.County.str.lower().str.strip() == county.strip().lower()]

        if not county_info.empty:
            # Extract the x and y coordinates for the county from the DataFrame
            x = int(county_info.x)
            y = int(county_info.y)
            # Move the turtle to the county's position and write the county name
            t.goto(x, y)
            t.write(county.capitalize(), align="center", font=("Comic Sans MS", 10, "bold"))

    # Convert each missing county to string with bullet point to output in message box to user
    missing_counties_str = "\n".join([f"• {county.capitalize()}" for county in missing_counties])
    messagebox.showinfo("Missing Counties", f"The following counties were missed:\n{missing_counties_str}")


def get_user_input(screen, named_counties_count):
    """Prompts the user to enter the name of a county."""
    return screen.textinput(
        title=f"{named_counties_count}/{TOTAL_COUNTIES} Counties Correct",
        prompt="Enter the name of a county").strip().lower()


def place_county_name(county_name, county_data):
    """Places the county name on the map at the specified coordinates."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    county_info = county_data[county_data.County.str.lower() == county_name]
    t.goto(int(county_info.x), int(county_info.y))
    t.write(county_name.capitalize(), font=("Comic Sans MS", 10, "bold"))


def main():
    # Setup screen and read data
    screen = setup_screen()
    county_data = read_county_data(COUNTIES_DATA_PATH)
    root = screen._root
    # Initialize variables
    irish_county_list = set(county_data.County.str.lower().to_list())
    named_counties = set()

    # Main game loop
    while len(named_counties) < TOTAL_COUNTIES:
        user_answer = get_user_input(screen, len(named_counties))

        if user_answer == "exit":
            missing_counties = [county.capitalize() for county in irish_county_list if county not in named_counties]
            write_missing_counties(missing_counties, county_data)
            root.destroy()  # Destroy the main window
            break
        elif user_answer in named_counties:
            messagebox.showinfo("Already Guessed", "You've already guessed that county! Try another one.")
        elif user_answer in irish_county_list and user_answer not in named_counties:
            named_counties.add(user_answer)
            place_county_name(user_answer, county_data)
        else:
            messagebox.showinfo("Invalid County", "That's not a valid county name. Try again.")

    # Keep the screen open until the user clicks
    screen.mainloop()


if __name__ == "__main__":
    main()
