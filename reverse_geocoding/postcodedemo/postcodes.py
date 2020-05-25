#!/usr/bin/env python3

import postcodes_io_api

import pandas as pd

api = postcodes_io_api.Api(debug_http=False)

#read data
df = pd.read_csv('data_lonlat.csv',sep=',',encoding='utf-8')

#define output DataFrame
odf = pd.DataFrame(columns=('index','lon','lat','postcode','country','region','admin_district','admin_ward'))

#processing
for index,row in df.iterrows():
    try:
        lon = row['longitude']
        lat = row['latitude']
        resp = api.get_nearest_postcodes_for_coordinates(latitude=lat,longitude=lon,limit=1)
        status = resp['status'] if 'status' in resp else str()
        result = resp['result'] if ('result' in resp) and (resp['result'] != None) else []
        item = result[0] if len(result)>0 else {}
        postcode = item['postcode'] if 'postcode' in item else str()
        country = item['country'] if 'country' in item else str()
        region = item['region'] if 'region' in item else str()
        admin_district = item['admin_district'] if 'admin_district' in item else str()
        admin_ward = item['admin_ward'] if 'admin_ward' in item else str()
        data = {"index":index, "lon":lon, "lat":lat, "postcode":postcode, "country":country, 
                "region":region, "admin_district":admin_district, "admin_ward":admin_ward}
        print(data)
        #add
        odf = odf.append([data],ignore_index=True)
    except Exception as e:
        print('error:',str(e))

#make odf output file
odf.to_csv('output.csv',encoding='utf-8-sig',index=False)

