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


print "<title>Buch hinzufügen</title>"

if not form.has_key('id'):
    exit()


myid = int(form.getvalue('id') )
buch = shared.Buch()
buch.read_db( db, myid)

print """
<FORM action="update.py" method="get">

    <p>
    <label for="zimmer">Zimmer</label>
    <input type="text" name="zimmer" value="%s"> 
    </p>

    <p>
    <label for="ort">Ort</label>
    <input type="text" name="ort" value="%s"> 
    </p>

    <p>
    <label for="spalte">Spalte</label>
    <input type="text" name="spalte" value="%s"> 
    </p>

    <p>
    <label for="zeile">Zeile</label>
    <input type="text" name="zeile" value="%s"> 
    </p>

    <p>
    <label for="autor">Autor</label>
    <input type="text" name="autor" value="%s"> 
    </p>

    <p>
    <label for="titel">Titel</label>
    <input type="text" name="titel" value="%s"> 
    </p>

    <p>
    <label for="sprache">Sprache</label>
    <input type="text" name="sprache" value="%s"> 
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
    <input type="text" name="eigner" value="%s"> 
    </p>

    <p>
    <label for="buch_art">Art des Buches</label>
    <input type="text" name="buch_art" value="%s"> 
    </p>

    <input type="hidden" id="id" name="id" value="%s" />

    <INPUT type="submit" value="Abschicken"> 
</FORM>
                """ % (
            buch.zimmer   ,
            buch.ort      ,
            buch.spalte   ,
            buch.zeile    ,
            buch.autor    ,
            buch.titel    ,
            buch.sprache  ,
            buch.eigner   ,
            buch.buch_art ,
            buch.myid 
                )

