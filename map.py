import curses
import os
from color import *
import random

MIN_X, MAX_X = 1, 105
MIN_Y, MAX_Y = 4, 26


def load_map(stdscr, file_path, color_option=0):
    curses.curs_set(0)
    init_colors()

    coords = {"walls": [], "zombies": [], "potions": []}

    try:
        # Read the content of the text file
        content = read_text_file(file_path)

        # Split the content into lines
        lines = content.split("\n")

        # Print each line to the stdscr window
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == " ":
                    stdscr.addstr(i, j, char)
                elif char == "X":  # This is the entrace of player
                    stdscr.addstr(i, j, char)
                    coords["entrance"] = (j, i)  # coords["entrance"] marks the entrance
                else:
                    if color_option == 0:
                        stdscr.addstr(i, j, char)
                    elif color_option == 1:
                        stdscr.addstr(
                            i, j, char, ALL_COLORS[random.randrange(len(ALL_COLORS))]
                        )
                    coords["walls"].append((j, i))

        for i in range(100):
            rand_x, rand_y = random.randint(MIN_X, MAX_X), random.randint(MIN_Y, MAX_Y)

            if (rand_x, rand_y) not in coords["walls"] and (rand_x, rand_y) != coords[
                "entrance"
            ]:
                stdscr.addstr(rand_y, rand_x, "Z", FORE_COLORS[0])
                coords["zombies"].append((rand_x, rand_y))

        for i in range(50):
            rand_x, rand_y = random.randint(MIN_X, MAX_X), random.randint(MIN_Y, MAX_Y)

            if (rand_x, rand_y) not in coords["walls"] and (rand_x, rand_y) != coords[
                "entrance"
            ]:
                stdscr.addstr(rand_y, rand_x, "+", FORE_COLORS[1])
                coords["potions"].append((rand_x, rand_y))

        stdscr.refresh()
        return coords

    except FileNotFoundError:
        stdscr.addstr(0, 0, "Error: File not found.")
        stdscr.refresh()
        stdscr.getch()


def stdscr_print_file(stdscr, file_path):
    # curses.curs_set(0)  # Hide the cursor

    try:
        # Read the content of the text file
        content = read_text_file(file_path)

        # Split the content into lines
        lines = content.split("\n")

        # Print each line to the stdscr window
        for i, line in enumerate(lines):
            stdscr.addstr(i, 0, line)

        stdscr.refresh()

    except FileNotFoundError:
        stdscr.addstr(0, 0, "Error: File not found.")
        stdscr.refresh()


def read_text_messages(file_path):
    # Read the content of the text file
    content = read_text_file(file_path)

    # Split the content into lines
    lines = content.split("\n")

    return lines


def read_text_file(file_path):
    # Get the absolute path to the text file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, file_path)

    with open(file_path, "r") as file:
        content = file.read()
    return content
