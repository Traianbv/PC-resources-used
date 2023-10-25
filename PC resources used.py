from tkinter import *
from psutil import virtual_memory, cpu_percent

window = Tk()
window.geometry("400x150")
window.title("CPU Usage")


def show_cpu():
    cpu_usage = cpu_percent(interval=1)
    # print("{}%".format(cpu_usage))
    cpu_show.config(text="{}%".format(cpu_usage), fg="red", font="bold")
    window.after(200, show_cpu)

def convertor_bytes(byte):
    one_giga = 1073741824
    giga = byte / one_giga
    giga = "{0:.2f}".format(giga)
    return giga

def show_ram():
    ram_usage=virtual_memory()
    ram_usage=dict(ram_usage._asdict())
    for key in ram_usage:
        if key != "percent":
            ram_usage[key] = convertor_bytes(ram_usage[key])
    ram_show.config(text="{} GB/ {} GB ({} %)".format(ram_usage["used"], ram_usage["total"], ram_usage["percent"]), fg="red", font="bold")
    ram_show.after(200, show_ram)

title = Label(text="PC Resurce Usage !", font=("Georgia", 15))
title.grid(column=1, row=0, pady=10)

cpu_label = Label(text="CPU Usage: ")
cpu_label.grid(column=0, row=1)

cpu_show = Label(bg="#000000", width=10)
cpu_show.grid(column=1, row=1)

ram_label = Label(text="RAM Usage: ")
ram_label.grid(column=0, row=2, pady=10)

ram_show = Label(bg="#000000", width=25)
ram_show.grid(column=1, row=2)


show_cpu()
show_ram()
window.mainloop()