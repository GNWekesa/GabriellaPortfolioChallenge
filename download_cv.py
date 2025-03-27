import sqlite3

# Connect to the database
conn = sqlite3.connect("database/portfolio.db")
cursor = conn.cursor()

# Retrieve the CV from the database
cursor.execute("SELECT cv_data FROM cv_table LIMIT 1")
row = cursor.fetchone()

# Ensure data exists before writing
if row and row[0]:
    with open("Gabriella_CV_Download.pdf", "wb") as file:
        file.write(row[0])
    print("✅ CV successfully downloaded as Gabriella_CV_Download.pdf")
else:
    print("⚠️ No CV found in the database.")

# Close the connection
conn.close()
