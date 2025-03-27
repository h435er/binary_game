import curses
import random
import time

def main(stdscr):
    # Farben initialisieren
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    menu_options = ["Play without Timer", "Play with Timer", "Exit/Quit"]
    selected_option = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.addstr(height // 2 - 2, width // 2 - 12, "Welcome to the Binary Game!", curses.color_pair(1))
        
        for idx, option in enumerate(menu_options):
            x = width // 2 - len(option) // 2
            if idx == selected_option:
                stdscr.addstr(height // 2 + idx, x, option, curses.color_pair(2))
            else:
                stdscr.addstr(height // 2 + idx, x, option)
        
        stdscr.refresh()
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif key == ord('\n'):
            if selected_option == 0:
                play_game(stdscr, timer=False)
            elif selected_option == 1:
                play_game(stdscr, timer=True)
            elif selected_option == 2:
                break

def play_game(stdscr, timer=False):
    while True:
        stdscr.clear()
        number = random.randint(1, 255) 
        binary_number = format(number, '08b')
        
        stdscr.addstr(0, 0, f"The decimal number is: {number}")
        stdscr.addstr(2, 0, "Type in binary...(example: 00000001): ")
        stdscr.addstr(5, 0, "press 'q' to get to the menu")
        stdscr.refresh()
        
        input_binary = ""
        start_time = time.time() if timer else None

        while True:
            stdscr.addstr(3, 0, input_binary + " " * (20 - len(input_binary)))  # Leeren Raum für Eingabe
            stdscr.refresh()

            if timer and time.time() - start_time > 10:
                stdscr.clear()
                stdscr.addstr(0, 0, "Time expired!")
                stdscr.addstr(2, 0, f"The right binary number was: {binary_number}")
                stdscr.addstr(4, 0, "Press Enter to continue...")
                stdscr.addstr(5, 0, "press 'q' to get to the menu")
                stdscr.refresh()
                stdscr.getch()
                break
            
            char = stdscr.getch()
            if char == ord('q'):
                return
            elif char == curses.KEY_BACKSPACE or char == 127:  # Backspace
                input_binary = input_binary[:-1]
            elif char == ord('\n'):  # Enter
                break
            else:
                input_binary += chr(char)

        stdscr.clear()
        if input_binary == binary_number:
            stdscr.addstr(0, 0, "Right! Nice!")
        else:
            stdscr.addstr(0, 0, f"Wrong! The riht binary number was: {binary_number}")
        
        stdscr.addstr(2, 0, "Press enter to continue...")
        stdscr.addstr(5, 0, "press 'q' to get to the menu")
        stdscr.refresh()
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
