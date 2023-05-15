from PKViewsData.PKViewsData import PKViewsData
from PKViewRulesBuilder.PKViewRulesBuilder import PKViewRulesBuilder
from PKUtils.JSON_manager import to_JSON, load_JSON

from flask import Flask, send_file


app = Flask(__name__)

@app.route('/api/v1/background_image')
def background_image():
    image_path = 'static/images/background_image.png'
    
    return send_file(
        image_path, 
        mimetype='image/png',
    )

@app.route('/api/v1/update_views_rules')
def update_views():
    f = open('static/view_rules/views_rules.json')
    data = load_JSON(f)
    views_rules = data['views_rules']

    view_rules_builder = PKViewRulesBuilder()
    views_data = PKViewsData(
        view_rules_builder=view_rules_builder
    )
    views_data.make_view_rules(views_rules=views_rules)
    
    return to_JSON(views_data.serialize())


if __name__ == '__main__':
    app.run(debug=True)
