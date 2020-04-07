# rki-covid19-data

The [Robert Koch-Institut](https://www.rki.de/) (rki) maintains a [dashboard](https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4) with the development of verified covid19 infections in germany.
That dashboard provides an (undocumented?) [API](https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query). This repository uses that API to dump all data from the table `RKI_COVID19` into a csv file that could fit your use case better than the somewhat raw API.

## Daily [Releases](https://github.com/ihucos/covid19-data/releases)
[![Build Status](https://travis-ci.org/ihucos/rki-covid19-data.svg?branch=master)](https://travis-ci.org/ihucos/rki-covid19-data) (In progress)

## Integrate with pandas
```
>>> import pandas as pd
>>> df = pd.read_csv('https://github.com/ihucos/rki-covid19-data/releases/download/2020-04-03/data.csv')
>>>
>>> #  Total verified infections as shown in dashboard
>>> df['AnzahlFall'][df['AnzahlFall'] > 0].sum()
79696
```


## Sample

|              |            |                 |              |            |            |                 |          |               |             |                         |           |                | 
|--------------|------------|-----------------|--------------|------------|------------|-----------------|----------|---------------|-------------|-------------------------|-----------|----------------| 
| IdBundesland | Bundesland | Landkreis       | Altersgruppe | Geschlecht | AnzahlFall | AnzahlTodesfall | ObjectId | Meldedatum    | IdLandkreis | Datenstand              | NeuerFall | NeuerTodesfall | 
| 10           | Saarland   | LK Sankt Wendel | A60-A79      | W          | 1          | 0               | 697852   | 1585785600000 | 10046       | "03.04.2020, 00:00 Uhr" | 1         | -9             | 
| 10           | Saarland   | LK Sankt Wendel | A80+         | M          | 1          | 0               | 697853   | 1585699200000 | 10046       | "03.04.2020, 00:00 Uhr" | 0         | -9             | 
| 10           | Saarland   | LK Sankt Wendel | unbekannt    | M          | 1          | 0               | 697854   | 1583971200000 | 10046       | "03.04.2020, 00:00 Uhr" | 0         | -9             | 
| 11           | Berlin     | SK Berlin Mitte | A00-A04      | M          | 1          | 0               | 697855   | 1583366400000 | 11001       | "03.04.2020, 00:00 Uhr" | 0         | -9             | 
| 11           | Berlin     | SK Berlin Mitte | A00-A04      | M          | 1          | 0               | 697856   | 1583884800000 | 11001       | "03.04.2020, 00:00 Uhr" | 0         | -              | 
