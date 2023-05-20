from PKViewsData.PKViewsData import PKViewsData
from PKViewRulesBuilder.PKViewRulesBuilder import PKViewRulesBuilder
from PKUtils.JSON_manager import to_JSON, load_JSON

from flask import Flask, send_file


app = Flask(__name__)

view_rules_builder = PKViewRulesBuilder()
views_data = PKViewsData(
    view_rules_builder=view_rules_builder
)


@app.route('/api/v1/sign_up_background_image')
def sign_up_background_image():
    image_path = 'static/images/bmstu_app/sign_up_background_image.png'

    return send_file(
        image_path, 
        mimetype='image/png',
    )

@app.route('/api/v1/sign_in_background_image')
def sign_in_background_image():
    image_path = 'static/images/bmstu_app/sign_in_background_image.png'

    return send_file(
        image_path, 
        mimetype='image/png',
    )

@app.route('/api/v1/update_sign_in_views_data')
def update_sign_in_views_data():
    f = open('static/views_data/bmstu_app/sign_in_views_data.json')
    data = load_JSON(f)
    views_rules = data['views_rules']

    views_data.make_view_rules(views_rules=views_rules)
    
    return to_JSON(views_data.serialize())

@app.route('/api/v1/update_sign_up_views_data')
def update_sign_up_views_data():
    f = open('static/views_data/bmstu_app/sign_up_views_data.json')
    data = load_JSON(f)
    views_rules = data['views_rules']

    views_data.make_view_rules(views_rules=views_rules)
    
    return to_JSON(views_data.serialize())


if __name__ == '__main__':
    app.run(debug=True)
