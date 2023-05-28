# @app.route('/api/v1/research_image')
# def research_image():
#     image_path = 'research/images/bmstu.png'

#     return send_file(
#         image_path, 
#         mimetype='image/png',
#     )

# @app.route('/api/v1/update_research_views_data')
# def update_research_views_data():
#     f = open('research/views_data/button_500_views_data.json')
#     data = load_JSON(f)
#     views_rules = data['views_rules']

#     views_data.make_view_rules(views_rules=views_rules)
    
#     return to_JSON(views_data.serialize())