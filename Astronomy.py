import sqlite3
import tkinter as tk

# Connect to the database
conn = sqlite3.connect('astronomy.db')

# Create a function to search for an object in the database


def search_object():
    # Get the object name from the entry widget
    object_name = object_name_entry.get()

    # Execute a SELECT statement to search for the object name in the database
    c = conn.cursor()
    c.execute("SELECT * FROM objects WHERE name=?", (object_name,))
    object_data = c.fetchone()

    # Check if the object was found
    if object_data is None:
        result_label.config(text="Sorry, the object was not found in the database.")
    else:
        # Print the object information
        name, mass, diameter, density, gravity, escape_velocity, rotation_period, length_of_day, distance_from_sun, orbital_period, orbital_velocity, moons, ring_system, global_magnetic_field, about =object_data
        name, type, distance, diameter, mass = object_data
        result_label.config(text=f"Name: {name}\nMass (10^24 kg): {mass}\nDiameter (km): {diameter}\nDensity (kg/m^3): {density}\nGravity (m/s^2): {gravity}\nEscape Velocity (km/s): {escape_velocity}\nRotation Period (hours):{rotation_period}\nLength of Day (hours):{length_of_day}\nDistance from Sun (10^6 km):{distance_from_sun}\nOrbital Period (days):{orbital_period}\nOrbital Velocity (km/s):{orbital_velocity}\nNumber of Moons:{moons}\nRing System?:{ring_system}\nGlobal Magnetic Field?:{global_magnetic_field}\nAbout:{about}")

# Create the GUI window
root = tk.Tk()
root.title("Astronomy Object Search")
root.geometry("1400x700")

# Create the object name label and entry widget
object_name_label = tk.Label(root, text="Enter the name of the astronomical object:")
object_name_label.pack()
object_name_entry = tk.Entry(root, width=130, borderwidth=3)
object_name_entry.pack()

# Create the search button
search_button = tk.Button(root, text="Search", command=search_object)
search_button.pack()

# Create the result label to display the object information
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI loop
root.mainloop()

# Close the database connection
conn.close()
