from flask import Flask
from flask_cors import CORS,cross_origin
 
from Controllers.Maps.maps_page import maps_page
from Controllers.Donate.donate import donate_fund
from Controllers.DonateConfirmation import confirm_donation

app=Flask(__name__)


#------------------register blue prints---------------------
app.register_blueprint(maps_page)
app.register_blueprint(donate_fund)

#-----------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)

