import curses

COLORS = [
    curses.COLOR_BLACK,
    curses.COLOR_RED,
    curses.COLOR_GREEN,
    curses.COLOR_YELLOW,
    curses.COLOR_BLUE,
    curses.COLOR_MAGENTA,
    curses.COLOR_CYAN,
    curses.COLOR_WHITE,
]

FORE_COLORS = []
BACK_COLORS = []
ALL_COLORS = []


def main(stdscr):
    init_colors()

    stdscr.addstr(5, 10, "Hello, ", BACK_COLORS[3])
    stdscr.addstr("World!", FORE_COLORS[2])  # Print "World!" using the default color
    stdscr.refresh()

    stdscr.getch()  # Wait for a key press before exiting


def init_colors():
    curses.start_color()  # Enable color support

    # CREATE FOREGROUND COLORS
    for i in range(1, len(COLORS)):
        curses.init_pair(
            i, COLORS[i], COLORS[0]
        )  # create foreground colors from 1 to 7
        FORE_COLORS.append(curses.color_pair(i))
        ALL_COLORS.append(curses.color_pair(i))

    # CREATE BACKGROUND COLORS
    for i in range(len(COLORS) - 1):
        curses.init_pair(
            i + 11, COLORS[7], COLORS[i]
        )  # create background colors from 11 to 17
        BACK_COLORS.append(curses.color_pair(i + 11))
        ALL_COLORS.append(curses.color_pair(i + 11))


if __name__ == "__main__":
    curses.wrapper(main)
