import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector.abstracts import MySQLConnectionAbstract

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


def get_db_config() -> dict:
    return {
        "host": os.environ.get("MYSQL_HOST", "localhost"),
        "port": int(os.environ.get("MYSQL_PORT", "3306")),
        "user": os.environ.get("MYSQL_USER", "root"),
        "password": os.environ.get("MYSQL_PASSWORD", "1234"),
        "database": os.environ.get("MYSQL_DATABASE", "greencart"),
        "charset": "utf8mb4",
    }


def get_connection() -> MySQLConnectionAbstract:
    return mysql.connector.connect(**get_db_config())
