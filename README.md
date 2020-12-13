# coins v2
### Second incarnation of Pecuniae Collectio

---
Pecuniae Collectio is build with and for the following reasons:
  - The initial PC version was build as a Proof of Concept. It was never finished to a usable level.
  - No existing coin collection application actually works or allows to be used in the way I want to maintain my coin collection administration.
  - I wrote several Python packages in the past, but never something that is GUI based. So this is a learning experience for me.
  - PC is writen with Windows in mind. It might or might not work on different OS'es. If you want to test, that's great, let me know the results. 
  - PC is written and tested with Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) 


---
##### Python install
* Upgrade pip
  - c:\python\python39\python.exe -m pip install --upgrade pip
* List packages
  - pip list (Is depending on the environment!)
* Install PIL
  - pip install pillow


---
##### Multi Language stuff
* C:\>py -3.4 C:\Python34\Tools\i18n\pygettext.py -d guess guess.py
* python C:\Python\Python39\Tools\i18n\pygettext.py --extract-all --default-domain=main --output-dir=locales main_window.py
* python C:\Python\Python39\Tools\i18n\pygettext.py -v -d base -o locales/base.pot main_window.py


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


---
##### Pycharm settings
* Custom tags
  * In the Settings/Preferences dialog Ctrl+Alt+S, select Editor | TODO.