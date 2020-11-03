import json
from typing import Dict

from .utils import get_current_utc


class Borrower:

    def __init__(self, email: str, age: int, income: float):
        self.created_at = get_current_utc()
        self.updated_at = self.created_at
        self.email = email
        self.age = age
        self.income = income

    def to_json(self) -> Dict:
        dict = {"email": self.email,
                "age": self.age,
                "income": self.income,
                "created_at": self.created_at,
                "updated_at": self.updated_at
                }

        return dict

    def save(self, file: str):
        data = self.to_json()
        with open(file, "r") as f:
            borrowers_file = json.load(f)
        borrowers_file["updated_at"] = get_current_utc()
        borrowers_file["candidates"].append(data)
        with open(file, 'w') as file:
            file.write(json.dumps(borrowers_file, indent=4))

    def update(self, file: str):
        with open(file, "r")as f:
            borrowers_file = json.load(f)
        borrowers_file["updated_at"] = get_current_utc()
        for i in borrowers_file["candidates"]:
            if self.email == i["email"]:
                i["age"] = self.age
                i["income"] = self.income
                i["updated_at"] = get_current_utc()
        with open(file, "w") as file:
            file.write(json.dumps(borrowers_file, indent=4))
