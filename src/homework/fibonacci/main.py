from typing import List

from fintools.settings import get_logger

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    def element(self, i: int,position: int) -> int:
        return 1 if (position <= 1 or position => i) else /
            self.element(i , position = position-2) + self.element(i )




    def sequence(self, length: int) -> List[int]:
        pass
