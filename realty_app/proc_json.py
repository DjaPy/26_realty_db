import requests
import json
import argparse
import sys

number_index = 0
sys.path.insert(number_index, '/home/kento/devman/26_realty_db/')

from realty_app import db
from realty_app.models import Real_estate

url = 'https://devman.org/media/filer_public/e5/62/' \
      'e56287d2-9519-4e18-878a-6d4849b628e2/ads.json'


def load_json(url):
    json = requests.get(url)
    json_content = json.json()
    return json_content


def get_json_from_unix(json_file):
    return json.load(json_file)


def add_real_estate_content(json_content):
    for apartment in json_content:
        apartment_data = Real_estate(
            id=apartment['id'],
            settlement=apartment['settlement'],
            under_construction=apartment['under_construction'],
            description=apartment['description'],
            price=apartment['price'],
            oblast_district=apartment['oblast_district'],
            living_area=apartment['living_area'],
            has_balcony=apartment['has_balcony'],
            address=apartment['address'],
            construction_year=apartment['construction_year'],
            rooms_number=apartment['rooms_number'],
            premise_area=apartment['premise_area'],
            active=True)
        db.session.add(apartment_data)
        db.session.commit()


def parser_for_update_db():
    parser = argparse.ArgumentParser(description="Updates the database")
    parser.add_argument('-u', '--update', required=True,
                        type=argparse.FileType(mode='r'),
                        help='Allows you to update the database'
                             ' from the upload, in json format')


if __name__ == '__main__':
    json_content = parser_for_update_db()
    try:
        json_content = json_content.update
    except AttributeError:
        json_content = load_json(url)
    add_real_estate_content(json_content)
