# import cx_Oracle
#
# con = cx_Oracle.connect("hr", 'hr', cx_Oracle.makedsn('localhost', 1521, 'orcl'))
#
# # con = cx_Oracle.connect("hr", "hr", "localhost/orcl")
#
# cursor = con.cursor()
#
# cursor.execute("""select * from employees""")
#
# for title in cursor:
#     print(title)

import os
import cx_Oracle
os.chdir('C:\\instantclient-basic-nt-11.2.0.4.0\\instantclient_11_2')
os.putenv('NLS_LANG', 'AMERICAN_AMERICA.UTF8')

db = cx_Oracle.connect('hr', 'hr', '192.168.219.124:1521/xe')

print('{}'.format(db.version))

sql = 'select * from employees'
cursor = db.cursor()
cursor.execute(sql)

for row in cursor:
    print(row)

cursor.close()
db.close()
