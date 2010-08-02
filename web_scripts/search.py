#!/usr/bin/python
# -*- coding: utf-8  -*-
import cgitb; cgitb.enable()
import MySQLdb, sys
import cgi
import shared
form = cgi.FieldStorage()  
db = MySQLdb.connect(read_default_file="/home/hroest_admin/.buch.cnf")
cursor = db.cursor()
print "Content-type: text/html; charset=utf-8"
print ""


print "<title>Suche</title>"


print """
<FORM action="search.py" method="get">
    <p>
    <label for="autor">Autor</label>
    <input type="text" name="autor" value=""> 
    <label for="title">Titel</label>
    <input type="text" name="title" value=""> 
    </p>
    <INPUT type="submit" value="Abschicken"> 
</FORM>
Momentan kann man nur ENTWEDER nach Autor ODER nach Titel suchen.
"""

if form.has_key('autor'):
    cursor.execute( "select * from buch.buch where autor like '%%%s%%'" % form.getvalue('autor') )
    mylist = cursor.fetchall()
elif form.has_key('title'):
    cursor.execute( "select * from buch.buch where titel like '%%%s%%'" % form.getvalue('title') )
    mylist = cursor.fetchall()
else:
    print "<hr><a href='index.py'>Zurück</a>"
    exit()


obj_list = [ shared.Buch(dbcols=col) for col in mylist ]
shared.print_list( obj_list )

print "<hr><a href='index.py'>Zurück</a>"
