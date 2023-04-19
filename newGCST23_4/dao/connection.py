import pymysql
from sqlalchemy import create_engine

from settings import DATABASES


class mysql:
    def __init__(self):
        self.DB = pymysql.connect(host=DATABASES['HOST'],
                                  user=DATABASES['USER'],
                                  password=DATABASES['PASSWORD'],
                                  database=DATABASES['NAME'])
        self.DB_SQLAlchemy = create_engine(
            f"mysql+pymysql://{DATABASES['USER']}:{DATABASES['PASSWORD']}@{DATABASES['HOST']}:3306/{DATABASES['NAME']}",
            echo=True)
        self.cursor = self.DB.cursor()