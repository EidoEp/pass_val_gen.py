import re                           # For Regex.
import random                       # For shuffling values.
import webbrowser                   # For using browser related features.
import tkinter                      # Simple PY UI.
from tkinter import *               # Simple PY UI.
from tkinter import messagebox      # Tkinter messagebox options.
from tkinter import ttk             # For handling the scroll bar.

###
### 2D Array for displaying password strength.
###
string_crack_time = \
    [  # column  0 1 2 3 4
        ["Instantly", "Instantly", "Instantly", "Instantly", "Instantly"],  #
        ["Instantly", "Instantly", "Instantly", "Instantly", "Instantly"],  # row     0 -> 3
        ["Instantly", "Instantly", "Instantly", "3 secs", "10 secs"],  # 1 -> 4
        ["Instantly", "Instantly", "8 secs", "3 mins", "13 mins"],  # 2 -> 5
        ["Instantly", "Instantly", "5 mins", "3 hrs", "17 hrs"],  # 3 -> 6
        ["Instantly", "13 mins", "3 hrs", "10 days", "57 days"],  # .
        ["4 secs", "6 hrs", "4 days", "1 year", "12 years"],  # .
        ["40 secs", "6 days", "169 days", "106 years", "928 years"],  # .
        ["6 mins", "169 days", "16 years", "6k years", "71k years"],
        ["1 hr", "12 years", "600 years", "108k years", "5m years"],
        ["11 hrs", "314 years", "21k years", "25m years", "423m years"],
        ["4 days", "8k years", "778k years", "1bn years", "5bn years"],
        ["46 days", "212k years", "28m years", "97bn years", "2tn years"],
        ["1 year", "512m years", "1bn years", "6tn years", "193tn years"],
        ["12 year", "143m years", "36bn years", "374tn years", "14qd years"],
        ["126 year", "3bn years", "1tn years", "23qd years", "1qt years"]  # 15 -> 18
    ]


###
### UI related
###

def linkedin_url(url):
    # You can also make a call to open a directory;
    # webbrowser.open_new(r"file://c:\test\test.csv")
    webbrowser.open_new(url)


def wrong_input():
    messagebox.showwarning("Wrong Input", "Please follow the instructions.")


def bar_press():
    str_val = input_var_val.get()
    press_val = onclick_validation(str_val)
    if press_val == "red":
        style_bar.configure('frenetic.Horizontal.TProgressbar', foreground='white', background='red')
        bar_val['value'] = 33.33333
    elif press_val == "yellow":
        style_bar.configure('frenetic.Horizontal.TProgressbar', foreground='white', background='yellow')
        bar_val['value'] = 66.66666
    elif press_val == "green":
        style_bar.configure('frenetic.Horizontal.TProgressbar', foreground='white', background='green')
        bar_val['value'] = 99.99999
    else:
        style_bar.configure('frenetic.Horizontal.TProgressbar', foreground='white', background='black')
        bar_val['value'] = 99.99999


