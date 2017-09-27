# Logs Analysis

![volcain.io](https://avatars1.githubusercontent.com/u/1916665?v=4&s=400)

> Udacity Nanodegree - Full Stack Web Developer Project

This project is used to analyze the logs of a newsdata database and do some reports

## Getting started

A quick introduction of the minimal setup you need to get a up running this project.

Setup database:

```shell
cd logsanalysis
psql -d news -f newsdata.sql
```

Run program:

```shell
cd logsanalysis
python newsdata.py
```

## Developing

### Built With

[PostgreSQL](https://www.postgresql.org/download/)
[Psycopg](http://initd.org/psycopg/download/)
[Python 3](https://www.python.org/download/releases/3.0/)

### Directory structure

```text
newsdata
|   LICENSE
|   newsdata.py (code to run)
|   newsdata.sql (SQL code to create the database)
|   newsdata_db.py (database code)
|   README.md
```

### Prerequisites

In order to run this code you need Python 3, PostgreSQL & Psycopg on your computer.

## Style guide

The code style relies on [PEP8](https://www.python.org/dev/peps/pep-0008/).

## Licensing

[MIT LICENSE](LICENSE)
