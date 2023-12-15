from flask import Flask,jsonify,request,send_file
import datetime as dt
from datetime import datetime
import requests
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import pandas as pd
from datetime import datetime,timedelta
from fuzzywuzzy import process
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

    return jsonify({"data":10})



@app.route('/get_json_data')
def get_json_data():

    url_f='https://weather.com/en-IN/weather/hourbyhour/l/07d5132b2543887e4d656175575b533c0fe15e1214b4e132d9ae286b18748dcb'
    uclient=req(url_f)
    page_html=uclient.read()
    page_html
    uclient.close()

    page_soup=soup(page_html,'html.parser')
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

    data3=pd.DataFrame(extracted_text,columns=['time','condition','temp'])
    #__________________
    containers=page_soup.find_all('div',{'class':"HourlyForecast--DisclosureList--MQWP6"})
    sub_containers=containers[0]
    detailed_containers=sub_containers.find_all("div",{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 DaypartDetails--enablePreviousBorder--2B1p5 Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})
    detailed_containers

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

    data1=pd.DataFrame(extracted_text,columns=['time','condition','temp'])
    #____________________________
    containers=page_soup.find_all('details',{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 DaypartDetails--enablePreviousBorder--2B1p5 Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})
    sub_containers=containers[0]
    detailed_containers=sub_containers.find_all("div",{'class':"DaypartDetails--DayPartDetail--2XOOV DaypartDetails--ctaShown--3JJj3 DaypartDetails--enablePreviousBorder--2B1p5 Disclosure--themeList--1Dz21 Disclosure--disableBorder--3Np63"})

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

    data2=pd.DataFrame(extracted_text,columns=['time','condition','temp']).head(1)
    weather_data=pd.concat([data1,data2,data3],axis=0)
    weather_data.to_csv('weatherdata.csv')
    list_of_dicts = weather_data.to_dict(orient='records')

    return jsonify({"data": list_of_dicts})

@app.route('/formation_img', methods=['POST', 'GET'])
def formation_img():
    try:
        if request.method == 'POST':
            image_file = request.files['image']
            image_array = np.frombuffer(image_file.read(), np.uint8)
            img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)            
            print(img,'__________________________________________________')

            if img is not None:
                haar_cascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')
                image = cv2.resize(img, (300, 300))
                
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
                    else:
                        temp_filename = tempfile.mktemp(suffix='.jpg')
                        cv2.imwrite(temp_filename, image)

                        return send_file(temp_filename, as_attachment=True, download_name='image.jpg')                
                except:
                    image = cv2.imread('face 13.png')
                    temp_filename = tempfile.mktemp(suffix='.jpg')
                    cv2.imwrite(temp_filename, image)

                    return send_file(temp_filename, as_attachment=True, download_name='image.jpg')            
            else:
                image = cv2.imread('face 13.png')
                temp_filename = tempfile.mktemp(suffix='.jpg')
                cv2.imwrite(temp_filename, image)

                return send_file(temp_filename, as_attachment=True, download_name='cropped_image.jpg')
    except:
        image = cv2.imread('face 13.png')
        temp_filename = tempfile.mktemp(suffix='.png')
        cv2.imwrite(temp_filename, image)

        return send_file(temp_filename, as_attachment=True, download_name='cropped_image.png')


