# Irish County Guessing Game
![image](https://github.com/user-attachments/assets/0e75af17-a9af-4d73-a1b2-eb286f2705d1)

This is a **Turtle-based game** where players try to guess all **32 counties of Ireland** by entering their names. Correct guesses will display the county name on a map, while missed counties are saved for review.

## Features

- **Interactive guessing game** to learn Irish counties
- **Graphical map display** using **Turtle graphics**
- **Tracks progress** with a correct guess counter
- **Stores missed counties** in a CSV file
- **Gives feedback** on invalid or duplicate entries
- **Fullscreen mode** for better visualization

## Prerequisites

- **Python 3.x** installed
- **Required libraries:** Install dependencies using:
  ```sh
  pip install pandas tk
  ```

## Setup

1. Clone this repository or download the script.
2. Ensure the following directory structure is present:
   ```
   ├── ireland_blank3.gif   # Ireland map image
   ├── irish_counties.csv   # List of counties with coordinates
   ├── game.py              # Main game script
   ```
3. Run the script:
   ```sh
   python game.py
   ```

## Usage

- The game starts in **fullscreen mode** with a **blank Ireland map**.
- Enter county names in the **pop-up text box**.
- **Correct entries** appear on the map at their locations.
- If a county is guessed **twice**, a message will notify the player.
- Type **"exit"** at any time to quit and **view missed counties**.
- Missed counties are saved in **Counties_missed.csv**.

## Example Output

```
[INFO] Displaying Ireland map.
[INFO] Enter a county name: "Dublin"
[INFO] Dublin added to map.
[INFO] Enter a county name: "Cork"
[INFO] Cork added to map.
[INFO] Exiting game. Counties missed saved to CSV.
```

## Notes

- **If all 32 counties are guessed correctly**, the game ends automatically.
- The **reset function** allows users to restart and try again.
- If you enter an incorrect or non-existent county, a message will notify you.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute the code with attribution.



