
from flask import Blueprint, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from flask import abort

confirm_donation_route = Blueprint('confirm_donation_route',__name__,template_folder='templates/Donate')

@confirm_donation_route.route('/result_page',methods=['GET','POST'])
def confirm_donation_router():
    name=request.get['name']
    amount=request.get['amount']
    return render_template('/result.html',name=name,amount_value=amount)