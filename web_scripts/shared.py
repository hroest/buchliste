
class Buch:
    def __init__(self, dbcols=None): 
        if dbcols:
            self._init_from_db_cols( dbcols )

    def _init_from_db_cols(self, res):
        self.myid     =   res[0]
        self.zimmer   =   res[1]
        self.ort      =   res[2]
        self.spalte   =   res[3]
        self.zeile    =   res[4]
        self.autor    =   res[5]
        self.titel    =   res[6]
        self.sprache  =   res[7]
        self.eigner   =   res[8]
        self.buch_art =   res[9]
        self.autor_firstname    =   res[10]
        self.autor_lastname    =   res[11]

    def read_object(self, other):
        self.zimmer   =  other.zimmer      
        self.ort      =  other.ort      
        self.spalte   =  other.spalte   
        self.zeile    =  other.zeile    
        self.autor    =  other.autor    
        self.titel    =  other.titel    
        self.sprache  =  other.sprache  
        self.eigner   =  other.eigner   
        self.buch_art =  other.buch_art 
        self.autor_firstname    =  other.autor_firstname
        self.autor_lastname    =  other.autor_lastname

    def read_form(self, form):
        self.zimmer   =       form.getvalue('zimmer'  )
        self.ort      =       form.getvalue('ort'     )
        self.spalte   =   int(form.getvalue('spalte'  ))
        self.zeile    =   int(form.getvalue('zeile'   ))
        self.autor    =       form.getvalue('autor'   )
        self.titel    =       form.getvalue('titel'   )
        self.sprache  =   int(form.getvalue('sprache' ))
        self.eigner   =       form.getvalue('eigner'  )
        self.buch_art =       form.getvalue('buch_art')
        self.autor_firstname    =       form.getvalue('autor_firstname'   )
        self.autor_lastname    =       form.getvalue('autor_lastname'   )
        if self.autor_firstname is None: self.autor_firstname = ''

    def read_db(self, db, myid):
        c = db.cursor()
        query = """select
        id, zimmer, ort, spalte, zeile, 
        autor, titel , sprache , eigner , buch_art ,
        autor_firstname, autor_lastname
        from buch.buch where id  = %s""" % myid 
        c.execute( query )
        res = c.fetchone()
        self._init_from_db_cols( res )

    def create(self, db):
        c = db.cursor()
        query = """INSERT INTO buch.buch 
        (zimmer, ort, spalte , zeile , titel , sprache , eigner , 
        buch_art, autor_firstname, autor_lastname )
        VALUES ('%s', '%s', %d, %d,  '%s', %d, '%s', '%s', '%s', '%s')
                """ % (
            self.zimmer   ,
            self.ort      ,
            self.spalte   ,
            self.zeile    ,
            #self.autor.replace('"', '\\"').replace("'", "\\'"),
            self.titel.replace('"', '\\"').replace("'", "\\'"),
            self.sprache  ,
            self.eigner   ,
            self.buch_art ,
            self.autor_firstname.replace('"', '\\"').replace("'", "\\'"),
            self.autor_lastname.replace('"', '\\"').replace("'", "\\'"),
                )
        c.execute( query )

    def update(self, db):
        c = db.cursor()
        query = """ UPDATE buch.buch SET 
        zimmer   = '%s',
        ort      = '%s',
        spalte   = '%s',
        zeile    = '%s',
        autor    = '%s',
        titel    = '%s',
        sprache  = '%s',
        eigner   = '%s',
        buch_art = '%s',
        autor_firstname    = '%s',
        autor_lastname    = '%s'
        where id  = %s
                """ % (
            self.zimmer   ,
            self.ort      ,
            self.spalte   ,
            self.zeile    ,
            self.autor.replace('"', '\\"').replace("'", "\\'"),
            self.titel.replace('"', '\\"').replace("'", "\\'"),
            self.sprache  ,
            self.eigner   ,
            self.buch_art ,
            self.autor_firstname.replace('"', '\\"').replace("'", "\\'"),
            self.autor_lastname.replace('"', '\\"').replace("'", "\\'"),
            self.myid 
                )
        #print query
        c.execute( query )

def print_list(mylist):
    print '<table style="text-align:center;">'
    print """<tr >
    <th>Zimmer</th>
    <th>Ort</th>
    <th>Regal</th>
    <th>Tablar</th>
    <th>Autor</th>
    <th>Titel</th>
    <th>Sprache</th>
    <th>Eigner</th>
    <th>Art</th>
    </tr>"""
    for l in mylist:
        print '<tr>'
        print "<td>%s</td>" % l.zimmer
        print "<td>%s</td>" % l.ort
        print "<td>%s</td>" % l.spalte
        print "<td>%s</td>" % l.zeile
        print "<td style='text-align:left;border-left:10px solid white'>%s</td>" % (l.autor_lastname + ', ' + l.autor_firstname )
        print "<td style='text-align:left;border-left:10px solid white'>%s</td>" % l.titel
        print "<td>%s</td>" % get_lang(l.sprache)
        print "<td>%s</td>" % l.eigner
        print "<td>%s</td>" % l.buch_art
        print "<td> <a href='edit.py?id=%s'>edit</a> </td>" % l.myid
        print "</tr>" 

    print "</table>"


def get_types_print(db):
    s = ''
    types = get_types(db)
    for t in types:
        s += t + ', '
    result =  '(%s)' % s[:-2]
    return result

def get_types(db):
    cursor = db.cursor()
    cursor.execute( "select distinct buch_art from buch.buch")
    return [r[0] for r in cursor.fetchall()]


def get_lang(sp):
    lang_dic = {
      0 : 'other',

      1 : 'de',
      2 : 'en',
      3 : 'fr',
      4 : 'sp',
      5 : 'sw',
      6 : 'altdeutsch',
      7 : 'de/en',
      8 : 'de/fr',
      9 : 'it'
    }
    return lang_dic[sp]


def number_books(db):
    cursor = db.cursor()
    cursor.execute( "select count(*) from buch.buch")
    return cursor.fetchone()
