import tkinter as tk
import FirstScreen as fs
import constants as v

def main():
    """ main function for running Becoming Physics game
    """
    top = tk.Tk()

    # Create LabelFrame from TKinter
    lf1 = tk.LabelFrame(top)
    app1 = fs.FirstScreen(lf1)

    # Place the LabelFrame
    lf1.grid()
    top.mainloop()


if __name__ == "__main__":
    main()