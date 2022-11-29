import streamlit as st
import joblib 
import pandas as pd

city_range = {'Abu Talat': 0,
 'Nakheel': 1,
 'Agami': 2,
 'Imbaba': 3,
 'Ain Shams': 4,
 'Shubra al-Khaimah': 5,
 'Faisal': 6,
 'Sharq District': 7,
 '15 May City': 8,
 'Gesr Al Suez': 9,
 'Badr City': 10,
 'Haram': 11,
 'Ras al-Bar': 12,
 'Marsa Matrouh': 13,
 'New Nozha': 14,
 'Helmeyat El Zaytoun': 15,
 'Hadayek al-Ahram': 16,
 'Asafra': 17,
 'Ismailia City': 18,
 'Ras Sedr': 19,
 'Seyouf': 20,
 'Hadayek al-Kobba': 21,
 'Tanta': 22,
 'Sidi Beshr': 23,
 'Mansura': 24,
 'Miami': 25,
 'Katameya': 26,
 'New Damietta': 27,
 'Mandara': 28,
 'Zahraa Al Maadi': 29,
 'Nasr City': 30,
 'Bolkly': 31,
 'Hurghada': 32,
 '10th of Ramadan': 33,
 'Shubra': 34,
 'Maadi': 35,
 'Hadayek 6th of October': 36,
 'Maamoura': 37,
 'Almazah': 38,
 'Zagazig': 39,
 'Sheraton': 40,
 'Obour City': 41,
 'Gianaclis': 42,
 'Al Ibrahimiyyah': 43,
 'Sharm al-Sheikh': 44,
 'Asyut City': 45,
 'Ain Sukhna': 46,
 'Azarita': 47,
 'Dabaa': 48,
 'New Capital City': 49,
 'Heliopolis': 50,
 'Hammam': 51,
 'Alamein': 52,
 'Saba Pasha': 53,
 'Agouza': 54,
 'Zezenia': 55,
 'Mohandessin': 56,
 'Smoha': 57,
 'Dokki': 58,
 'Stanley': 59,
 'New Mansoura': 60,
 'Mostakbal City': 61,
 'Laurent': 62,
 'Moharam Bik': 63,
 'Camp Caesar': 64,
 'Glim': 65,
 'Al Manial': 66,
 'Roushdy': 67,
 'Sahl Hasheesh': 68,
 'North Coast': 69,
 'New Heliopolis': 70,
 'Borg al-Arab': 71,
 '6th of October': 72,
 'Kafr Abdo': 73,
 'Zamalek': 74,
 'Madinaty': 75,
 'Shorouk City': 76,
 'San Stefano': 77,
 'Amreya': 78,
 'Mokattam': 79,
 'Sheikh Zayed': 80,
 'New Cairo - El Tagamoa': 81,
 'West Somid': 82,
 'Rehab City': 83,
 'Gouna': 84,
 'Giza District': 85}
Inputs = joblib.load("Inputs1.pkl")
Model = joblib.load("Model1.pkl")

def predict(Type, Bedrooms, Bathrooms, Area, Furnished,Level, Payment_Option, Delivery_Term,City):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Type"] = Type
    test_df.at[0,"Bedrooms"] = Bedrooms
    test_df.at[0,"Bathrooms"] = Bathrooms
    test_df.at[0,"Area"] = Area
    test_df.at[0,"Furnished"] = Furnished
    test_df.at[0,"Level"] = Level
    test_df.at[0,"Payment_Option"] = Payment_Option
    test_df.at[0,"Delivery_Term"] = Delivery_Term  
    result = Model.predict(test_df)[0]
    if City in city_range:
        City = city_range[City]
        return City
    else :
        City = 'The Area Not Found'
        return City
    
    
def main():
    st.title("Egypt Houses Price App")
    st.image("""https://realestate.eg/ckfinder/userfiles/images/mountain-view-3-new-cairo/Seperat%20Villas%20in%20Mountain%20View%20III.png""")
    st.header('Enter the House details:')
    Type = st.selectbox("The Type of The Property" , ['Apartment', 'Duplex', 'Penthouse', 'Studio', 'Chalet',
    'Twin House', 'Stand Alone Villa', 'Town House'])
    Bedrooms = st.number_input('Bedrooms Number :', min_value=1, max_value=11, value=1)
    Bathrooms = st.number_input('Bathrooms Number :', min_value=1, max_value=11, value=1) 
    Area = st.slider("The Area Of The House" , min_value=0, max_value=1000, value=0, step=1)
    Furnished = st.selectbox("Furnished" ,['Yes', 'No'])
    Level = st.selectbox("The Floor Of The  Property" , [ 1, 10,  0, 12,  3,  2, 11,  9,  4,  5,  8,  6,  7])
    Payment_Option = st.selectbox("Payment Option" , ['Cash', 'Cash or Installment', 'Unknown Payment', 'Installment'])
    Delivery_Term = st.selectbox("Delivery Term" , ['Finished', 'Semi Finished', 'Core & Shell', 'Not Finished'])
    City = st.selectbox('City:', list(city_range.keys()))
    

    if st.button("Predict"):
        result = predict(Type, Bedrooms, Bathrooms, Area, Furnished,Level, Payment_Option, Delivery_Term,City)
        st.success(f'The Price of the house is {result} EGP')
if __name__ == '__main__':
    main()
