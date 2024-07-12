import tkinter as tk
import random
#import tksvg

def update_ui():
    
    root.after(1000, update_ui)

def rand3000(upperlimit):
    return str(random.randint(0, upperlimit))

def small_Widget(sensor, measure, reihe, saule, Photo):
    Frame = tk.Frame(root, pady=10)#, padx=10
    Frame.grid(row = reihe, column = saule)#, padx = 3, pady = 3
    Frame.config(bg = "#1A1A1A")
    Image = tk.PhotoImage(file = "Images/" + Photo)
    Label = tk.Label(Frame, text=sensor + measure, width=15, height=1, bg = "#1A1A1A", font=("Helvetica", 20), fg="white").grid(row=0)
    ImageLabel = tk.Label(Frame, image=Image, width=100, height=100).grid(row=1)

def medium_Widget(sensor, measure, reihe, saule, Photo):
    Frame = tk.Frame(root, pady=10)#, padx=10
    Frame.grid(row = reihe, column = saule)
    Frame.config(bg = "#1A1A1A")
    Label = tk.Label(Frame, text=sensor + measure, width=23, height=1, bg="#1A1A1A", font=("Helvetica", 20), fg="white").grid(row=0)
    Image = tk.PhotoImage(file = "Images/" + Photo)
    ImageLabel = tk.Label(Frame, image=Image, width=100, height=100, bg="blue").grid(row=1)

def Large_widget(sensor, reihe, saule):
    Frame = tk.Frame(root, pady=10)#, padx=10
    Frame.grid(row = reihe, column = saule, columnspan = 5)
    Frame.config(bg = "#1A1A1A")
    if sensor == True:
        anzaige = "Fuga detectada!"
    else:
        anzaige = "Sin fugas"
    Label = tk.Label(Frame, text=anzaige, width=46, height=1, bg="#1A1A1A", font=("Helvetica", 30), fg="white").grid(row=0, column=0)
    Image = tk.PhotoImage(file = "Images/virus-covid-solid.png")
    ImageLabel = tk.Label(Frame, image=Image, width=100, height=100, bg="red").grid(row=1, column=0)

def margins(separation, rand):
    margin = tk.Frame(root)
    margin.grid(row = 0)
    Label = tk.Label(margin, width=separation, bg="black")

# Create the main window
root = tk.Tk()
widthRoot = int(root.winfo_screenwidth())
heightRoot = int(root.winfo_screenheight())
root.geometry(f"{widthRoot}x{heightRoot}")
root.config(bg="black")
root.title("Fluchtlos")
#svg_image = tksvg.SvgImage( file = 'Images/virus-covid-solid.png')
pollutionSensorLabel = rand3000(100)
pollutionFrame = medium_Widget(pollutionSensorLabel, "%", 0, 0, "virus-covid-solid.png")
tempreatureSensorLabel = rand3000(100)
temperatureFrame = medium_Widget(tempreatureSensorLabel, "°", 0, 1, "virus-covid-solid.png")
wargningFrane = Large_widget(True, 0, 2)
tartarSensorLabel = rand3000(100)
tartarFrame = small_Widget(tartarSensorLabel, "mg/L", 1, 0, "virus-covid-solid.png")
waterFlowSensorLabel = rand3000(300)
waterFlowFrame = small_Widget(waterFlowSensorLabel, "L/s", 1, 1, "virus-covid-solid.png")
preassureLabel = rand3000(200)
preassureFrame = small_Widget(preassureLabel, "kg/cm²", 1, 2, "virus-covid-solid.png")
detailsFrame = small_Widget("", "Detalles", 1, 3, "virus-covid-solid.png")


# Start periodic data update
update_ui()

# Start the main event loop
root.mainloop()