###
### Validating a password
###
def onclick_validation(pass_chk):
    # Setting to pull text from the 2D array
    row = len(pass_chk) - 3

    # All chars, AL1 each
    if re.match(r'^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{3,18}$)', pass_chk):
        column = 4
        crack = string_crack_time[row][column]
        label_crack["text"] = "The time to crack this password:"
        entry_val3["text"] = crack
        if row <= 5:
            entry_val2["text"] = "Weak"
            return "red"
        elif row == 6:
            entry_val2["text"] = "Fair"
            return "yellow"
        else:
            entry_val2["text"] = "Strong"
            return "green"

    # All chars, AL1 each, except special chars.
    elif re.match(r'^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{3,18}$)', pass_chk):
        column = 3
        crack = string_crack_time[row][column]
        label_crack["text"] = "The time to crack this password:"
        entry_val3["text"] = crack
        if row <= 5:
            entry_val2["text"] = "Weak"
            return "red"
        elif row == 6:
            entry_val2["text"] = "Fair"
            return "yellow"
        else:
            entry_val2["text"] = "Strong"
            return "green"

    # Big and small letters, AL1 each.
    elif re.match(r'^((?=.*[a-z])(?=.*[A-Z])[A-Za-z]{3,18}$)', pass_chk):
        column = 2
        crack = string_crack_time[row][column]
        label_crack["text"] = "The time to crack this password:"
        entry_val3["text"] = crack
        if row <= 6:
            entry_val2["text"] = "Weak"
            return "red"
        else:
            entry_val2["text"] = "Fair"
            return "yellow"

    # Big or small letters, AL1 each.
    elif re.match(r'^(([A-Z]{3,18})|([a-z]{3,18})$)', pass_chk):
        column = 1
        crack = string_crack_time[row][column]
        label_crack["text"] = "The time to crack this password:"
        entry_val3["text"] = crack
        if row <= 7:
            entry_val2["text"] = "Weak"
            return "red"
        else:
            entry_val2["text"] = "Fair"
            return "yellow"

    # Big or small letters, AL1 each.
    elif re.match(r'^\d{3,18}$', pass_chk):
        column = 0
        crack = string_crack_time[row][column]
        label_crack["text"] = "The time to crack this password:"
        entry_val3["text"] = crack
        if row <= 11:
            entry_val2["text"] = "Weak"
            return "red"
        else:
            entry_val2["text"] = "Fair"
            return "yellow"

    # Weak all chars, between 3 and 8
    elif re.match(r'^[A-Za-z\d@$!%*#?&]{3,8}$', pass_chk):
        entry_val2["text"] = "Weak"
        label_crack["text"] = "The time to crack this password:"
        entry_val3["text"] = "Instantly"
        return "red"

    # Less then 3 chars
    elif re.match(r'(^[\w\W]{0,2}$)', pass_chk):
        entry_val2["text"] = "Wrong Input"
        label_crack["text"] = "The number of characters used is too low."
        entry_val3["text"] = ""

    # More then 18 chars
    elif re.match(r'(^[\w\W]{18,}$)', pass_chk):
        entry_val2["text"] = "Wrong Input"
        label_crack["text"] = "The number of characters used is too high."
        entry_val3["text"] = ""

    else:
        wrong_input()


###
### Generating a password - configs
###

# All the chars without limitation.
def all_chars(pass_length):
    password = ""
    for count in range(0, pass_length):
        random_pick = random.randint(1, 4)
        if random_pick == 1:
            password += str(random.randint(0, 9))
        elif random_pick == 2:
            password += random.choice("abcdefghijklmnopqrstuvwxyz")
        elif random_pick == 3:
            password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            password += random.choice("@$!%*#?&")

    label_gen["text"] = "Your password is:"
    entry_gen2.config(state=NORMAL)
    entry_gen2.delete(0, END)
    entry_gen2.insert(0, password)
    entry_gen2.config(state="readonly")


# All the chars, at least one of each.
def al1_all_chars(pass_length):
    password = ""
    al1_all_pass = None
    while al1_all_pass is None:
        for count in range(0, pass_length):
            random_pick = random.randint(1, 4)
            if random_pick == 1:
                password += str(random.randint(0, 9))
            elif random_pick == 2:
                password += random.choice("abcdefghijklmnopqrstuvwxyz")
            elif random_pick == 3:
                password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            else:
                password += random.choice("@$!%*#?&")

        al1_all_pass = re.match(r'^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{3,18}$)', password)

    label_gen["text"] = "Your password is:"
    entry_gen2.config(state=NORMAL)
    entry_gen2.delete(0, END)
    entry_gen2.insert(0, password)
    entry_gen2.config(state="readonly")


# All the chars, except special chars and at least one of each.
def al1_no_special_chars(pass_length):
    password = ""
    al1_no_special_pass = None
    while al1_no_special_pass is None:
        for count in range(0, pass_length):
            random_pick = random.randint(1, 3)
            if random_pick == 1:
                password += str(random.randint(0, 9))
            elif random_pick == 2:
                password += random.choice("abcdefghijklmnopqrstuvwxyz")
            else:
                password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        al1_no_special_pass = re.match(r'^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{3,18}$)', password)

    label_gen["text"] = "Your password is:"
    entry_gen2.config(state=NORMAL)
    entry_gen2.delete(0, END)
    entry_gen2.insert(0, password)
    entry_gen2.config(state="readonly")


# Mixed letters, at least one small and big letters
def al1_letters_mixed_chars(pass_length):
    password = ""
    al1_letters_mixed_pass = None
    while al1_letters_mixed_pass is None:
        for count in range(0, pass_length):
            pass_type2 = random.randint(1, 2)
            if pass_type2 == 1:
                password += random.choice("abcdefghijklmnopqrstuvwxyz")
            else:
                password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        al1_letters_mixed_pass = re.match(r'^((?=.*[a-z])(?=.*[A-Z])[A-Za-z]{3,18}$)', password)

    label_gen["text"] = "Your password is:"
    entry_gen2.config(state=NORMAL)
    entry_gen2.delete(0, END)
    entry_gen2.insert(0, password)
    entry_gen2.config(state="readonly")


