# WORK IN PROGRESS

# covid19-data
A helper to access Robert Koch-Institut's covid19 data more easily

## Where does this data come from?
The [Robert Koch-Institut](https://www.rki.de/) (rki) maintains a [dashboard](https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4) with the development of covid19 in germany.
That dashboard provides an (undocumented?) [API](https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query)

This repository uses that api to dump all data from the table `RKI_COVID19` into an csv file that can be used for E. g. analysis with pandas, costum dashboards or whatever else you find useful. The data is downloaded every day and can be found under releases. You can also just run that script locally.


## Daily update status
[![Build Status](https://travis-ci.org/ihucos/covid19-data.svg?branch=master)](https://travis-ci.org/ihucos/covid19-data)

## Loading this data with pandas
```
>>> import pandas
>>> df = pandas.read_csv('https://github.com/ihucos/covid19-data/releases/download/2020-04-03/data.csv')
>>> df.head()
   IdBundesland          Bundesland     Landkreis Altersgruppe Geschlecht  \
0             1  Schleswig-Holstein  SK Flensburg      A15-A34          M
1             1  Schleswig-Holstein  SK Flensburg      A15-A34          M
2             1  Schleswig-Holstein  SK Flensburg      A15-A34          M
3             1  Schleswig-Holstein  SK Flensburg      A15-A34          M
4             1  Schleswig-Holstein  SK Flensburg      A15-A34          W

   AnzahlFall  AnzahlTodesfall  ObjectId     Meldedatum  IdLandkreis  \
0           1                0    670153  1584144000000         1001
1           2                0    670154  1584576000000         1001
2           1                0    670155  1584748800000         1001
3           1                0    670156  1585267200000         1001
4           1                0    670157  1584144000000         1001

              Datenstand  NeuerFall  NeuerTodesfall
0  03.04.2020, 00:00 Uhr          0              -9
1  03.04.2020, 00:00 Uhr          0              -9
2  03.04.2020, 00:00 Uhr          0              -9
3  03.04.2020, 00:00 Uhr          0              -9
4  03.04.2020, 00:00 Uhr          0              -9
```
