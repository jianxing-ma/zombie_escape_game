#!usr/bin/python3
"""
This is game execution main file, including the main game logic
"""
import curses
from color import *
from map import *


def main():
    print(read_text_file("welcome_message.txt"))
    input()

    curses.wrapper(execute)

    curses.endwin()


def execute(stdscr):
    map_coords = load_map(stdscr, "map1.txt", 1)
    navigate_map(stdscr, map_coords)


def navigate_map(stdscr, map_coords):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input mode
    init_colors()

    x, y = map_coords["entrance"]

    while True:
        # Print the character at the updated position
        stdscr.addch(y, x, "X", BACK_COLORS[5])
        stdscr.refresh()

        if (x, y) in map_coords["zombies"]:
            encounter_zombies(stdscr)
            map_coords["zombies"].remove((x, y))
        if (x, y) in map_coords["potions"]:
            encounter_potion(stdscr)

        # Wait for user input (arrow keys)
        key = stdscr.getch()

        # Move the character based on the arrow key pressed
        if key in [ord("w"), ord("s"), ord("a"), ord("d")]:
            stdscr.addstr(y, x, " ")
            stdscr.refresh()

            if key == ord("w") and (x, y - 1) not in map_coords["walls"]:  # UP Arrow
                y -= 1
            elif (
                key == ord("s") and (x, y + 1) not in map_coords["walls"]
            ):  # DOWN Arrow
                y += 1
            elif (
                key == ord("a") and (x - 1, y) not in map_coords["walls"]
            ):  # LEFT Arrow
                x -= 1
            elif (
                key == ord("d") and (x + 1, y) not in map_coords["walls"]
            ):  # RIGHT Arrow
                x += 1

        # Exit the loop if the 'q' key is pressed
        if key == ord("q"):
            break


def encounter_zombies(stdscr):
    messages = read_text_messages("zombie_messages.txt")
    stdscr.addstr(28, 1, " " * 105)
    stdscr.addstr(28, 10, messages[random.randrange(len(messages))], FORE_COLORS[0])
    stdscr.refresh()


def encounter_potion(stdscr):
    stdscr.addstr(28, 1, " " * 105)
    stdscr.addstr(28, 40, "You retrieved a potion!", FORE_COLORS[1])


if __name__ == "__main__":
    main()
