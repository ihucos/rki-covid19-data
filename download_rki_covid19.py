from datetime import date
import csv
import sys

import requests

API_PATH = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query"
PER_PAGE = 1000
OUT_FIELDS = [
    "IdBundesland",
    "Bundesland",
    "Landkreis",
    "Altersgruppe",
    "Geschlecht",
    "AnzahlFall",
    "AnzahlTodesfall",
    "ObjectId",
    "Meldedatum",
    "IdLandkreis",
    "Datenstand",
    "NeuerFall",
    "NeuerTodesfall",
]
BASE_QUERY = dict(
    where="1=1",
    resultType="none",
    outFields=",".join(OUT_FIELDS),
    returnIdsOnly="false",
    returnUniqueIdsOnly="false",
    returnCountOnly="false",
    returnDistinctValues="false",
    cacheHint="false",
    resultOffset="0",
    resultRecordCount=PER_PAGE,
    sqlFormat="none",
    f="json",
)

try:
    outfile = sys.argv[1]
except IndexError:
    print("missing argument: output file", file=sys.stderr)
    sys.exit(1)

with open(outfile, "w") as file:
    writer = csv.DictWriter(file, fieldnames=OUT_FIELDS)
    writer.writeheader()

    page = 0
    while True:
        print(f"querying page {page} ...")
        resp = requests.get(
            API_PATH, params=dict(BASE_QUERY, resultOffset=page * PER_PAGE)
        )
        resp.raise_for_status()
        features = resp.json()["features"]
        if not features:
            break
        writer.writerows(f["attributes"] for f in features)
        page += 1

print(f"saved to {outfile}")
