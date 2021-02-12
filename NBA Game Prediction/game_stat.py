import pandas as pd
import numpy as np
import csv, sqlite3



con = sqlite3.connect("city.db")
cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


cursor.execute('''SELECT * FROM c;''')

rows = cursor.fetchall()
 
for row in rows:
	print(row)
			 
#commit the changes to db			
con.commit()
#close the connection
con.close()