import streamlit as st
import joblib 
import pandas as pd
city_label = {'Nakheel': 0,
 'Agami': 1,
 'Ain Shams': 2,
 'Faisal': 3,
 'Shubra al-Khaimah': 4,
 'Haram': 5,
 'Abu Talat': 6,
 '15 May City': 7,
 'Gesr Al Suez': 8,
 'Badr City': 9,
 'New Nozha': 10,
 'Imbaba': 11,
 'Hadayek al-Ahram': 12,
 'Marsa Matrouh': 13,
 'Helmeyat El Zaytoun': 14,
 'Sharq District': 15,
 'New Damietta': 16,
 'Ismailia City': 17,
 'Hadayek al-Kobba': 18,
 'Zagazig': 19,
 'Obour City': 20,
 'Nasr City': 21,
 'Tanta': 22,
 'Borg al-Arab': 23,
 'Mandara': 24,
 'Mansura': 25,
 'Seyouf': 26,
 'Asafra': 27,
 'Hadayek 6th of October': 28,
 'Almazah': 29,
 'Katameya': 30,
 'Maadi': 31,
 'Zahraa Al Maadi': 32,
 'Hammam': 33,
 'Sidi Beshr': 34,
 'Ras al-Bar': 35,
 '10th of Ramadan': 36,
 'New Capital City': 37,
 'Miami': 38,
 'Bolkly': 39,
 'Ras Sedr': 40,
 'Heliopolis': 41,
 'Gianaclis': 42,
 'Shubra': 43,
 'Sheraton': 44,
 'New Mansoura': 45,
 'Hurghada': 46,
 'Agouza': 47,
 'Amreya': 48,
 'Mohandessin': 49,
 'New Heliopolis': 50,
 'Asyut City': 51,
 'Al Ibrahimiyyah': 52,
 'Zezenia': 53,
 'Dokki': 54,
 'Glim': 55,
 'Saba Pasha': 56,
 'Sharm al-Sheikh': 57,
 'Alamein': 58,
 'Maamoura': 59,
 'Mostakbal City': 60,
 'Azarita': 61,
 '6th of October': 62,
 'Laurent': 63,
 'Dabaa': 64,
 'Ain Sukhna': 65,
 'Smoha': 66,
 'Roushdy': 67,
 'Stanley': 68,
 'Shorouk City': 69,
 'West Somid': 70,
 'Kafr Abdo': 71,
 'Zamalek': 72,
 'Moharam Bik': 73,
 'Sheikh Zayed': 74,
 'Madinaty': 75,
 'Camp Caesar': 76,
 'New Cairo - El Tagamoa': 77,
 'San Stefano': 78,
 'Rehab City': 79,
 'Sahl Hasheesh': 80,
 'North Coast': 81,
 'Al Manial': 82,
 'Mokattam': 83,
 'Giza District': 84,
 'Gouna': 85}
