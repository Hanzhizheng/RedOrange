import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedOrange.settings')

import django
django.setup()

from others.models import (
    Province,
    City,
    Area,
)


def save(file_name, model, foreign_key):
    model_name = foreign_key.__name__.lower() if foreign_key else ''
    with open(file_name, encoding='utf-8') as f:
        all_data = json.load(f)
        for data in all_data:
            kwargs = {
                'name': data['name'],
                'code': data['code'],
            }
            if model_name:
                if foreign_key.objects.filter(code=data[model_name]).exists():
                    kwargs.update(
                        {model_name: foreign_key.objects.get(code=data[model_name])},
                    )
                    model.objects.update_or_create(**kwargs)
            else:
                model.objects.update_or_create(**kwargs)
    print('load %s data done' % model.__name__)


def load_provinces(file_name=None):
    file_name = file_name or './provinces.json'
    model = Province
    foreign_key = None
    save(file_name, model, foreign_key)


def load_cities():
    file_name = './cities.json'
    model = City
    foreign_key = Province
    save(file_name, model, foreign_key)


def load_areas():
    file_name = './areas.json'
    model = Area
    foreign_key = City
    save(file_name, model, foreign_key)


if __name__ == "__main__":
    load_provinces('./provinces_nmg.json')
    load_cities()
    load_areas()