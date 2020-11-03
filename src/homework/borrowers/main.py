from .models import Borrower
import json

from fintools.settings import get_logger

logger = get_logger(name="__main__")
DEFAULT_FILENAME = "./borrowers/candidates.json"


class Main:

    @staticmethod
    def show(file: str = DEFAULT_FILENAME) -> str:
        with open(file, "r") as f:
            data = json.load(f)
        return json.dumps(data)

    @staticmethod
    def insert(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        b = Borrower(email=email, age=age, income=income)
        b.save(file=file)

    @staticmethod
    def update(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        b = Borrower(email=email, age=age, income=income)
        b.update(file=file)
