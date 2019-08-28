#!/usr/bin/env python3

import psycopg2

if __name__ == '__main__':
    DBNAME = "news"
    q1 = "select articles.title, logpath.views from logpath join articles on logpath.path like concat('%', articles.slug, '%') order by logpath.views desc limit 3;"
    q2 = """select authors.name, sum(logpath.views) as views from logpath
    join articles on logpath.path like concat('%', articles.slug, '%')
    join authors on articles.author = authors.id
    group by authors.name order by views desc;"""
    q3 = """select errtotal.time::date, cast(errtotal.error as float) / cast(total.requests as float) * 100 as errors
    from errtotal left join total on errtotal.time::date = total.time::date
    where (cast(errtotal.error as float) / cast(total.requests as float) * 100) > 1;"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    
    # Executes each query
    c.execute(q1)
    articles = c.fetchall()
    c.execute(q2)
    authors = c.fetchall()
    c.execute(q3)
    errors = c.fetchall()
    db.close()

    # Prints out formatted results
    print("Three most popular articles of all time:\n")
    for x in articles:
        print("{} - {} views".format(x[0], x[1]))

    print("\nMost popular article authors of all time:\n")
    for x in authors:
        print("{} - {} views".format(x[0], x[1]))

    print("\nDays with more than 1% of error requests:\n")
    for x in errors:
        print("{} - {:.2f}% errors".format(x[0].strftime("%B %d, %Y"), x[1]))