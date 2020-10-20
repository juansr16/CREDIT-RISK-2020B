from typing import List
import fire

from fintools.settings import get_logger
from fintools.utils import timeit, method_caching

logger = get_logger(name=__name__)


class Main:
    def __init__(self):
        logger.info("Main object initialized.")

    def fib_rec(self, n):
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            x = self.fib_rec(n - 1)
            x.append(sum(x[:-3:-1]))
            return x

    @method_caching
    def element(self, position: int) -> int:
        if isinstance(position, int):
            return position

    @timeit(logger=logger)
    def sequence(self, length: int) -> List[int]:
        return self.fib_rec(length)


if __name__ == "__main__":
    fire.Fire(Main)
