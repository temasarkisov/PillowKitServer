import random
import json


VIEW_TYPE = 'text_field'
VIEWS_NUMBER = 25


def generate_color():
    color = '%06x' % random.randint(0, 0xFFFFFF)
    return f'#{color}ff'

def calculate_achor_id(idx):
    if idx == 0:
        return 'container'
    return f'{VIEW_TYPE}_{idx - 1}'

def calculate_achor_to(idx):
    if idx == 0:
        return 'top'
    return 'bottom'

def calculate_height():
    return str(844.0 / VIEWS_NUMBER)

def generate_visual_property():
    if VIEW_TYPE == 'label':
        return {
            'background_color': generate_color()
        }
    elif VIEW_TYPE == 'text_field':
        return {
            'background_color': generate_color()
        }
    elif VIEW_TYPE == 'image':
        return {
            'image_URL': 'http://127.0.0.1:5000/api/v1/research_image'
        } 
    elif VIEW_TYPE == 'button':
        return {
            'background_color': generate_color()
        }
    return {}


if __name__ == '__main__':
    views_data_dict = {
        'views_rules': {}
    }

    for idx in range(VIEWS_NUMBER):
        view_id = f'{VIEW_TYPE}_{idx}'
        
        views_data_dict['views_rules'][view_id] = {
            'view_type': VIEW_TYPE,
            'layout_config': {
                'left': {
                    'id': 'container',
                    'to': 'left',
                    'constant': '0'
                },
                'top': {
                    'id': calculate_achor_id(idx=idx),
                    'to': calculate_achor_to(idx=idx),
                    'constant': '0'
                },
                'right': {
                    'id': 'container',
                    'to': 'right',
                    'constant': '0'
                },
                'height': {
                    'constant': calculate_height()
                }
            },
            'visual_properties': generate_visual_property()
        }

    out_file = open(
        f'views_data/{VIEW_TYPE}_{VIEWS_NUMBER}_views_data.json', 
        'w',
    )
    json.dump(
        views_data_dict, 
        out_file, 
        indent=4,
    )