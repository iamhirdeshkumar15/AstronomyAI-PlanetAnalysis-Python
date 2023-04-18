import sqlite3

# Create a connection to the database file (will create the file if it doesn't exist)
conn = sqlite3.connect('astronomy.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create the objects table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS objects(
        name text, mass real, diameter real, density real,
        gravity real, escape_velocity real, rotation_period real,
        length_of_day real, distance_from_sun real, orbital_period real,
        orbital_velocity real, moons integer, ring_system text,
        global_magnetic_field text, about Text)''')

# Insert some sample data into the objects table
c.execute("INSERT INTO objects VALUES ('Mercury', 0.330, 4879, 5427, 3.7, 4.3, 1407.6, 4222.6, 57.9, 88.0, 47.4, 0, 'No', 'Yes', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Venus', 4.87, 12104, 5243, 8.9, 10.4, -5832.5, 2802.0, 108.2, 224.7, 35.0, 0, 'No', 'No', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Earth', 5.97, 12756, 5514, 9.8, 11.2, 23.9, 24.0, 149.6, 365.2, 29.8, 1, 'No', 'Yes', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Mars', 0.642, 6792, 3933, 3.7, 5.0, 24.6, 24.7, 227.9, 687.0, 24.1, 2, 'No', 'No', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Jupiter', 1898, 142984, 1326, 23.1, 59.5, 9.9, 9.9, 778.6, 4331, 13.1, 79, 'Yes', 'Yes', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Saturn', 568, 120536, 687, 9.0, 35.5, 10.7, 10.7, 1433.5, 10747, 9.7, 82, 'Yes', 'Yes', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Uranus', 86.8, 51118, 1271, 8.7, 21.3, -17.2, 17.2, 2872.5, 30589, 6.8, 27, 'Yes', 'Yes', 'hello world')")
c.execute("INSERT INTO objects VALUES ('Neptune', 102, 49528, 1638, 11.0, 23.5, 16.1, 16.1, 4495.1, 59800, 5.4, 14, 'Yes', 'Yes', 'hello world')")


# Commit the changes and close the connection
conn.commit()
conn.close()
