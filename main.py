from concurrent.futures import ThreadPoolExecutor, as_completed

import psycopg2

from config import config


def fetch_data() -> None:
    with psycopg2.connect(**config.dict()) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users;")
        for omg in cursor:
            print(omg)


def postgres_ping(connection_index: int) -> None:
    wrong_connection = {
        **config.dict(),
        'password': 'omg'
    }

    try:
        print(f'Connection attempt #{connection_index + 1}')
        psycopg2.connect(**wrong_connection)
    except psycopg2.OperationalError as e:
        print(e)


def main() -> None:
    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = [executor.submit(postgres_ping, index) for index in range(2100)]
        for future in as_completed(futures):
            future.result()


if __name__ == '__main__':
    main()
    # fetch_data()


# TODO create pre-commit config yaml file
# TODO add requirements.txt as well to minimize dependency footprint
