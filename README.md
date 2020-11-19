# coins v2
### Second incarnation of Pecuniae Collectio


---
##### Some usefull sql stuff
* List all fields for table strike
  - select sql from sqlite_master WHERE name = 'strike';
* List all tables
  - SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';
* List all indixes
  - SELECT type, name, tbl_name, sql FROM sqlite_master WHERE type= 'index';

---
