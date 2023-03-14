import psycopg2
from config import config


def main():
    with psycopg2.connect(**config.dict()) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users;")
        for omg in cursor:
            print(omg)


if __name__ == '__main__':
    main()



# TODO create pre-commit config yaml file
