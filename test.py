import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# create the Tkinter GUI window
root = tk.Tk()
root.title("Humidity Line Chart")

# create a sample data set of humidity values
humidity_data = [50, 55, 60, 65, 70, 75, 80]

# create a Matplotlib figure and axis
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# plot the humidity data as a line chart
ax.plot(humidity_data)

# set the chart title and axis labels
ax.set_title("Humidity Line Chart")
ax.set_xlabel("Time")
ax.set_ylabel("Humidity")

# create a Tkinter canvas and embed the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# run the Tkinter event loop
root.mainloop()
