import newsdata_db


# plain text template for an individual log result
TOP_ARTICLES = '''"%s" - %s views'''

TOP_AUTHORS = '''%s - %s views'''

DAYS_OF_ERROR_REQUESTS = '''%s - %s%% errors'''


def get_results():
    '''Get all results and print them to the stream'''

    # display top articles
    print('TOP 3 ARTICLES')
    for title, views in newsdata_db.get_top_articles():
        print(TOP_ARTICLES % (title, views))

    # display top authors
    print('\nTOP AUTHORS OF ALL TIME')
    for author, views in newsdata_db.get_top_authors():
        print(TOP_AUTHORS % (author, views))

    # display error requests by date
    print('\nDAYS OF ERROR REQUEST > 1%')
    for h_date, percentage in newsdata_db.get_days_of_error():
        print(DAYS_OF_ERROR_REQUESTS % (h_date, percentage))


if __name__ == '__main__':
    get_results()
