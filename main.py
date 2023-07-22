#!usr/bin/python3
import curses


def main():
    curses.wrapper(execute)


def execute(stdscr):
    stdscr.addstr(0, 0, "Hello")
    stdscr.getch()


if __name__ == "__main__":
    main()
