import os
from dataclasses import asdict, dataclass
from typing import Dict


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
