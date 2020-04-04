# rki-covid19-data

The [Robert Koch-Institut](https://www.rki.de/) (rki) maintains a [dashboard](https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4) with the development of covid19 in germany.
That dashboard provides an (undocumented?) [API](https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query)

This repository uses that api to dump all data from the table `RKI_COVID19` into an csv file that can be used for E. g. analysis with pandas, costum dashboards or whatever else you find useful. The data is downloaded every day and can be found under releases. You can also just run that script locally.


## Sample ([./data_sample.csv](./data_sample.csv))

|              |            |                 |              |            |            |                 |          |               |             |                         |           |                | 
|--------------|------------|-----------------|--------------|------------|------------|-----------------|----------|---------------|-------------|-------------------------|-----------|----------------| 
| IdBundesland | Bundesland | Landkreis       | Altersgruppe | Geschlecht | AnzahlFall | AnzahlTodesfall | ObjectId | Meldedatum    | IdLandkreis | Datenstand              | NeuerFall | NeuerTodesfall | 
| 10           | Saarland   | LK Sankt Wendel | A60-A79      | W          | 1          | 0               | 697852   | 1585785600000 | 10046       | "03.04.2020, 00:00 Uhr" | 1         | -9             | 
| 10           | Saarland   | LK Sankt Wendel | A80+         | M          | 1          | 0               | 697853   | 1585699200000 | 10046       | "03.04.2020, 00:00 Uhr" | 0         | -9             | 
| 10           | Saarland   | LK Sankt Wendel | unbekannt    | M          | 1          | 0               | 697854   | 1583971200000 | 10046       | "03.04.2020, 00:00 Uhr" | 0         | -9             | 
| 11           | Berlin     | SK Berlin Mitte | A00-A04      | M          | 1          | 0               | 697855   | 1583366400000 | 11001       | "03.04.2020, 00:00 Uhr" | 0         | -9             | 
| 11           | Berlin     | SK Berlin Mitte | A00-A04      | M          | 1          | 0               | 697856   | 1583884800000 | 11001       | "03.04.2020, 00:00 Uhr" | 0         | -              | 

## Integrate with pandas
```
>>> import pandas
>>> df = pandas.read_csv('https://github.com/ihucos/covid19-data/releases/download/2020-04-03/data.csv')
>>>
>>> # get the total verified infections as shown in the dashboard
>>> df['AnzahlFall'][df['AnzahlFall'] > 0].sum()
79696
```

## Daily [Releases](https://github.com/ihucos/covid19-data/releases)
[![Build Status](https://travis-ci.org/ihucos/covid19-data.svg?branch=master)](https://travis-ci.org/ihucos/covid19-data)

