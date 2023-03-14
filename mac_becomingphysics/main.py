import tkinter as tk
from FirstScreen import FirstScreen

def main():
    """ main function for running Becoming Physics game
    """
    top = tk.Tk()

    # Create LabelFrame from TKinter
    lf1 = tk.LabelFrame(top)
    app1 = FirstScreen(lf1)

    # Place the LabelFrame
    lf1.grid()
    top.mainloop()


if __name__ == "__main__":
    main()