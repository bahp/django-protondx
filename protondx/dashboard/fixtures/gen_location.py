import random
import postcodes_io_api
from django.contrib.gis.db.models import Extent
from django.contrib.gis.geos import Point

from dataUpload.models import CountryBorder, RegionBorder


def get_locations(lat, long):
    """
    Uses coordinates to determine Country, Region, and Postcode.

    :param float lat: Latitude
    :param float long: Longitude
    :return: Returns a dictionary of locations at different scales
    :rtype: dict
    """
    # api = postcodes_io_api.Api(debug_http=False)
    # resp = api.get_nearest_postcodes_for_coordinates(latitude=lat, longitude=long, limit=1, radius=2000)
    # result = resp['result'] if ('result' in resp) and (resp['result'] != None) else []
    # item = result[0] if len(result) > 0 else {}
    # postcode = item['postcode'] if 'postcode' in item else str()
    pnt = Point(long, lat)

    # try and get region using local data, if that fails take data from postcodesAPI
    try:
        region = RegionBorder.objects.distance(pnt).order_by('distance')
        print(region)
        region = region[0]
    except IndexError:
        region = str()

        # region = item['region'] if 'region' in item else (item['country'] if 'country' in item else str())

    # try and take country from local data, if that fails and there is a region country is UK else unknown
    try:
        country = CountryBorder.objects.filter(mpoly__contains=pnt)[0].name
    except IndexError:
        if region:
            country = 'United Kingdom'
        else:
            country = ''

    return {"country": country, "region": region, "postcode": str()}


def generate_random(number):
    """
    This method is used to generate random points with the United Kingdom (currently) and obtain
    associated location data such as country, region and postcode.

    :param number: Number of points to generate
    :return: List of dictionaries, each containing: country, region, postcode, point
    :rtype: list
    """
    UK_poly = CountryBorder.objects.filter(name="United Kingdom").annotate(extent=Extent('mpoly'))
    list_of_points = []
    minx, miny, maxx, maxy = UK_poly[0].extent
    counter = 0
    while counter < number:
        long = random.uniform(minx, maxx)
        lat = random.uniform(miny, maxy)
        pnt = Point(long, lat, srid=4326)
        if UK_poly[0].mpoly.contains(pnt):
            locations = get_locations(lat, long)
            locations['coordinates'] = pnt
            list_of_points.append(locations)
            counter += 1
    return list_of_points
