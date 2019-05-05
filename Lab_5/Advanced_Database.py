import sqlite3
conn = sqlite3.connect('db1')
c = conn.cursor()

print("What species are in the database?")
c.execute("SELECT name FROM species")
names = c.fetchall()
print(names)

print("\nHow many proteins from each species are present in the database?")
c.execute("SELECT COUNT(species),name FROM protein t1 INNER JOIN species t2 ON t1.species = t2.abbrev GROUP BY name")
result = c.fetchall()
print(result)

for row in c:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}'.format(row[0], row[1]))

# Adding Sus scrofa again
c.execute("INSERT INTO species(abbrev, name, common) VALUES ('Ss','Sus scrofa','Wild boar')")

print("\nWhat proteins are longer than 1000 aa?")
c.execute('''SELECT accession FROM protein WHERE length("sequence")>1000''')
accessions = []
for row in c:
	accessions.append(row[0])
print(accessions)

# Adding information about the method
#c.execute('''ALTER TABLE protein ADD method character varying(20)''')

print("\nWhat species are present in family NHR3?")
c.execute('''SELECT common FROM species WHERE abbrev IN (SELECT species FROM protein t1 INNER JOIN familymembers t2 ON t1.accession = t2.protein WHERE t2.family="NHR3")''')
nh3=c.fetchall()
print(nh3)

