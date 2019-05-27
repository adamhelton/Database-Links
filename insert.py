import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
'Server='Insert Server NAme Here;'
'Database=test;'
'Trusted_Connection=yes;')

cursor=conn.cursor()
cursor.execute('SELECT * FROM Name of Database')
cursor.execute('''
    INSERT INTO Test.dbo.Movies (Title, Director_FirstName, Director_LastName, Genre, Star_FirstName, Star_LastName, Rating, Producer_FirstName, Producer_LastName)
    VALUES
    ('Test', 'John', 'Smith', 'Drama', 'Eric', 'Doe', 8, 'Hellen', 'Jones'),
    ('Second', 'Hellen', 'Jones', 'Drama', 'John', 'Smith', 9, 'Eric', 'Doe')
''')

conn.commit()
