import fire

from fintools.settings import get_logger
from fintools.utils import timeit, method_caching

MY_STUDENT_ID = "IF699365"


class Hello:

    @staticmethod
    def hello():
        return f"This is a greeting message from {MY_STUDENT_ID}."

if __name__ == "__main__":
    fire.Fire(Hello)