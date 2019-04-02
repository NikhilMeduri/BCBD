
from flask import Blueprint, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from flask import abort


maps_page = Blueprint('maps_page', __name__, template_folder='templates/Maps')
CORS(maps_page)


@maps_page.route('/', methods=['GET', 'POST'])
def maps_page_render():
    return render_template('MapB.html')


