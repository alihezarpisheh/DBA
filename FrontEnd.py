from tkinter import *
import BackEnd
# ============== functions ==============


def clearlist():
    list1.delete(0, END)


def r_function(library):
    for b in library:
        list1.insert(END, b)
# ============== settings ==============


window = Tk()
# ============== Labels and Entries ==============
firstLabel = Label(window, text="Title")
firstLabel.grid(row=0, column=0)

secondLabel = Label(window, text="Author")
secondLabel.grid(row=0, column=2)

thirdLabel = Label(window, text="Year")
thirdLabel.grid(row=1, column=0)

fourthLabel = Label(window, text="ISBN")
fourthLabel.grid(row=1, column=2)

titleText = StringVar()
firstEntry = Entry(window, textvariable=titleText)
firstEntry.grid(row=0, column=1)

authorText = StringVar()
secondEntry = Entry(window, textvariable=authorText)
secondEntry.grid(row=0, column=3)

yearText = StringVar()
thirdEntry = Entry(window, textvariable=yearText)
thirdEntry.grid(row=1, column=1)

ISBNText = StringVar()
fourthEntry = Entry(window, textvariable=ISBNText)
fourthEntry.grid(row=1, column=3)


list1 = Listbox(window, width=40, height=10)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)
# ============== Buttons ==============


def view_command():
    clearlist()
    library = BackEnd.view()
    r_function(library)


btn1 = Button(window, text="View all", width=10, command=view_command)
btn1.grid(row=2, column=3)


def search_command():
    clearlist()
    library = BackEnd.search(titleText.get(), authorText.get(), yearText.get(), ISBNText.get())
    r_function(library)


btn2 = Button(window, text="Search", width=10, command=search_command)
btn2.grid(row=3, column=3)


def add_command():
    clearlist()
    library = BackEnd.add(titleText.get(), authorText.get(), yearText.get(), ISBNText.get())
    view_command()


btn3 = Button(window, text="Add", width=10, command=add_command)
btn3.grid(row=4, column=3)


def got_selected(event):
    global selected_book
    if len(list1.curselection()) > 0:
        i = list1.curselection()
        selected_book = list1.get(i[0])
        firstEntry.delete(0, END)
        firstEntry.insert(END, selected_book[1])
        secondEntry.delete(0, END)
        secondEntry.insert(END, selected_book[2])
        thirdEntry.delete(0, END)
        thirdEntry.insert(END, selected_book[3])
        fourthEntry.delete(0, END)
        fourthEntry.insert(END, selected_book[4])


list1.bind("<<ListboxSelect>>", got_selected)


def edit_command():
    BackEnd.edit(selected_book[0], titleText.get(), authorText.get(), yearText.get(), ISBNText.get())
    view_command()


btn4 = Button(window, text="Edit", width=10, command=edit_command)
btn4.grid(row=5, column=3)


def delete_command():
    BackEnd.delete(selected_book[0])
    view_command()


btn5 = Button(window, text="Delete", width=10, command=delete_command)
btn5.grid(row=6, column=3)

btn6 = Button(window, text="Close app", width=10, command=window.destroy)
btn6.grid(row=7, column=3)

view_command()
window.mainloop()

