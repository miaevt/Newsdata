# NewsDB
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
    
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
    
## Requirements
- Python 3
- PostgreSQL
- newsdata.sql (see set-up instructions below)

## Set-up Instructions
1.  Create the news database in PostgreSQL
    - From the command line, launch the psql console by typing: ```psql```
    - Check to see if a news database already exists by listing all databases with the command: ```\l```
    - If a news database already exists, drop it with the command: ```DROP DATABASE news;```
    - Create the news database with the command: ```CREATE DATABASE news;```
    - Exit the console by typing: ```\q```
2.  Download the schema and data for the news database:
    - [Click here to download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3.  Unzip the downloaded file, newsdata.zip.
    - You should now have an sql script called *newsdata.sql*.
4.  From the command line, navigate to the directory containing *newsdata.sql*.
5.  Import the schema and data in *newsdata.sql* to the news database by typing: ```psql -d news -f newsdata.sql```

## View Statements
```sql
CREATE VIEW logpath AS
SELECT path, count(*) AS views
FROM log
WHERE status = '200 OK'
AND path != '/'
GROUP BY path;
```
```sql
CREATE VIEW error AS
SELECT time::date, count(*) AS total
FROM log WHERE status = '404 NOT FOUND'
GROUP BY time::date;
```
```sql
CREATE VIEW total AS
SELECT time::date, count(*) AS requests
FROM log
GROUP BY time::date;
```

## Get Started
Before running the Python code, execute the view statements listed in the "View Statements" section above.

Use this command to run the code:
```
python newsdb.py
```
