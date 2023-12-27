import argparse
from tkinter import Tk
from gui import TumorGUI

def main(window_title, window_width, window_height):
    root = Tk()
    root.title(window_title)
    root.geometry(f"{window_width}x{window_height}")
    app = TumorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tumor Classification Application")
    parser.add_argument("--title", type=str, default="Tumor Classification", help="Window title")
    parser.add_argument("--width", type=int, default=800, help="Window width")
    parser.add_argument("--height", type=int, default=600, help="Window height")
    args = parser.parse_args()

    main(args.title, args.width, args.height)
