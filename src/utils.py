import logging

logger = logging.getLogger("cleansheet")
logger.setLevel(logging.INFO)
_handler = logging.StreamHandler()
_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
if not logger.handlers:
    logger.addHandler(_handler)

MAX_FILE_SIZE_MB = 50
MAX_FILE_SIZE_PRO_MB = 500
TARGET_PROFILE_SECONDS = 5

SUPPORTED_EXTENSIONS = {".csv", ".tsv", ".txt"}
SUPPORTED_EXTENSIONS_PRO = {".csv", ".tsv", ".txt", ".xlsx", ".xls"}

CLEANING_METHODS = {
    "mean": "Fill with Mean (numeric only)",
    "median": "Fill with Median (numeric only)",
    "mode": "Fill with Mode (most frequent)",
    "drop": "Drop rows with missing values",
    "value": "Fill with a custom value",
}

TEXT_OPERATIONS = [
    "Strip whitespace",
    "Lowercase",
    "Uppercase",
    "Title Case",
    "Remove special characters",
    "Replace text",
]

DTYPE_MAP: dict[str, str] = {
    "int64": "Int64",
    "float64": "float64",
    "string": "string",
    "datetime64[ns]": "datetime64[ns]",
    "category": "category",
}


def format_bytes(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def humanize_column_name(col: str) -> str:
    return col.replace("_", " ").replace("-", " ").strip().title()
