import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
'Server=LAPTOP-EM4ODK5N;'
'Database=test;'
'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM test.dbo.Movies')

for row in cursor:
    print(row)
