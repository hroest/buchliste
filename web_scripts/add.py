#!/usr/bin/python
# -*- coding: utf-8  -*-
import cgitb; cgitb.enable()
import MySQLdb, sys
import cgi
form = cgi.FieldStorage()  
db = MySQLdb.connect(read_default_file="/home/hroest_admin/.buch.cnf")
cursor = db.cursor()
print "Content-type: text/html; charset=utf-8"
print ""

print "<title>Buch hinzufügen</title>"


print """
<FORM action="create.py" method="get">

    <p>
    <label for="zimmer">Zimmer</label>
    <input type="text" name="zimmer" value=""> 
    </p>

    <p>
    <label for="ort">Ort</label>
    <input type="text" name="ort" value=""> 
    </p>

    <p>
    <label for="spalte">Spalte</label>
    <input type="text" name="spalte" value=""> 
    </p>

    <p>
    <label for="zeile">Zeile</label>
    <input type="text" name="zeile" value=""> 
    </p>

    <p>
    <label for="autor">Autor</label>
    <input type="text" name="autor" value=""> 
    </p>

    <p>
    <label for="titel">Titel</label>
    <input type="text" name="titel" value=""> 
    </p>

    <p>
    <label for="sprache">Sprache</label>
    <input type="text" name="sprache" value=""> 
    de = 1
    en = 2
    fr = 3
    sp = 4
    sw = 5
    altdeutsch = 6
    de/en = 7
    de/fr=8
    </p>

    <p>
    <label for="eigner">Eigner</label>
    <input type="text" name="eigner" value=""> 
    </p>

    <p>
    <label for="buch_art">Art des Buches</label>
    <input type="text" name="buch_art" value=""> 
    </p>

    <INPUT type="submit" value="Abschicken"> 
</FORM>
"""

print "<hr><a href='index.py'>Zurück</a>"
