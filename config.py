import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    database: str
    user: str
    password: str
    host: str
    port: str
    log_format: str
    log_level: str

    @classmethod
    def load_values(cls):
        return cls(
            database=os.environ['PGDATABASE'],
            user=os.environ['PGUSER'],
            password=os.environ['PGPASSWORD'],
            host=os.environ['PGHOST'],
            port=os.environ['PGPORT'],
            log_format=os.environ.get(
                'LOG_FORMAT', '[%(asctime)s.%(msecs)03d] %(levelname)s - %(message)s'
            ),
            log_level=os.environ.get('LOG_LEVEL', 'INFO'),
        )

# TODO add a function to get a dictionary here!


config = Config.load_values()
