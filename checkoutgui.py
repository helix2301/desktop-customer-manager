import tkinter

# Table of services containing their names and costs.
SERVICES = [('Adult Haircut', 15.95),
            ('Adult Haircut & Dry', 18.95),
            ('Kid Cut', 10.95),
            ('Kids Cut & Dry', 13.95),
            ('Buzz Cut', 10.00),
            ('Waxing', 11.00),
            ('Bleach', 54.95),
            ('Color Dye', 44.95)]

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()

        self.main_window = root
        self.top_frame = tkinter.Frame(self)
        self.bottom_frame = tkinter.Frame(self)

        # Create list of control variables to query state of CheckButtons.
        self.cb_vars = [tkinter.IntVar() for _ in range(len(SERVICES))]

        # Create another list to hold a corresponding Checkbuttons.
        self.cbs = [
            tkinter.Checkbutton(
                self.top_frame,
                text='{}-${:.2f}'.format(SERVICES[i][0], SERVICES[i][1]),
                variable=self.cb_vars[i])
            for i in range(len(self.cb_vars))
        ]
        # Pack the Checkbuttons.
        for i in range(len(self.cbs)):
            self.cbs[i].pack()

        #Create an OK button and Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame,
                    text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                    text='Quit', command=self.main_window.destroy)

        #Pack the buttons.
        self.ok_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Pack frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

    def show_choice(self):
        popup_window = tkinter.Toplevel()
        label_frame = tkinter.LabelFrame(popup_window, text='Total Charges')
        label_frame.pack()
        # Add up the cost of all the items which are checked.
        total = sum(SERVICES[i][1] for i in range(len(self.cb_vars))
                        if self.cb_vars[i].get())
        tkinter.Label(label_frame, text='${:.2f}'.format(total)).pack()
        # Enter a local mainloop and wait for window to be closed by user.
        root.wait_window(popup_window)

root = tkinter.Tk()
app = MyApp(root)
app.master.title('Check Out')
app.mainloop()

