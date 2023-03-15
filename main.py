import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from typing import Dict

import psycopg2

LONG_PASSWORD = 'gibberish' * 100
PG_OVERLOAD_MSG = 'sorry, too many clients already'
THREAD_COUNT = 20


@dataclass(frozen=True)
class Config:
    database: str
    user: str
    password: str
    host: str
    port: str

    @classmethod
    def load_values(cls):
        return cls(
            database=os.environ['PGDATABASE'],
            user=os.environ['PGUSER'],
            password=os.environ['PGPASSWORD'],
            host=os.environ['PGHOST'],
            port=os.environ['PGPORT'],
        )

    def dict(self) -> Dict:
        return asdict(self)


config = Config.load_values()


def postgres_ping() -> None:
    wrong_connection = {**config.dict(), 'password': LONG_PASSWORD}

    try:
        psycopg2.connect(**wrong_connection)
    except psycopg2.OperationalError as e:
        if PG_OVERLOAD_MSG in str(e):
            print(e)


def main() -> None:
    while True:
        with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
            futures = [executor.submit(postgres_ping) for _ in range(THREAD_COUNT)]
            for future in as_completed(futures):
                future.result()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting at your request')
