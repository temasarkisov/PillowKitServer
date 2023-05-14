from PKViewsData.PKViewsData import PKViewsData
from PKViewRules.PKViewRules import PKViewRules
from PKUtils.JSON_manager import to_JSON, to_error_JSON

from flask import Flask, request


app = Flask(__name__)

@app.route('/api/v1/update_views_rules')
def update_views():
    views_rules = [
        PKViewRules(
            id='demo0',
            view_type='label',
            layout_config={
                'left': {
                    'id': 'container',
                    'to': 'left',
                    'constant': '10',
                },
                'top': {
                    'id': 'container',
                    'to': 'top',
                    'constant': '10',
                },
                'right': {
                    'id': 'container',
                    'to': 'right',
                    'constant': '-50',
                },
                'bottom': {
                    'id': 'container',
                    'to': 'bottom',
                    'constant': '-300',
                },
            },
            visual_properties={
                'text': 'Demo0',
                'font': 'ALSSiriusVF_Medium',
                'font_size': '30.0',
                'text_alignment': 'center',
                'background_color': '#32a852ff',
                'corner_radius': '30',
                'border_color': '#a91de0ff',
                'border_width': '5',
            },
            visual_effects=None,
        ),
        PKViewRules(
            id='demo1',
            view_type='label',
            layout_config={
                'left': {
                    'id': 'container',
                    'to': 'left',
                    'constant': '10',
                },
                'top': {
                    'id': 'demo0',
                    'to': 'bottom',
                    'constant': '10',
                },
                'right': {
                    'id': 'container',
                    'to': 'right',
                    'constant': '-10',
                },
                'bottom': {
                    'id': 'container',
                    'to': 'bottom',
                    'constant': '-50',
                },
            },
            visual_properties={
                'text': 'Demo1',
                'font': 'ALSSiriusVF_Medium',
                'font_size': '30.0',
                'text_alignment': 'center',
                'background_color': '#32a852ff',
                'corner_radius': '30',
                'border_color': '#a91de0ff',
                'border_width': '5',
            },
            visual_effects=None,
        ),
        PKViewRules(
            id='demo3',
            view_type='image',
            layout_config={
                'left': {
                    'id': 'container',
                    'to': 'left',
                    'constant': '10',
                },
                'top': {
                    'id': 'container',
                    'to': 'top',
                    'constant': '300',
                },
                'right': {
                    'id': 'container',
                    'to': 'right',
                    'constant': '-10',
                },
                'bottom': {
                    'id': 'container',
                    'to': 'bottom',
                    'constant': '-300',
                },
            },
            visual_properties={
                'image_URL': 'https://s.yimg.com/ny/api/res/1.2/EKu93CW66xcYA8h7_F7FNg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://media.zenfs.com/en/sixers_wire_usa_today_sports_articles_847/33b84e605616e67764769429dd3963c0',
                'background_color': '#32a852ff',
                'corner_radius': '30',
                'border_color': '#a91de0ff',
                'border_width': '5',
            },
            visual_effects=None,
        ),
        # PKViewRules(
        #     id='demo0',
        #     view_type='text_field',
        #     layout_config={
        #         'relative': 'top',
        #     },
        #     visual_properties={
        #         'placeholder': 'I love Pasha',
        #         'font': 'ALSSiriusVF_Medium',
        #         'font_size': '30.0',
        #         'text_color': '#a91de0ff',
        #         'background_color': '#e6e1a1ff',
        #         'corner_radius': '30',
        #         'border_color': '#a91de0ff',
        #         'border_width': '2',
        #         'autocorrectionType': 'false',
        #         'autocapitalization_type': 'false',
        #     },
        #     visual_effects=None,
        # ),
        PKViewRules(
            id='demo3',
            view_type='button',
            layout_config={
                'left': {
                    'id': 'container',
                    'to': 'left',
                    'constant': '10',
                },
                'top': {
                    'id': 'container',
                    'to': 'top',
                    'constant': '10',
                },
                'right': {
                    'id': 'container',
                    'to': 'right',
                    'constant': '-50',
                },
                'bottom': {
                    'id': 'container',
                    'to': 'bottom',
                    'constant': '-300',
                },
            },
            visual_properties={
                'text': 'Pasha is the best!',
                'font': 'ALSSiriusVF_Medium',
                'font_size': '30.0',
                'text_alignment': 'center',
                'background_color': '#32a852ff',
                'corner_radius': '30',
                'border_color': '#a91de0ff',
                'border_width': '5',
                'is_user_interaction_enabled': 'true',
            },
            visual_effects={
                'tap_effect': 'pulse',
            },
        ),
    ]

    view_data = PKViewsData(views_rules=views_rules)
    
    return to_JSON(view_data.serialize())


if __name__ == '__main__':
    app.run(debug=True)
