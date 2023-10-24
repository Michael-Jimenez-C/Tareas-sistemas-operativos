import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root=tk.Tk()

# Create a Matplotlib figure object
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Plot the graph on the subplot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y)

# Create a Tkinter canvas object and embed the figure in it
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Pack the canvas object into the Tkinter window
canvas.get_tk_widget().pack()


x = [1, 2, 3, 4, 5]
y = [3, 4, 7, 0, 20]
ax.plot(x, y)

# Create a Tkinter canvas object and embed the figure in it
canvas.figure=fig
canvas.draw()

root.mainloop()