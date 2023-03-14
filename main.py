import psycopg2

# TODO config dataclass (in this module)
db_args = {
    'database': '',
    'user': '',
    'password': '',
    'host': 'localhost',
    'port': '5432',
}


def main():
    with psycopg2.connect(**db_args) as connection:
        cursor = connection.cursor()
        print(cursor)


if __name__ == '__main__':
    main()


# dbname: the database name
# database: the database name (only as keyword argument)
# user: user name used to authenticate
# password: password used to authenticate
# host: database host address (defaults to UNIX socket if not provided)
# port: connection port number (defaults to

# TODO create pre-commit config yaml file
