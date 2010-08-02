#!/usr/bin/python
# -*- coding: utf-8  -*-
print "Content-type: text/html; charset=utf-8"
print ""

import MySQLdb
import shared
db = MySQLdb.connect(read_default_file="/home/hroest_admin/.buch.cnf")
cursor = db.cursor()

print """
<h1>Willkommen</h1> bei der Bücherdatenbank von Hannes und Martina.

<p>
Momentan sind %s Bücher erfasst.
</p>

<ul>
<li> <a href="all.py">List</a> </li>
<li> <a href="add.py">Add</a> </li>
<li> <a href="search.py">Search</a> </li>
</ul>

""" % shared.number_books(db)
