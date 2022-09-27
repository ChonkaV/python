from tkinter import *
from tkinter import messagebox
import json

FONT = ("Arial", 20, "bold")
STATIONS = ["Station_1", "Station_2", "Station_3", "Station_4"]


# --------------------------- Save Data ------------------ #
def save():
    station = clicked.get()
    temp = temperature_entry.get()
    res = resistance_entry.get()
    stress = surface_stress_entry.get()
    new_data = {
        station: {
            "Temperature": temp,
            "Resistance": res,
            "Surface_stress": stress,
        }
    }
    if len(station) == 0 or len(temp) == 0 or len(res) == 0:
        messagebox.showinfo(title="Oops", message="Egy mező sem maradhat üresen!!!")
    else:
        # is_ok = messagebox.askokcancel(title=station, message=f"Biztosan a megadott értékeket szeretné menteni?\n"
        #                                                       f"Hőmérséklet: {temp}\nEllenállás: {res}\n"
        #                                                       f"Feszültség: {stress}")
        try:
            with open(f"{station}.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open(f"{station}.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open(f"{station}.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            print(new_data)


# -------------------------- GUI Setup ------------------------------ #
window = Tk()
window.title("Pákahegy ellenőrzőlap")
window.config(padx=50, pady=20)

canvas = Canvas(width=250, height=250)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

# Drop Down menu
clicked = StringVar()
clicked.set("Station_1")
drop_menu = OptionMenu(window, clicked, *STATIONS)
drop_menu.grid(column=0, row=1, columnspan=2)

# Labels
temperature = Label(text="Hőmérséklet: ", font=FONT, pady=10)
temperature.grid(column=0, row=2)

resistance = Label(text="Ellenállás: ", font=FONT, pady=10)
resistance.grid(column=0, row=3)

surface_stress = Label(text="Feszültség: ", font=FONT, pady=10)
surface_stress.grid(column=0, row=4)

# Entries
temperature_entry = Entry(width=10, font=FONT)
temperature_entry.grid(column=1, row=2)
temperature_entry.focus()

resistance_entry = Entry(width=10, font=FONT)
resistance_entry.grid(column=1, row=3)

surface_stress_entry = Entry(width=10, font=FONT)
surface_stress_entry.grid(column=1, row=4)

# Buttons
submit_button = Button(text="Küldés", width=20, font=FONT, command=save)
submit_button.grid(column=0, row=5, columnspan=2)

window.mainloop()