@app.route('/dynamic_discount',methods=['POST','GET'])
def dynamic_discount():

    data = request.get_json()
    print(data['search text'])

    start_time = data['date'] + " " + data['start_time']
    end_time   = data['date'] + " " + data['end_time']
    print(start_time)
    print(end_time)

    time1 = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    time_difference = str(time2 - time1)
    total_hour = int(time_difference.split(':')[0])
    print('total_hour',total_hour)
    predict_data=[]

    date_string=data['date']        #____________________________________________________________________
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    day_format = date_object.strftime('%A')
    if day_format == 'Sunday' or 'Saturday':
        predict_data.append(0)
    elif day_format == 'Friday':
        predict_data.append(1)
    else:
        predict_data.append(2)

    time_string = data['start_time']      #_______________________________________________________________________
    input_time = datetime.strptime(time_string, '%H:%M:%S').time()
    print('input_time',input_time)

    if input_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
        predict_data.append(1)
    elif input_time < datetime.strptime('16:00:00', '%H:%M:%S').time():
        predict_data.append(2)
    else:
         predict_data.append(0)
    
    #   customer level
    play_ratio=data['booking_count']/90
    if play_ratio <=.05:
        predict_data.append(0)
    if play_ratio < .35:
        predict_data.append(1)
    if play_ratio >= .35:
        predict_data.append(2)
    print('play_ratio',play_ratio)

    df=pd.read_csv('weatherdata.csv')
    input_time = datetime.strptime(time_string, '%H:%M:%S').time()
    half_hour = timedelta(minutes=30)
    new_time = (datetime.combine(datetime.min, input_time) + half_hour).time()
    new_time=str(new_time)
    time=new_time[:5]
    temperature=list(df[df['time']==time]['temp'])[0]
    predict_data.append(temperature)

    turf_rating = data['turf'] #____________________________________________________________________________
    predict_data.append(turf_rating)

    weather_conditions=['T-Storms','Scattered T-Storms']
    weather_c='Scattered T-Storms'   #___________________________________________________
    if weather_c in weather_conditions:
        predict_data.append(1)    
    else:
        predict_data.append(0)

    print('predict_data',predict_data)

    model=joblib.load('dynamic_discound_model')
    result =model.predict([predict_data]) * total_hour * data['price']

    actual_price = data['price']

    return jsonify({"discount_price": result[0]})


@app.route('/search_response',methods=['POST','GET'])
def search_response():
 
    data = request.get_json()  
    print(data,'from search_response________________________________________________________________')
    
    user_input = data[0]['name']
    print(user_input)

    api_url_search = 'http://192.168.1.22:8000/owner/turf-display-all/'
    search_rquest_turf = requests.get(api_url_search)
    if search_rquest_turf.status_code == 200:
        data = search_rquest_turf.json()
        data=pd.DataFrame(data)
        data.to_csv('turf_details.csv')  
    # user_input = "Golden Turf Gardens"
    df=pd.read_csv('turf_details.csv')
    matches = process.extract(user_input,list(df.name) )
    print(matches)

    threshold = 60

    similar_turfs = [match for match in matches if match[1] >= threshold]
    list_=[]
    if similar_turfs:
        print("Similar Turfs:")
        for turf, confidence in similar_turfs:
            df[df['name']==turf]
            list_.append(turf)
        
        list_2 = []

        for name in list_:
            matching_rows = df[df['name'].str.strip().str.lower() == name.strip().lower()]
            # print(matching_rows,"_________________________________________________")

            if not matching_rows.empty:
                list_2.append(matching_rows.to_dict(orient='records')[0])

        return list_2
    else:
        return "No similar turfs found."

    
@app.route('/player_search_response',methods=['POST','GET'])
def player_search_response():       
    
    data = request.get_json()  
    print(data,'from search_response________________________________________________________________')
    
    user_input = data[0]['name']
    print(user_input)

    api_url_player_search = 'http://192.168.1.21:9000/user/player/'
    search_request_player = requests.get(api_url_player_search)
    if search_request_player.status_code == 200:
        data = search_request_player.json()
        data=pd.DataFrame(data)
        data.to_csv('player_details.csv')

    # user_input = "munshid"
    df=pd.read_csv('player_details.csv')
    print(df)
    matches = process.extract(user_input,list(df.player_name) )
    print(matches)

    threshold = 70
    similar_name = [match for match in matches if match[1] >= threshold]
    list_=[]
    if similar_name:
        print("similar_name:")
        for player, confidence in similar_name:
            df[df['player_name']==player]
            list_.append(player)        
        list_2 = []
        for name in list_:
            matching_rows = df[df['player_name'].str.strip().str.lower() == name.strip().lower()]
            if not matching_rows.empty:
                list_2.append(matching_rows.to_dict(orient='records')[0])

        return list_2
    else:
        return "No similar turfs found."

if __name__ == '__main__':
    app.run(debug=True) 




