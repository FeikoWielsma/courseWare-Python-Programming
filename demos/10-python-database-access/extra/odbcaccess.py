import pyodbc

cnxn = pyodbc.connect("DSN=test;PWD=password")
cursor = cnxn.cursor()


# DBfile = '/data/MSAccess/Music_Library.mdb'
# conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
# cursor = conn.cursor()
#
# SQL = 'SELECT Artist, AlbumName FROM RecordCollection ORDER BY Year;'
# for row in cursor.execute(SQL): # cursors are iterable
#    print row.Artist, row.AlbumName
#
# cursor.close()
# conn.close()