# Small or big letters only.
def letters_fixed_chars(pass_length):
    password = ""
    pass_type2 = random.randint(1, 2)
    if pass_type2 == 1:
        for count in range(0, pass_length):
            password += random.choice("abcdefghijklmnopqrstuvwxyz")
    else:
        for count in range(0, pass_length):
            password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    label_gen["text"] = "Your password is:"
    entry_gen2.config(state=NORMAL)
    entry_gen2.delete(0, END)
    entry_gen2.insert(0, password)
    entry_gen2.config(state="readonly")


# Digits only.
def digits_fixed_chars(pass_length):
    password = ""
    for count in range(0, pass_length):
        password += str(random.randint(0, 9))

    label_gen["text"] = "Your password is:"
    entry_gen2.config(state=NORMAL)
    entry_gen2.delete(0, END)
    entry_gen2.insert(0, password)
    entry_gen2.config(state="readonly")


###
### Generating a password - logic
###
def onclick_generator():  # Value received should be Weak/Fair/Strong OR Other

    gen_type = input_var_gen.get()

    # Weak Gen
    if gen_type == "Weak" or gen_type == "weak":
        pass_length = random.randint(3, 14)
        # 8 chars and below
        if pass_length <= 8:
            all_chars(pass_length)

        # 9 chars only
        elif pass_length == 9:
            pass_type = random.randint(1, 3)
            if pass_type == 1:
                digits_fixed_chars(pass_length)
            elif pass_type == 2:
                letters_fixed_chars(pass_length)
            else:
                al1_letters_mixed_chars(pass_length)

        # 10 chars only
        elif pass_length == 10:
            pass_type = random.randint(1, 2)
            if pass_type == 1:
                digits_fixed_chars(pass_length)
            else:
                letters_fixed_chars(pass_length)

        # 11-14 chars
        else:
            digits_fixed_chars(pass_length)

    # Fair Gen
    elif gen_type == "Fair" or gen_type == "fair":

        pass_length = random.randint(9, 18)

        # 9 chars only
        if pass_length == 9:
            pass_type = random.randint(1, 2)
            if pass_type == 1:
                al1_all_chars(pass_length)
            else:
                al1_no_special_chars(pass_length)

        # 10 chars only
        elif pass_length == 10:
            al1_letters_mixed_chars(pass_length)

        # 11-14 chars
        elif pass_length <= 15:
            pass_type = random.randint(1, 2)
            if pass_type == 1:
                al1_letters_mixed_chars(pass_length)
            else:
                letters_fixed_chars(pass_length)

        # 15-18 chars
        else:
            pass_type = random.randint(1, 3)
            if pass_type == 1:
                digits_fixed_chars(pass_length)
            elif pass_type == 2:
                letters_fixed_chars(pass_length)
            else:
                al1_letters_mixed_chars(pass_length)

    # Strong Gen
    elif gen_type == "Strong" or gen_type == "strong":
        # 10-18 chars
        pass_length = random.randint(10, 18)
        pass_type = random.randint(1, 2)
        if pass_type == 1:
            al1_all_chars(pass_length)
        else:
            al1_no_special_chars(pass_length)

    # Wrong input
    else:
        wrong_input()


###
### User interface
###

interface = Tk()
# Window size
interface.geometry("470x580")

###
### Header
###
interface.title("Password Generator & Validator [Win]")

# Headline
headline = Label(interface, text="Password Generator & Validator", font=('Helvetica', 16, 'bold'))
headline.pack(pady=15)

###
### Body
###

# Instructions
instructions1 = Label(interface,
                     text="    The following password options are available in this script;\n\n    \u2022 Numbers only.\n    \u2022 Upper or lower case letters.\n    \u2022 Upper and lower case letters mixed.\n    \u2022 Numbers, upper and lower case letters.\n    \u2022 Special charecters [@$!%*#?&], numbers, upper and lower case letters.",
                     font=('Helvetica', 10, ""),
                     # bd=1,
                     # relief="sunken",
                     justify="left")

