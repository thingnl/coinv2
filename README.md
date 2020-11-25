# coins v2
### Second incarnation of Pecuniae Collectio


---
##### Some usefull sqlite stuff
* List all fields for table strike
  - select sql from sqlite_master WHERE name = 'strike';
* List all tables
  - SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';
* List all indixes
  - SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type= 'index';

---
##### Common/dump issues:
* sqlite3.ProgrammingError: Incorrect number of bindings supplied.
  * don not pass a string, but a tuple: cursor.execute('INSERT INTO images VALUES(?)', (img,))
    * Not: cursor.execute('INSERT INTO images VALUES(?)', img)
    * But: cursor.execute('INSERT INTO images VALUES(?)', (img,))


* convert tuple (e.g. from sql) to string:
  * fullname = fullname[0]

---
##### Python functions cheat sheet
* Loop 1 to something: for i in range(0, len(glob.country_data)):
* Insert into tupple: glob.country_data.insert(0,"'*'")

