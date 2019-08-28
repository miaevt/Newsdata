# Newsdb
Newsdb is a reporting tool that outputs the following information regarding user activity stored in the newsdata database:
    
    - Three most popular articles of all time
    - Most popular article authors of all time
    - Days with more than 1% of error requests
    
#### Requirements
    - Python 3
    - PostgreSQL
    - newsdata.sql

#### View Statements
```
create view logpath as select path, count(*) as views from log where status = '200 OK' and path != '/' group by path;
```
```
create view error as select time::date, count(*) as total from log where status = '404 NOT FOUND' group by time::date;
```
```
create view total as select time::date, count(*) as requests from log group by time::date;
```

#### Get Started
Before running the Python code, execute the view statements listed in the "View Statements" section above.

Use this command to run the code:
```
python newsdb.py
```
