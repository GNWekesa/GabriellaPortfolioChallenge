import sqlite3

# Connect to the database
conn = sqlite3.connect("database/portfolio.db")
cursor = conn.cursor()

# Read the CV file in binary mode
with open("cv_files/Gabriella_CV.pdf", "rb") as file:
    cv_data = file.read()

# Insert the binary data into the database
cursor.execute("INSERT INTO cv_table (cv_data) VALUES (?)", (cv_data,))
conn.commit()

print("✅ CV successfully uploaded to database.")

# Close connection
conn.close()
