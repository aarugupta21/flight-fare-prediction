from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline = request.form['airline']
        if (airline == 'Jet Airways'):
            Jet_Airways = True
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet =False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet =False

        elif (airline == 'IndiGo'):
            Jet_Airways = False
            IndiGo =True
            Air_India = False
            Multiple_carriers =False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business =False
            Vistara_Premium_economy =False
            Trujet = False

        elif (airline == 'Air India'):
            Jet_Airways = False
            IndiGo = False
            Air_India = True
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'Multiple carriers'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = True
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy =False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'SpiceJet'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = True
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'Vistara'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = True
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'GoAir'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = True
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'Multiple carriers Premium economy'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = True
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'Jet Airways Business'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = True
            Vistara_Premium_economy = False
            Trujet = False

        elif (airline == 'Vistara Premium economy'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = True
            Trujet = False

        elif (airline == 'Trujet'):
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

        else:
            Jet_Airways = False
            IndiGo = False
            Air_India = False
            Multiple_carriers = False
            SpiceJet = False
            Vistara = False
            GoAir = False
            Multiple_carriers_Premium_economy = False
            Jet_Airways_Business = False
            Vistara_Premium_economy = False
            Trujet = False

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
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = True
            s_Kolkata = False
            s_Mumbai = False
            s_Chennai = False

        elif (Source == 'Kolkata'):
            s_Delhi = False
            s_Kolkata = True
            s_Mumbai = False
            s_Chennai = False

        elif (Source == 'Mumbai'):
            s_Delhi = False
            s_Kolkata = False
            s_Mumbai = True
            s_Chennai = False

        elif (Source == 'Chennai'):
            s_Delhi = False
            s_Kolkata = False
            s_Mumbai = False
            s_Chennai = True

        else:
            s_Delhi = False
            s_Kolkata = False
            s_Mumbai = False
            s_Chennai = False

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = True
            d_Delhi = False
            d_New_Delhi = False
            d_Hyderabad = False
            d_Kolkata = False

        elif (Source == 'Delhi'):
            d_Cochin = False
            d_Delhi = True
            d_New_Delhi = False
            d_Hyderabad = False
            d_Kolkata = False

        elif (Source == 'New_Delhi'):
            d_Cochin = False
            d_Delhi = False
            d_New_Delhi = True
            d_Hyderabad = False
            d_Kolkata = False

        elif (Source == 'Hyderabad'):
            d_Cochin = False
            d_Delhi = False
            d_New_Delhi = False
            d_Hyderabad = True
            d_Kolkata = False

        elif (Source == 'Kolkata'):
            d_Cochin = False
            d_Delhi = False
            d_New_Delhi = False
            d_Hyderabad = False
            d_Kolkata = True

        else:
            d_Cochin = False
            d_Delhi = False
            d_New_Delhi = False
            d_Hyderabad = False
            d_Kolkata = False

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )

        #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
        #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
        #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
        #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
        #    'Airline_Multiple carriers',
        #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
        #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
        #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
        #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
        #    'Destination_Kolkata', 'Destination_New Delhi']

        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output = round(prediction[0], 2)

        return render_template('home.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)