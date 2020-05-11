import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedOrange.settings')

import django
django.setup()

from others.models import (
    JobCategory,
    JobSubCategory,
)


def save(file_name, model, call):
    with open(file_name, encoding='utf-8') as f:
        all_data = json.load(f)
        for data in all_data:
            if call == 'load_jobc':
                kwargs = {
                    'name': data['name'],
                    'code': data['code'],
                }
            elif call == 'load_jobsc':
                kwargs = {
                    'name': data['sc_name'],
                    'code': data['sc_code'],
                    'category': JobCategory.objects.get(code=data['code']),
                }
            model.objects.update_or_create(**kwargs)
    print('load %s data done' % model.__name__)


def load_jobc():
    file_name = './categories.json'
    model = JobCategory
    save(file_name, model, call='load_jobc')


def load_jobsc():
    file_name = './sub_categories.json'
    model = JobSubCategory
    save(file_name, model, call='load_jobsc')



if __name__ == "__main__":
    load_jobc()
    load_jobsc()