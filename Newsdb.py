import psycopg2

if __name__ == '__main__':
    DBNAME = "news"
    q1 = "select articles.title, logpath.views from (select path, count(*) as views from log where status = '200 OK' and path != '/' group by path) as logpath join articles on logpath.path like concat('%', articles.slug, '%') order by logpath.views desc limit 3;"
    q2 = "select authors.name, sum(logpath.logviews) as views from (select path, count(*) as logviews from log where status = '200 OK' and path != '/' group by path) as logpath join articles on logpath.path like concat('%', articles.slug, '%') join authors on articles.author = authors.id group by authors.name order by views desc;"
    q3 = "select errtotal.time::date, cast(errtotal.error as float) / cast(total.requests as float) * 100 as errors from (select time::date, count(*) as error from log where status = '404 NOT FOUND' group by time::date) as errtotal left join (select time::date, count(*) as requests from log group by time::date) as total on errtotal.time::date = total.time::date where (cast(errtotal.error as float) / cast(total.requests as float) * 100) > 1;"
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    
    c.execute(q1)
    articles = c.fetchall()
    c.execute(q2)
    authors = c.fetchall()
    c.execute(q3)
    errors = c.fetchall()
    db.close()

    print("What are the most popular three articles of all time?\n")
    for x in articles:
        print("{} - {} views".format(x[0], x[1]))

    print("\nWho are the most popular article authors of all time?\n")
    for x in authors:
        print("{} - {} views".format(x[0], x[1]))

    print("\nOn which days did more than 1% of requests lead to errors?\n")
    for x in errors:
        print("{} - {:.2f}% errors".format(x[0], x[1]))

    
    #{}\nWho are the most popular article authors of all time?\n{}\nOn which days did more than 1% of requests lead to errors?\n{}".format(articles, authors, errors))

  

# Question 1 query
#select articles.title, logpath.views from (select path, count(*) as views from log where status = '200 OK' and path != '/' group by path) 
#as logpath join articles on logpath.path like concat('%', articles.slug, '%') order by logpath.views desc limit 3;

# Question 2 query
#select authors.name, sum(logpath.logviews) as views from (select path, count(*) as logviews from log where status = '200 OK' and path != '/' group by path)
#as logpath join articles on logpath.path like concat('%', articles.slug, '%') join authors on articles.author = authors.id
#group by authors.name order by views desc;

# Question 3 query
#select errtotal.time::timestamp::date, cast(errtotal.error as float) / cast(total.requests as float) * 100 as errors
#from (select time::timestamp::date, count(*) as error from log where status = '404 NOT FOUND' group by time::timestamp::date) as errtotal
#left join (select time::timestamp::date, count(*) as requests from log group by time::timestamp::date) as total on errtotal.time::timestamp::date = total.time::timestamp::date
#where (cast(errtotal.error as float) / cast(total.requests as float) * 100) > 1;