from PKViewsData.PKViewsData import PKViewsData
from PKViewRulesBuilder.PKViewRulesBuilder import PKViewRulesBuilder
from PKUtils.JSON_manager import to_JSON, load_JSON

from flask import Flask, send_file, request
import os


app = Flask(__name__)

view_rules_builder = PKViewRulesBuilder()
views_data = PKViewsData(
    view_rules_builder=view_rules_builder
)


# http://62.84.114.142:5000/api/v1/image/static?name=sign_in_background_image
@app.route('/api/v1/image/static')
def image_from_static():
    args = request.args
    name = args.get('name') + '.png'
    image_path = os.path.join('static/images/bmstu_app', name)

    return send_file(
        image_path, 
        mimetype='image/png',
    )

# http://62.84.114.142:5000/api/v1/update/views/data?name=sign_in_views_data
@app.route('/api/v1/update/views/data')
def update_views_data():
    args = request.args
    print(args.get('name'))
    name = args.get('name') + '_o.json'
    json_path = os.path.join('static/views_data/bmstu_app', name)
    
    f = open(json_path)
    data = load_JSON(f)
    views_rules = data['views_rules']
    views_data.make_view_rules(views_rules=views_rules)
    
    return to_JSON(views_data.serialize())


if __name__ == '__main__':
    extra_dirs = ['static',]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)
    
    port = int(os.environ.get('PORT', 5000))
    
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=port,
        extra_files=extra_files,
    )
