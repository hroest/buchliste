#!/usr/bin/python
# -*- coding: utf-8  -*-
import cgitb; cgitb.enable()
import MySQLdb, sys
import shared
db = MySQLdb.connect(read_default_file="/home/hroest_admin/.buch.cnf")
cursor = db.cursor()
print "Content-type: text/html; charset=utf-8"
print ""

print "<title>Alle</title>"
cursor.execute( "select * from buch.buch")
mylist = cursor.fetchall()

obj_list = [ shared.Buch(dbcols=col) for col in mylist ]
shared.print_list( obj_list )

print "<hr><a href='index.py'>Zurück</a>"