# Note
instructions1.pack(anchor=W)
noteFrame = Frame(interface)
noteFrame.pack(side=TOP, anchor=NW, padx=17, pady=10)
instructions2 = Label(noteFrame, text="Note:", font=('Helvetica', 10, "bold"), fg="blue", justify="left")
instructions2.pack(side=LEFT)
instructions3 = Label(noteFrame, text="The crack time doesn't consider dictionary but strings.", font=('Helvetica', 10), justify="left")
instructions3.pack(side=LEFT)

##
## Validator
##

# Sub-headers
sub_head_val1 = Label(interface, text="   Validator:", font=('Helvetica', 13, 'bold'))
sub_head_val1.pack(anchor=W)
sub_head_val2 = Label(interface, text="    Check if the password you have in mind is good.",
                      font=('Helvetica', 10, ''))
sub_head_val2.pack(anchor=W)

# Frames for the validator fields
# First Frame
validateFrame1 = Frame(interface)
validateFrame1.pack(side=TOP, anchor=NW)
# Second Frame
validateFrame2 = Frame(interface)
validateFrame2.pack(side=TOP, anchor=NW, padx=20)
# Third Frame
validateFrame3 = Frame(interface)
validateFrame3.pack(side=TOP, anchor=NW, padx=17)

# Input & Bar
style_bar = ttk.Style()
style_bar.theme_use('clam')
input_var_val = StringVar()
entry_val = Entry(validateFrame1, textvar=input_var_val, font=('Helvetica', 10, '')).pack(side=LEFT, padx=20, pady=15)
bar_val = ttk.Progressbar(validateFrame2, style='frenetic.Horizontal.TProgressbar', orient=HORIZONTAL, length=100,
                          mode='determinate')
entry_val2 = tkinter.Label(validateFrame2, text="", font=('Helvetica', 10, 'bold'))
entry_val3 = tkinter.Label(validateFrame3, text="", font=('Helvetica', 10, 'bold'))
label_crack = tkinter.Label(validateFrame3, text="", font=('Helvetica', 10, ''))
button_val = Button(validateFrame1, text="Check", command=bar_press).pack(side=LEFT, pady=10)
bar_val.pack(side=LEFT)
entry_val2.pack(side=LEFT, padx=13)
label_crack.pack(side=LEFT)
entry_val3.pack(side=LEFT, padx=5)

##
## Generator
##

# Sub-headers
sub_head_gen1 = Label(interface, text="\n   Generator:", font=('Helvetica', 13, 'bold'))
sub_head_gen1.pack(anchor=W)
sub_head_gen2 = Label(interface,
                      text="    Create a random password according to your needs.\n    Input- Weak / Fair / Strong",
                      font=('Helvetica', 10, ''), justify="left")
sub_head_gen2.pack(anchor=W)

# Frames for the generator fields
# First Frame
generateFrame1 = Frame(interface)
generateFrame1.pack(side=TOP, anchor=NW, padx=20)
# Second Frame
generateFrame2 = Frame(interface)
generateFrame2.pack(side=TOP, anchor=NW, padx=20)

# Input
input_var_gen = StringVar()
entry_gen = Entry(generateFrame1, textvar=input_var_gen, font=('Helvetica', 10, '')).pack(side=LEFT, pady=15)
label_gen = tkinter.Label(generateFrame2, text="", font=('Helvetica', 10, ''))
entry_gen2 = Entry(generateFrame2, font=('Helvetica', 10, 'bold'), bd=0, state=DISABLED)
button_gen = Button(generateFrame1, text="Generate", command=onclick_generator).pack(side=LEFT, padx=20)
label_gen.pack(side=LEFT)
entry_gen2.pack(side=LEFT, padx=7)

###
### Footer
### Creating a Frame for the footer
###
bottomFrame = Frame(interface)
bottomFrame.pack(side=BOTTOM, anchor=SW)
# Created By...
creatorLabel = Label(bottomFrame,
                     font=('arial', 10, 'bold'),
                     text="    Eido Epstein |\n",
                     anchor=W
                     )
creatorLabel.pack(side=LEFT)
# Linkedin URL Link
linkedinFrame = Frame(bottomFrame)
linkedinFrame.pack(side=LEFT)
linkedin = Label(linkedinFrame,
                 text="Linkedin\n",
                 fg="blue",
                 cursor="hand2",
                 font=('arial', 10, 'bold')
                 )
linkedin.pack(side=LEFT)
linkedin.bind("<Button-1>", lambda e: linkedin_url("www.linkedin.com/in/eido-epstein"))

###
### Closing the UI loop
###
interface.mainloop()
