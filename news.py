#!/usr/bin/env python

import psycopg2
import datetime

DBNAME = "news"


def get_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("SELECT art.title, COUNT(log.path) as count FROM log \
            INNER JOIN articles as art on ('/article/' || art.slug) = log.path\
            WHERE log.path != '/' GROUP BY log.path, art.title \
            ORDER BY COUNT(log.path) DESC LIMIT 3")
    c.execute(query)
    return c.fetchall()
    db.close()


def display_articles(x):
    articles = x
    for article in articles:
        print('"' + article[0] + '" - ' + str(article[1]) + ' views')


def get_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("SELECT auth.name, COUNT(art.author) as count FROM log \
            INNER JOIN articles as art on ('/article/' || art.slug) = log.path\
            INNER JOIN authors as auth on art.author = auth.id \
            WHERE log.path != '/' GROUP BY art.author, auth.name \
            ORDER BY COUNT(art.author) DESC")
    c.execute(query)
    return c.fetchall()
    db.close()


def display_authors(x):
    authors = x
    for author in authors:
        print(author[0] + ' - ' + str(author[1]) + ' views')


def get_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("SELECT t1.date, ((t1.count * 100) / t2.count) as percentage \
            FROM (SELECT date(time) as date, COUNT(status) as count \
            FROM log WHERE status LIKE '%4%' GROUP BY date(time)) as t1, \
            (SELECT date(time) as date, COUNT(status) as count \
            FROM log GROUP BY date(time)) as t2 \
            WHERE t1.date = t2.date and ((t1.count * 100) / t2.count) > 1")
    c.execute(query)
    return c.fetchall()
    db.close()


def display_error(x):
    error_days = x
    for error_day in error_days:
        year = error_day[0].year
        month = datetime.date(1900, error_day[0].month, 1).strftime('%B')
        day = error_day[0].day
        print(month + ' ' + str(day) + ', ' + str(year) +
              ' - ' + str(error_day[1]) + '% errors')


print "The Most Popular Three Articles of All Time:"
display_articles(get_articles())

print "\nThe Most Popular Article Authors of All Time:"
display_authors(get_authors())

print "\nDays With More Than 1% of Requests Lead to Errors:"
display_error(get_errors())
