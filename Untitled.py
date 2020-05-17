from tkinter import *

root = Tk()
var = StringVar()
var.set('Select')

def foo(value):
    var.set(value)
    print("foo1" + value)

def foo2(value):
    var.set(value)
    print("foo2 " + value)

def foo3(value):
    var.set(value)
    print("foo3 " + value)

def change_menu(value):
    var.set('Select')
    print('changing optionmenu commands')
    populate_menu(optionmenu, one=foo3, two=foo3)

def populate_menu(optionmenu, **cmds):
    menu = optionmenu['menu']
    menu.delete(0, "end")
    for name, func in cmds.items():
        menu.add_command(label=name, command=
                         lambda name=name, func=func: func(name))

optionmenu = OptionMenu(root, var, ())  # no choices supplied here
optionmenu.pack()
Label(root, textvariable=var).pack()

populate_menu(optionmenu, one=foo, two=foo2, change=change_menu)

root.mainloop()