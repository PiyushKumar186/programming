from Tkinter import *

root = Tk()

v = IntVar()

Label(root,
      text="""Choose a Programming Language:""",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(root,
            text="Python",
            padx = 20,
            variable = v,
            value = 1).pack(anchor = W)
Radiobutton(root,
            text="Perl",
            padx = 20,
            variable = v,
            value = 2).pack(anchor=W)
Radiobutton(root,
            text="C",
            padx = 20,
            variable = v,
            value = 3). pack(anchor=W)
mainloop()