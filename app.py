# app.py

from flask import Flask,jsonify,request,send_file
import datetime as dt
import requests
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import pandas as pd
from datetime import datetime,timedelta
import numpy as np
import cv2
import numpy as np
import joblib
import sklearn
import os
import tempfile







app = Flask(__name__)


@app.route('/')
def home():
    return 'haii'


@app.route('/current_weather', methods=['POST'])
def weather():

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = '1f5da08cb47d3cc87ac91f78a97f435a'
    CITY = 'calicut'
    url =BASE_URL + "appid=" + "1f5da08cb47d3cc87ac91f78a97f435a" + "&q=" +  CITY
    response =requests.get(url).json()
    temperature_kelvin = response['main']['temp']

    temperature_celsius = temperature_kelvin - 273.15

    # return render_template("current_weather.html", temperature=str((f'Temperature in Celsius: {temperature_celsius:.2f}°C')))

    return jsonify({"data":10})



@app.route('/get_json_data')
def get_json_data():


    url_f='https://weather.com/en-IN/weather/hourbyhour/l/07d5132b2543887e4d656175575b533c0fe15e1214b4e132d9ae286b18748dcb'
    uclient=req(url_f)
    page_html=uclient.read()
    page_html
    uclient.close()

    page_soup=soup(page_html,'html.parser')
    # page_soup
    containers=page_soup.find_all('details',{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 Disclosure--themeList--1Dz21"})
    sub_containers=containers[0]
    detailed_containers=sub_containers.find_all("div",{'class':"DetailsSummary--DetailsSummary--1DqhO DetailsSummary--hourlyDetailsSummary--2xM-L"})

    extracted_text=[]
    for i in containers:

        sub_containers=i.find_all("div",{'class':"DetailsSummary--DetailsSummary--1DqhO DetailsSummary--hourlyDetailsSummary--2xM-L"})
        time_start=str(sub_containers).find('Name">')+6
        time_end=time_start+5


        sub_containers_condition=i.find_all("div",{'class':"DetailsSummary--condition--2JmHb"})
        time_start_c=str(sub_containers_condition).find('307Ax">')+7
        time_end_c=str(sub_containers_condition).find('</span></div>')

        sub_containers_d=i.find_all("span",{'class':"DetailsSummary--tempValue--jEiXE"})
        time_start_d=str(sub_containers_d).find('"TemperatureValue">')+19
        time_end_d=str(sub_containers_d).find('<span>°')



        extracted_text.append([str(sub_containers)[time_start:time_end],str(sub_containers_condition)[time_start_c:time_end_c],str(sub_containers_d)[time_start_d:time_end_d]])

    print(len(extracted_text))
    extracted_text


    data3=pd.DataFrame(extracted_text,columns=['time','condition','temp'])






    containers=page_soup.find_all('div',{'class':"HourlyForecast--DisclosureList--MQWP6"})
    sub_containers=containers[0]
    detailed_containers=sub_containers.find_all("div",{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 DaypartDetails--enablePreviousBorder--2B1p5 Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})
    detailed_containers

    containers
    extracted_text=[]
    for i in containers:

        sub_containers=i.find_all("div",{'class':"DetailsSummary--DetailsSummary--1DqhO DetailsSummary--hourlyDetailsSummary--2xM-L"})
        time_start=str(sub_containers).find('Name">')+6
        time_end=time_start+5


        sub_containers_condition=i.find_all("div",{'class':"DetailsSummary--condition--2JmHb"})
        time_start_c=str(sub_containers_condition).find('307Ax">')+7
        time_end_c=str(sub_containers_condition).find('</span></div>')

        sub_containers_d=i.find_all("span",{'class':"DetailsSummary--tempValue--jEiXE"})
        time_start_d=str(sub_containers_d).find('"TemperatureValue">')+19
        time_end_d=str(sub_containers_d).find('<span>°')



        extracted_text.append([str(sub_containers)[time_start:time_end],str(sub_containers_condition)[time_start_c:time_end_c],str(sub_containers_d)[time_start_d:time_end_d]])

    print(len(extracted_text))
    extracted_text

    data1=pd.DataFrame(extracted_text,columns=['time','condition','temp'])









    containers=page_soup.find_all('details',{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 DaypartDetails--enablePreviousBorder--2B1p5 Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})
    sub_containers=containers[0]
    detailed_containers=sub_containers.find_all("div",{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 DaypartDetails--enablePreviousBorder--2B1p5 Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})
    detailed_containers

    containers
    extracted_text=[]
    for i in containers:

        sub_containers=i.find_all("div",{'class':"DetailsSummary--DetailsSummary--1DqhO DetailsSummary--hourlyDetailsSummary--2xM-L"})
        time_start=str(sub_containers).find('Name">')+6
        time_end=time_start+5


        sub_containers_condition=i.find_all("div",{'class':"DetailsSummary--condition--2JmHb"})
        time_start_c=str(sub_containers_condition).find('307Ax">')+7
        time_end_c=str(sub_containers_condition).find('</span></div>')

        sub_containers_d=i.find_all("span",{'class':"DetailsSummary--tempValue--jEiXE"})
        time_start_d=str(sub_containers_d).find('"TemperatureValue">')+19
        time_end_d=str(sub_containers_d).find('<span>°')



        extracted_text.append([str(sub_containers)[time_start:time_end],str(sub_containers_condition)[time_start_c:time_end_c],str(sub_containers_d)[time_start_d:time_end_d]])

    print(len(extracted_text))
    extracted_text


    data2=pd.DataFrame(extracted_text,columns=['time','condition','temp']).head(1)

    weather_data=pd.concat([data1,data2,data3],axis=0)
    weather_data.to_csv('weatherdata.csv')

    # weather_data.to_json('data.json', orient='records', lines=True)

    list_of_dicts = weather_data.to_dict(orient='records')


    return jsonify({"data": list_of_dicts})




@app.route('/formation_img', methods=['POST', 'GET'])
def formation_img():
    if request.method == 'POST':
        image_file = request.files['image']
        image_array = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        print(img,'__________________________________________________')

        if img is not None:
            haar_cascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')
            image = cv2.resize(img, (800, 800))

            try:
                faces = haar_cascade.detectMultiScale(image, 1.1, 9)
                if len(faces) == 1:
                    x, y, width, height = faces[0]
                    cropped_image = image[y-30:y + height+60, x-30:x + width+30]
                    temp_filename = tempfile.mktemp(suffix='.jpg')
                    cv2.imwrite(temp_filename, cropped_image)

                    return send_file(temp_filename, as_attachment=True, download_name='cropped_image.jpg')
                
                elif len(faces) >= 2:
                    temp_filename = tempfile.mktemp(suffix='.jpg')
                    cv2.imwrite(temp_filename, image)

                    return send_file(temp_filename, as_attachment=True, download_name='image.jpg')
                
            
            except:
                image = cv2.imread('face 13.png')
                temp_filename = tempfile.mktemp(suffix='.png')
                cv2.imwrite(temp_filename, image)

                return send_file(temp_filename, as_attachment=True, download_name='image.png')
        
        else:
            image = cv2.imread('face 13.png')
            temp_filename = tempfile.mktemp(suffix='.jpg')
            cv2.imwrite(temp_filename, image)

            return send_file(temp_filename, as_attachment=True, download_name='cropped_image.png')



    image = cv2.imread('face 13.png')
    temp_filename = tempfile.mktemp(suffix='.png')
    cv2.imwrite(temp_filename, image)

    return send_file(temp_filename, as_attachment=True, download_name='cropped_image.png')
# image = cv2.imread('face 13.png')
# temp_filename = tempfile.mktemp(suffix='.png')
# cv2.imwrite(temp_filename, image)
# return send_file(temp_filename, as_attachment=True, download_name='cropped_image.png')


@app.route('/dynamic_discount')
def dynamic_discount():
    predict_data=[]
    date_string='06,12,1998'         #____________________________________________________________________
    date_object = datetime.strptime(date_string, '%d,%m,%Y')
    day_format = date_object.strftime('%A')
    if day_format == 'Sunday' or 'Saturday':
        predict_data.append(0)
    elif day_format == 'Friday':
        predict_data.append(1)
    else:
        predict_data.append(2)

    time_string = '06:00:00'      #_______________________________________________________________________
    input_time = datetime.strptime(time_string, '%H:%M:%S').time()

    if input_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
        predict_data.append(1)
    elif input_time < datetime.strptime('16:00:00', '%H:%M:%S').time():
        predict_data.append(2)
    else:
         predict_data.append(0)

    
    #   customer level
    # play_ratio= 'no_of_play'/90  _____________________________________________________________________
    play_ratio=.30
    if play_ratio <=.05:
        predict_data.append(0)
    if play_ratio < .35:
        predict_data.append(1)
    if play_ratio >= .35:
        predict_data.append(2)

    
    data=pd.read_csv('weatherdata.csv')
    input_time = datetime.strptime(time_string, '%H:%M:%S').time()
    half_hour = timedelta(minutes=30)
    new_time = (datetime.combine(datetime.min, input_time) + half_hour).time()
    new_time=str(new_time)
    time=new_time[:5]
    temperature=list(data[data['time']==time]['temp'])[0]
    predict_data.append(temperature)



    turf_rating = 5 #____________________________________________________________________________
    predict_data.append(turf_rating)


    weather_conditions=['T-Storms','Scattered T-Storms']
    weather_c='Scattered T-Storms'   #___________________________________________________
    if weather_c in weather_conditions:
        predict_data.append(1)
    
    else:
        predict_data.append(0)


    model=joblib.load('dynamic_discound_model')
    result =model.predict([predict_data])*1000


    # result =predict_data
    return {'discount_price':str(result),'list':predict_data}


    # return jsonify()


@app.route('/modify_price',methods=['POST','GET'])
def modify_price():
    price=1200
    return jsonify({
            "user": 1,  # Assuming user ID
            "date": "2023-12-10",
            "start_time": "12:00:00",
            "end_time": "14:00:00",
            'discount_price' : 100*4
        })



if __name__ == '__main__':
    app.run(debug=True) 


