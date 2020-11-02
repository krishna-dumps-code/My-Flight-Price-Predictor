from flask import Flask, request, render_template, flash, redirect, url_for
from flask_cors import cross_origin
import sklearn
import pickle
import numpy as np
import pandas as pd

my_app = Flask(__name__)
my_app.secret_key = "hellok55676637436"
model = pickle.load(open("rfmodel_flight.pkl", "rb"))

@my_app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@my_app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        # Date_of_Journey
        dep_date = request.form["Dep_Time"]
        Journey_date = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_date, format ="%Y-%m-%dT%H:%M").month)

        # Departure time
        Dep_hour = int(pd.to_datetime(dep_date, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(dep_date, format ="%Y-%m-%dT%H:%M").minute)
        #print("Departure : ",Dep_hour, Dep_min)

        # Arrival time
        arr_date = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(arr_date, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(arr_date, format ="%Y-%m-%dT%H:%M").minute)
        #print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration(minutes in log)
        dur_hours_in_min = int(request.form["Dur_hour"])*60
        dur_min = int(request.form["Dur_min"])
        duration = round(np.log(dur_hours_in_min + dur_min),3)
        print("Duration : ", dur_hours_in_min, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0(not in column)
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
    
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
   
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0 

        elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Bangalore = 0(not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = [1,0,0,0]

        elif (Source == 'Kolkata'):
            s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = [0,1,0,0]

        elif (Source == 'Mumbai'):
            s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = [0,0,1,0]

        elif (Source == 'Chennai'):
            s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = [0,0,0,1]

        else:
            s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = [0,0,0,0]


        # Destination
        # Bangalore = 0(not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = [1,0,0,0,0]
        
        elif (Destination == 'Delhi'):
            d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = [0,1,0,0,0] 

        elif (Destination == 'New_Delhi'):
            d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = [0,0,1,0,0]

        elif (Destination == 'Hyderabad'):
           d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = [0,0,0,1,0]

        elif (Destination == 'Kolkata'):
            d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = [0,0,0,0,1]

        else:
            d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = [0,0,0,0,0]

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata)
    
        prediction=model.predict([[
            Total_stops,Journey_date,Journey_month,Dep_hour,Dep_min,Arrival_hour,
            Arrival_min,Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,
            Multiple_carriers,Multiple_carriers_Premium_economy,SpiceJet,
            Trujet,Vistara,Vistara_Premium_economy,s_Chennai,s_Delhi,s_Kolkata,
            s_Mumbai,d_Cochin,d_Delhi,d_Hyderabad,d_Kolkata,d_New_Delhi,duration
            ]])

        price = round(prediction[0],2)
        flash('We wist you a happy and safe journey.', 'success')
        return render_template('home.html',prediction_text=f"Your ticket price ranges from Rs. {price-100} - {price+80}")
    else:
        flash('Please provide some info to get the Price!', 'error')
        return redirect(url_for('home'))


if __name__ == "__main__":
    my_app.run(debug=True)
