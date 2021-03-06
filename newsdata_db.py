# "Database code" for the Logs Analysis Project.

import psycopg2

DBNAME = "news"


def query(sql_select_statement):
    """Return result of given SQL statement"""
    conn = None
    resultset = None
    if sql_select_statement is not None:
        try:
            # connect to PostgreSQL database
            conn = psycopg2.connect(database=DBNAME)
            # create new cursor
            cur = conn.cursor()
            # execute SELECT statement
            cur.execute(sql_select_statement)
            # fetch all rows
            resultset = cur.fetchall()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            # close connection
            if conn is not None:
                conn.close()

    return resultset


def get_top_articles():
    """Most popular three articles of all time"""
    sql = """SELECT articles.title, COUNT(*) AS views
                FROM articles, log
                WHERE log.path = '/article/' || articles.slug
                GROUP BY articles.title
                ORDER BY views DESC
                LIMIT 3;"""
    return query(sql)


def get_top_authors():
    """Most popular article authors of all time"""
    sql = """SELECT authors.name, COUNT(*) AS views
                FROM authors, articles, log
                WHERE authors.id = articles.author
                    AND log.path = '/article/' || articles.slug
                GROUP BY authors.name
                ORDER BY views DESC;"""
    return query(sql)


def get_days_of_error():
    """Days with more than 1% of requests which lead to errors"""
    sql = """SELECT TO_CHAR(r.h_date, 'FMMonth FMDD, YYYY'), r.percent FROM
        (
          SELECT tmp.h_date, tmp.total, tmp.error,
            ROUND( 100 * (
                CAST(tmp.error AS DECIMAL) / tmp.total
                ), 2) AS percent FROM
            (
              SELECT DATE(time) AS h_date,
                COUNT(*) AS total,
                SUM( CASE WHEN status != '200 OK' THEN 1 ELSE 0 END ) AS error
                FROM log
              GROUP BY h_date
            ) AS tmp
        ) AS r
        WHERE r.percent > 1
        ORDER BY r.percent DESC;"""
    return query(sql)
