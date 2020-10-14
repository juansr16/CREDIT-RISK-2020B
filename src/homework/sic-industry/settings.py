import os


INDUSTRY_SEARCH_DEFAULT_FILENAME = os.environ.get(
    "INDUSTRY_SEARCH_DEFAULT_FILENAME",
    default="./industry-search/industries.json"
)

INDUSTRY_SEARCH_DEFAULT_THRESHOLD = float(os.environ.get(
    "INDUSTRY_SEARCH_DEFAULT_THRESHOLD",
    default="0.5"
))
