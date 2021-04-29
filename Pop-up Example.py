
# https://www.youtube.com/watch?v=tpwu5Zb64lQ

from tkinter import *

root = Tk()
root.geometry("300x300")



def close_pop (confirm):
    pop.destroy()
    # Depending on the requirement and the button purpose you can
    # add additional statements to this function (if, for, while etc.)


def open_pop ():

    global pop
    pop = Toplevel(root)
    pop.title("Wrong Input")
    root.geometry("150x150")

    pop_label = Lable(pop, text="Please follow the instructions", anchor=CENTER, font=("helvetica", 13, "bold") )
    pop_label.pack() # Adding pady=... ????

    # global warning_image
    # warning_image = PhotoImage(file="DIRECTORY")

    pop_frame = Frame(pop)
    pop_frame.pack()

    # pop_pic = Label(pop_frame, image=warning_image, borderwidth=0)
    # pop_pic.grid(row=0, column=0, padx=10)

    ok = Button(pop_frame, text="OK", command=lambda: close_pop("ok") )
    ok.grid(row=0, column=1) # padx=.... ?????


button = button(root, text="Click Me!", command=open_pop)
button.pack(pady=50)


root.mainloop()
