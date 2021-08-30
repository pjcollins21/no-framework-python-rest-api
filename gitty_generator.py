#gitty
import sqlite3

"""
Guitar Model:
{
    "gId": INTEGER PRIMARY KEY AUTOINCREMENT
	"mfr": text
	"mdl": text
	"gtype": text
	"puc": text
	"color": text
}
"""

conn = sqlite3.connect('gitty.db')
csr = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS guitars (id INTEGER PRIMARY KEY AUTOINCREMENT, mfr text, mdl text, gtype text, puc text, color text)"
csr.execute(create_table)
q = "UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'guitars'"
csr.execute(q)
conn.commit()

gittys = [
    ["Harley Benton", "CLD-15MCE", "electro-acoustic", "piezo", "dark natural"],
    ["Epiphone", "2013 Nighthawk Special Custom Re-Issue", "electric", "HSH", "honey-burst"],
    ["Schecter", "Custom C1 Exotic: Spalted Maple", "electric", "HH", "natural burst"],
    ["Harley Benton", "ST-90SA", "electric", "SSS", "natural"]
]
for gitty in gittys:
    q = "INSERT INTO guitars (mfr, mdl, gtype, puc, color) VALUES ( ?, ?, ?, ?, ?)"
    csr.execute(q, (*gitty,))
    conn.commit()
conn.close()