import fire
from fintools.settings import get_logger
from fintools.utils import timeit
import json

logger = get_logger(name=__name__)

from .utils import FlattenJson


class Main:
    fj = FlattenJson()

    def show(self, file: dict):
        json1_file = open(file)
        json1_str = json1_file.read()
        json1_data = json.loads(json1_str)
        return json1_data

    @timeit(logger=logger)
    def flatten(self, file: dict):
        fj = FlattenJson()
        json1_file = open(file)
        json1_str = json1_file.read()
        json1_data = json.loads(json1_str)
        return fj.flatten_dict(json1_data)


if __name__ == "__main__":
    fire.Fire(Main)