city_per_m = {'Nakheel': 2643.64406779661,
 'Agami': 3454.9058473736372,
 'Ain Shams': 3633.9285714285716,
 'Faisal': 3763.597977243995,
 'Shubra al-Khaimah': 3875.379939209726,
 'Haram': 3918.500154942671,
 'Abu Talat': 4107.142857142857,
 '15 May City': 4144.796380090498,
 'Gesr Al Suez': 4195.454090909091,
 'Badr City': 4273.1902009358655,
 'New Nozha': 4440.132669983416,
 'Imbaba': 4682.539682539683,
 'Hadayek al-Ahram': 5276.7314925236215,
 'Marsa Matrouh': 5664.92068243041,
 'Helmeyat El Zaytoun': 5814.624759461193,
 'Sharq District': 5819.964349376114,
 'New Damietta': 5997.727272727273,
 'Ismailia City': 6917.47572815534,
 'Hadayek al-Kobba': 7209.302325581395,
 'Zagazig': 7210.759027266028,
 'Obour City': 7255.73988529515,
 'Nasr City': 7422.387644543776,
 'Tanta': 7470.308788598575,
 'Borg al-Arab': 7592.364708239133,
 'Mandara': 7847.286108555658,
 'Mansura': 7898.196469685341,
 'Seyouf': 7952.054794520548,
 'Asafra': 7987.371744277822,
 'Hadayek 6th of October': 8059.29372489698,
 'Almazah': 8246.869409660107,
 'Katameya': 8530.694246314788,
 'Maadi': 8740.701057471264,
 'Zahraa Al Maadi': 8876.271763280145,
 'Hammam': 8926.72858617131,
 'Sidi Beshr': 9044.357026587086,
 'Ras al-Bar': 9063.432835820895,
 '10th of Ramadan': 9068.769361702127,
 'New Capital City': 9101.232729498452,
 'Miami': 9155.020215633424,
 'Bolkly': 9440.928270042194,
 'Ras Sedr': 9582.44762784966,
 'Heliopolis': 10056.840815075839,
 'Gianaclis': 10320.51282051282,
 'Shubra': 10480.62015503876,
 'Sheraton': 10491.496108388585,
 'New Mansoura': 10652.410924531943,
 'Hurghada': 10866.505166475315,
 'Agouza': 11061.51990349819,
 'Amreya': 11596.385815991238,
 'Mohandessin': 11948.542024013723,
 'New Heliopolis': 12107.100928485364,
 'Asyut City': 12239.345887016849,
 'Al Ibrahimiyyah': 12452.651515151516,
 'Zezenia': 12581.132075471698,
 'Dokki': 12660.550458715596,
 'Glim': 13013.462202278219,
 'Saba Pasha': 13217.796171753751,
 'Sharm al-Sheikh': 13463.527321190582,
 'Alamein': 13588.253881143082,
 'Maamoura': 13588.709677419354,
 'Mostakbal City': 13704.535121160336,
 'Azarita': 13719.325153374233,
 '6th of October': 13967.59350725094,
 'Laurent': 14029.279873384332,
 'Dabaa': 14468.22308690013,
 'Ain Sukhna': 14950.239125980956,
 'Smoha': 15113.732313575525,
 'Roushdy': 15361.702127659575,
 'Stanley': 15709.969788519638,
 'Shorouk City': 15793.188223538647,
 'West Somid': 15806.589147286822,
 'Kafr Abdo': 16371.750704666458,
 'Zamalek': 16532.80168606985,
 'Moharam Bik': 18138.096401452625,
 'Sheikh Zayed': 18141.515796225078,
 'Madinaty': 18930.939048215125,
 'Camp Caesar': 18986.39455782313,
 'New Cairo - El Tagamoa': 19365.32639196986,
 'San Stefano': 19826.52705061082,
 'Rehab City': 19838.307168005776,
 'Sahl Hasheesh': 19842.047930283225,
 'North Coast': 20586.289498359118,
 'Al Manial': 21123.711340206184,
 'Mokattam': 23248.16122667959,
 'Giza District': 28863.82393397524,
 'Gouna': 52036.84030157642}
Inputs = joblib.load("features.h5")
Model = joblib.load("model.h5")

def predict(Type, Bedrooms, Bathrooms, Area, Furnished,Level, Payment_Option, Delivery_Term,City,meter_Price):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Type"] = Type
    test_df.at[0,"Bedrooms"] = Bedrooms
    test_df.at[0,"Bathrooms"] = Bathrooms
    test_df.at[0,"Area"] = Area
    test_df.at[0,"Furnished"] = Furnished
    test_df.at[0,"Level"] = Level
    test_df.at[0,"Payment_Option"] = Payment_Option
    test_df.at[0,"Delivery_Term"] = Delivery_Term
    if City in city_label:
        City = city_label[City]
        return City
    else :
        City = 'The Area Not Found'
        return City  
***************************************************
    if meter_Price in city_per_m:
        meter_Price = city_per_m[meter_Price]
        return meter_Price
    else :
        meter_Price = 'The Area Not Found'
        return meter_Price
    result = Model.predict(test_df)[0]
    
def main():
    st.title("Egypt Houses Price App")
    Type = st.selectbox("The Type of The Property" , ['Apartment', 'Duplex', 'Penthouse', 'Studio', 'Chalet',
    'Twin House', 'Stand Alone Villa', 'Town House'])
    Bedrooms = st.number_input('Bedrooms Number :', min_value=1, max_value=11, value=1)
    Bathrooms = st.number_input('Bathrooms Number :', min_value=1, max_value=11, value=1) 
    Area = st.slider("The Area Of The House" , min_value=0, max_value=1000, value=0, step=1)
    Furnished = st.selectbox("Furnished" ,['Yes', 'No'])
    Level = st.selectbox("The Floor Of The  Property" , [ 1, 10,  0, 12,  3,  2, 11,  9,  4,  5,  8,  6,  7])
    Payment_Option = st.selectbox("Payment Option" , ['Cash', 'Cash or Installment', 'Unknown Payment', 'Installment'])
    Delivery_Term = st.selectbox("Delivery Term" , ['Finished', 'Semi Finished', 'Core & Shell', 'Not Finished'])
    City = st.selectbox('City:', list(city_label.keys()))
    

    if st.button("Predict The Price Of The House"):
        result = predict(Type, Bedrooms, Bathrooms, Area, Furnished,Level, Payment_Option, Delivery_Term,City)
        st.success(f'The Price of the house is {result} EGP')
if __name__ == '__main__':
    main()
