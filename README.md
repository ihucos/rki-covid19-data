# WORK IN PROGRESS

# covid19-data
A helper to access Robert Koch-Institut's covid19 data more easily

## Where does this data come from?
The [Robert Koch-Institut](https://www.rki.de/) (rki) maintains a [dashboard](https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4) with the development of covid19 in germany.
That dashboard provides an (undocumented?) [API](https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query)

This repository uses that api to dump all data from the table `RKI_COVID19` into an csv file that can be used for E. g. analysis with pandas, costum dashboards or whatever else you find useful. The data is downloaded every day and can be found under releases. You can also just run that script locally.

## Loading this data with pandas
```
import pandas
df = pandas.read_csv('https://raw.githubusercontent.com/ihucos/covid19-data/master/data.csv')
```

## Daily update status
[![Build Status](https://travis-ci.org/ihucos/covid19-data.svg?branch=master)](https://travis-ci.org/ihucos/covid19-data)
