# Tkinter’s Button widget doesn’t pass any information to the callback. This makes things a bit complicated if you want to use the same callback for several buttons, like in this example:

# def callback():
    # print "button", "?"

# Button(text="one",   command=callback).pack()
# Button(text="two",   command=callback).pack()
# Button(text="three", command=callback).pack()
# A common beginner’s mistake is to call the callback function when constructing the widget. That is, instead of giving just the function’s name (e.g. “callback”), the programmer adds parentheses and argument values to the function:

# def callback(number):
    # print "button", number

# Button(text="one",   command=callback(1)).pack()
# Button(text="two",   command=callback(2)).pack()
# Button(text="three", command=callback(3)).pack()
# If you do this, Python will call the callback function before creating the widget, and pass the function’s return value to Tkinter. Tkinter then attempts to convert the return value to a string, and tells Tk to call a function with that name when the button is activated. This is probably not what you wanted.