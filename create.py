#!/usr/bin/python
# -*- coding: utf-8  -*-
import cgitb; cgitb.enable()
import MySQLdb, sys
import cgi
import shared
form = cgi.FieldStorage()  
db = MySQLdb.connect(read_default_file="/home/hroest_admin/.buch.cnf")
cursor = db.cursor()


if not form.has_key('autor'):
    print "ERROR"
    exit()
     
buch = shared.Buch()
buch.read_form( form )
buch.create(db)

print "Location: all.py"
print 
