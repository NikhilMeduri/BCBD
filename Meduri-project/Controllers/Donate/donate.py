
from flask import Blueprint, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from flask import abort


donate_fund=Blueprint('donate_fund',__name__,template_folder='templates/Donate')

@donate_fund.route('/donate',methods=['GET','POST'])
def donate_funds():
    return render_template('Donate.html')