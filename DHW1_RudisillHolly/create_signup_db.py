# Holly Rudisill
# 11/10/2026
# DHW1
# create a table and user database using sql in python. 


import sqlite3

# Connect to SQLite database file (creates file if it doesn't exist)
conn = sqlite3.connect("signup_hw.db")
cursor = conn.cursor()

# Drop table so script can be re-run cleanly in class
cursor.execute("DROP TABLE IF EXISTS users")

# STUDENT CODE GOES IN THIS SECTION ONLY!!!
#--------------------------------------------------------------------------------------
# STEP 1: Create users table
# TO DO: Create a table called users with fields
# user_id, first_name, last_name, email, username, password_hash, signup_date, country, age
# I have started the table for you with the primary key 'user_id'
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NON NULL UNIQUE,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    signup_date TEXT NOT NULL,
    country TEXT NOT NULL,
    age INTEGER    
)""")

# STEP 2: Insert sample fake users
# TO DO: Create a list called users that will store all 10 of your fake users information.
# I have started it for you

users = [ (101, "Purl", "Skeinson", "purl.skeinson@example.com", "purl_knits", "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f", "2024-01-15", "USA", 28),
    (102, "Hank", "Spinster", "hank.s@example.com", "hank_of_yarn", "c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2", "2024-02-10", "Canada", 34),
    (103, "Origami", "Folder", "origami.folder@example.com", "paper_crane99", "39d5622df3b6510ee4fb4084f333eb5a4847e30d1aa5610cfb3f9d504505cc98", "2024-03-05", "Mexico", 25),
    (104, "Rowan", "Caston", "rowan.caston@example.com", "rowan_knitting", "47649568fb8d02df0b6a7102e1c9e83ec903cb6858e8ec434407b4612d4db994", "2024-04-12", "UK", 41),
    (105, "Amigurumi", "Stitcher", "ami.stitcher@example.com", "crochet_crew", "c066e2cde57c430e32ef74900746973e6d817454f767851940954b0c25fc49c8", "2024-05-18", "Australia", 29),
    (106, "Tension", "Gauge", "tension.gauge@example.com", "perfect_gauge", "8f5bc65120a113d5cfbf4ec1a810d7a22fc94b9ff3f3d790d5bc5156a59bc655", "2024-06-22", "USA", 32),
    (107, "Senbazuru", "Kami", "senbazuru.k@example.com", "1000_cranes", "a9ec2b12368c857849e7b231eb93a8d11e51b14ea1379ec8f38ffb61fb73b98c", "2024-07-01", "Spain", 23),
    (108, "Bobbin", "Weaver", "bobbin.weaver@example.com", "bobbin_along", "29432d00c436b75c829e1eb13c18b7617b0d2d34a41031d279cf3291244ab772", "2024-08-14", "USA", 37),
    (109, "Heather", "Heckle", "heather.h@example.com", "heather_yarns", "823d4ee7111352a9261fbfa0e439ca6bb46d299496fb10b3ef1fb63df7e73d32", "2024-09-19", "New Zealand", 26),
    (110, "Cable", "Ribbing", "cable.ribbing@example.com", "cable_knit_life", "11b15cb26efbf01384073d744b3602d334544d673f8ed0469b82bf9c836ecba9", "2024-10-30", "Germany", 30),]


#------------------------------------------------------------------------------------
# DO NOT CODE PASS HERE!!!
# STEP 3: Run the python script! Once your done creating your table and adding in the user information
# You should run the program and it will create your database called signup_hw.db.
# You can then view it in your terminal and you can upload the .db file to a database viewer thats provided on Canvas.

cursor.executemany("""
INSERT INTO users (
    user_id, first_name, last_name, email, username, password_hash,
    signup_date, country, age
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", users)

conn.commit()
conn.close()

print("✅ signup_hw.db created with users table and sample data.")

print()

conn = sqlite3.connect("signup_hw.db")
cur = conn.cursor()
for row in cur.execute("SELECT * FROM users LIMIT 10"):
    print(row)
conn.close()