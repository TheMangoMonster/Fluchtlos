import tkinter as tk
import random

def update_ui():
    
    root.after(1000, update_ui)

def rand3000(upperlimit):
    return str(random.randint(0, upperlimit))

def small_Widget(sensor, measure, reihe, saule):
    Frame = tk.Frame(root, pady=10)#, padx=10
    Frame.grid(row = reihe, column = saule)#, padx = 3, pady = 3
    Frame.config(bg = "#1A1A1A")
    Label = tk.Label(Frame, text=sensor + measure, width=15, height=1, bg = "#1A1A1A", font=("Helvetica", 20), fg="white").grid(row=0)

def medium_Widget(sensor, measure, reihe, saule):
    Frame = tk.Frame(root, pady=10)#, padx=10
    Frame.grid(row = reihe, column = saule)
    Frame.config(bg = "#1A1A1A")
    Label = tk.Label(Frame, text=sensor + measure, width=23, height=1, bg="#1A1A1A", font=("Helvetica", 20), fg="white").grid(row=0)

def Large_widget(sensor, reihe, saule):
    Frame = tk.Frame(root, pady=10)#, padx=10
    Frame.grid(row = reihe, column = saule, columnspan = 5)
    Frame.config(bg = "#1A1A1A")
    if sensor == True:
        anzaige = "Fuga detectada!"
    else:
        anzaige = "Sin fugas"
    Label = tk.Label(Frame, text=anzaige, width=46, height=1, bg="#1A1A1A", font=("Helvetica", 30), fg="white").grid(row=0, column=0)

# Create the main window
root = tk.Tk()
widthRoot = int(root.winfo_screenwidth())
heightRoot = int(root.winfo_screenheight())
root.geometry(f"{widthRoot}x{heightRoot}")
root.config(bg="#f0f0f0")
root.title("Fluchtlos")
pollutionSensorLabel = rand3000(100)
pollutionFrame = medium_Widget(pollutionSensorLabel, "%", 0, 0)
pollutionImage = tk.PhotoImage(file="Images/pollution.png")
pollutionLabel = tk.Label(pollutionFrame, image=pollutionImage).grid(row = 1, column = 0)
tempreatureSensorLabel = rand3000(100)
temperatureFrame = medium_Widget(tempreatureSensorLabel, "°", 0, 1)
temperatureImage = tk.PhotoImage(file="Images/temperature.png")
temperatureLabel = tk.Label(temperatureFrame, image=temperatureImage).grid(row = 1, column = 1)
waringSensor = random.choice([True, False])
warningFrame = Large_widget(waringSensor, 0, 2)
waringImage = tk.PhotoImage(file="Images/warning.png")
warningLabel = tk.Label(warningFrame, image=waringImage).grid(row = 1, column = 2)
tartarSensorLabel = rand3000(100)
tartarFrame = small_Widget(tartarSensorLabel, "mg/L", 2, 0)
pressureLabel = tk.Label(tartarFrame, text="Salinidad", font=("Helvetica", 30)).grid(row=3, column=0)
waterFlowSensorLabel = rand3000(300)
waterFlowFrame = small_Widget(waterFlowSensorLabel, "L/s", 2, 1)
waterFlowImage = tk.PhotoImage(file="Images/drop.png")
waterFlowLabel = tk.Label(waterFlowFrame, image=waterFlowImage).grid(row=3, column=1)
preassureSensorLabel = rand3000(200)
preassureFrame = small_Widget(preassureSensorLabel, "kg/cm²", 2, 2)
pressureLabel = tk.Label(preassureFrame, text="Presion del agua", font=("Helvetica", 30)).grid(row=3, column=2)
detailsFrame = small_Widget("", "Detalles", 2, 3)
detailsImage = tk.PhotoImage(file="Images/details.png")
detailsLabel = tk.Label(detailsFrame, image=detailsImage).grid(row=3, column=3)


# Start periodic data update
update_ui()

# Start the main event loop
root.mainloop()