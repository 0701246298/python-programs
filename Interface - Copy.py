import tkinter as tk
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    new_window.geometry('300x200')
    new_window.config(background='blue')
    label = tk.Label(window, text="lets do it Again", bg='yellow', width=100, pady=48, padx=10)
    label.pack(pady=10)



window = tk.Tk()
window.title("New Product")
label = tk.Label(window, text="lets do it Again",bg='yellow',width=100,pady=48,padx=10)
label.pack(pady=10)

# entry for giving name.
field= tk.Entry(window)
field.pack()


# create a button to trigger an event
button = tk.Button(window, text="Click me!!")



def button_click(self):
    label.config(text=field.get())
def change_window_properties():
    window=tk.Tk()
    #change bg color
window.configure(bg='pink')
#change windows size.
#window.geometry('500x500')



button.bind('<Button-1>', button_click,command=open_new_window)
button.pack()

# start the event loop
window.mainloop()

