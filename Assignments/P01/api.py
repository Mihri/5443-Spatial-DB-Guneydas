from array import typecodes
from cmath import sqrt
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn

import psycopg2
import json

"""
           _____ _____   _____ _   _ ______ ____
     /\   |  __ \_   _| |_   _| \ | |  ____/ __ \
    /  \  | |__) || |     | | |  \| | |__ | |  | |
   / /\ \ |  ___/ | |     | | | . ` |  __|| |  | |
  / ____ \| |    _| |_   _| |_| |\  | |   | |__| |
 /_/    \_\_|   |_____| |_____|_| \_|_|    \____/
"""

description = """🚀
## Earthquakes Api
##Mihriban Guneydas
"""

class DatabaseCursor(object):

    def __init__(self, conn_config_file):
        with open(conn_config_file) as config_file:
            self.conn_config = json.load(config_file)

    def __enter__(self):
        self.conn = psycopg2.connect(
            "dbname='"
            + self.conn_config["dbname"]
            + "' "
            + "user='"
            + self.conn_config["user"]
            + "' "
            + "host='"
            + self.conn_config["host"]
            + "' "
            + "password='"
            + self.conn_config["password"]
            + "' "
            + "port="
            + self.conn_config["port"]
            + " "
        )
        self.cur = self.conn.cursor()
        self.cur.execute("SET search_path TO " + self.conn_config["schema"])

        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

app = FastAPI(
    title="Earthquakes Api",
    description=description,
    version="0.0.1",
)

"""
  _____   ____  _    _ _______ ______  _____
 |  __ \ / __ \| |  | |__   __|  ____|/ ____|
 | |__) | |  | | |  | |  | |  | |__  | (___
 |  _  /| |  | | |  | |  | |  |  __|  \___ \
 | | \ \| |__| | |__| |  | |  | |____ ____) |
 |_|  \_\\____/ \____/   |_|  |______|_____/
"""

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/findAll")
async def All():
    sql = "SELECT * FROM test_data"
    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()

@app.get("/findOne/{earthquake_id}")
async def One(earthquake_id):
    sql = f"""SELECT * FROM test_data WHERE earthquake_id='{earthquake_id}'"""
    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()

@app.get("/findbyCountry/{place}")
async def Country(place):
    sql = f"""SELECT * FROM test_data WHERE place LIKE '{place}'"""
    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()

@app.get("/findClosest/{lat}/{long}")
async def Closest(lat,long):
    sql = f"""SELECT *, ST_Distance('SRID=4326;POINT({lat} {long})'::geometry, the_geom) AS dist FROM test_data ORDER BY dist LIMIT 1"""
    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()

@app.get("/findMostFrequent")
async def mostFrequent():
    sql = "SELECT place,COUNT(place) AS MOST_FREQUENT FROM test_data GROUP BY place ORDER BY COUNT(place) DESC"
    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()

@app.get("/findBiggest")
async def Biggest():
    sql = "SELECT place, magnitude FROM test_data ORDER BY magnitude DESC LIMIT 10"
    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8080, log_level="debug", reload=True)
