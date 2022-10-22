# NHIS-HMO-Record-Keeper
![alt text](/shot1.png?raw=true)
## This is one of my very first projects written many years ago.
## Many of the programming approach in this work is totally erronous and I have not had time to rewrite the program.
## I hope this will in some way help those who starting to explore python tkinter and sqlite3.

This is a windows application.
The app performs basic CRUD operation with python, tkinter and sqlite3.

The app:
-- records HMOs
-- records hospital patients as either 
    -- principal (main record holder)
    -- spouse
    -- children
    -- extra
    -- dependant
-- registers hospital services and their price
-- registers drugs purchased by hospital and their price

The records are shown on the right and can be update and deleted


### Backend - python, sqlite3
### Frontend - tkinter (python)

```diff
- Note: The code will break without the database file (in same path as addrecord.py);  
that is because I did not ask the tables to create if not exists.

- I leave that to anyone interested to fix, I believe it's a small one
```

```diff
! NHIS: National Health Insurance Scheme
! HMO: Health Management Organization
```


