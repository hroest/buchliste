#!/usr/bin/python
# -*- coding: utf-8  -*-
import cgitb; cgitb.enable()
import MySQLdb, sys
import cgi
import shared
form = cgi.FieldStorage()  
db = MySQLdb.connect(read_default_file="/home/hroest_admin/.buch.cnf")
cursor = db.cursor()
#print "Content-type: text/html; charset=utf-8"
#print ""

#print "<title>Buch hinzufügen</title>"

if not form.has_key('autor'):
    print "Content-type: text; charset=utf-8"
    print 
    print "ERROR"
    exit()
     
myid = int(form.getvalue('id') )
buch = shared.Buch()
buch.read_db( db, myid )

buch_new = shared.Buch()
buch_new.read_form( form )

buch.read_object( buch_new )
buch.update(db)

print "Location: all.py"
print 
