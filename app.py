from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
from keras.models import load_model
import tensorflow as tf
import sys
import facebook
import urllib.request
import numpy as np
import pandas as pd

app = Flask(__name__)

dic={0:'motorcycle',1:'truck',2:'boat',3:'bus',4:'cycle',5:'sitar',6:'ektara',7:'flutes',8:'tabla',9:'harmonium'}

model=load_model('mobilenetv2_real1.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(224,224))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 224,224,3)
	p = model.predict_classes(i)
	return dic[p[0]]

def predict(img_path):
    model=load_model('mlic_small.h5')
    model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

    # img = cv2.imread('test.jpg')
    # img = cv2.resize(img,(320,240))
    # img = np.reshape(img,[1,320,240,3])

    # classes = model.predict_classes(img)

    # return classes
    # dimensions of our images
    img_width, img_height = 224, 224

    # predicting images
    img = tf.keras.utils.load_img(img_path, target_size=(img_width, img_height))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    return classes.tolist()
def predict_test(newlist):
    submission=pd.Dataframe(newlist[3])
    model=load_model('mobilenetv2_real1.h5')
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy']) 
    test_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    labels=['boat','bus','cycle','ektara','flutes','harmonium','motorcycle','sitar','tabla','truck']
    test_generator = test_data_generator.flow_from_dataframe(
        labels,
        directory = "static/",
        x_col="image",
        y_col=None,
        target_size=(224, 224),
        color_mode="rgb",
        classes=None,
        class_mode=None,
        shuffle=False,
        batch_size=1
    )

    predictions = model.predict(test_generator,steps=len(test_generator.filenames))
    return predictions
# routes
def calculate(p):
    c=[]
    k=0
    for i in p[0]:
        k=k+1
        if i>=0.50:
            c.append(dic[k-1])
    return c
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html", prediction = 0, img_path = '')

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

token='EAAF5VNX0krcBAB0Rt9aXsxRMhDKPPiYvjpHGZBdixiA3mNx4cPlJakFqeZANk5mq7RTNx5MJOJSUHM31FZBzZCvdfGfReKjpXYPZCYXbklJec5JOBqzZBH2wtZBt8gdfbQzGwjrt883bt5htDeSLqU14Nyu4ox3m0WAlAXRY9k2OqpRqdCqhnHnZAi6X60UKEWDaDniompSDbj5xF0oBC9IvgshECWnTqnwn5XIHm3Fk1ZANVSgbJKKO953svwBHerR0ZD'

@app.route("/su", methods = ['GET', 'POST'])
# def get_output():
# 	if request.method == 'POST':
#         img = request.files['my_image']

# 		img_path = "static/" + img.filename	
# 		img.save(img_path)

# 		p = predict(img_path)

# 	return render_template("index.html", prediction = p, img_path = img_path)
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict(img_path)
	return render_template("index.html", prediction = calculate(p), img_path = img_path)


@app.route("/submit",methods=['GET','POST'])
def push():
    if request.method=='POST':
        img=request.files['my_image']
        img_path="static/"+img.filename
        img.save(img_path)
        p=predict(img_path)
        c=calculate(p)
        graph=facebook.GraphAPI(access_token=token)
        page_id='100744415996177'
        img_url='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYnmwcE8kQNdspoPLTP-PoUkbDl0H65tJpZQdB0Mhx8TLOJx75VWGBY2S84jdy4l0qgVcau6D0P0js0bnchwhgzMiPV7Q7MFLT_ApNDdmbL4Ny4dMuinKHvoQnTFrpPe8Pw7nyqRFZXocpwDKg1vVAtFQbwbIwW3qNBDNTgrMyJV1f4X47-rn90jITWw/s450/image612.jpg'
        graph.put_object(page_id,'photos',message=c[0],url=img_url)
        return render_template("index.html",predict=c,img_path=img_path)

@app.route('/text')
def home():

	return render_template('homesus.html')


# @app.route('/predict',methods=['POST'])
# def predict():
#     message=request.form['message']
    # df=pd.read_csv("dataset_SE_Bangla.csv")
    # X=df["Text"]
    # cv=TfidfVectorizer()
    # X=cv.fit_transform(X)
    # infile = open('suspicious_model','rb')
    # model = joblib.load(infile)
    #data=[message]
    #vecct=cv.transform(data).toarray()
    #_prediction = int(model.predict(vecct))
    # if _prediction ==0:
    #     message="✅"+message
    # else:
    #     message="❌"+message
    # page_access_token = token
    # graph = facebook.GraphAPI(page_access_token)
    # facebook_page_id = '101432762410121'
    # graph.put_object(facebook_page_id, "feed", message=message)
    # return render_template('homesus.html',message=message,prediction=_prediction)

def get_text_of_post():
    try:
        graph=facebook.GraphAPI(access_token=token,version=3.1)
        posts=graph.request('100744415996177/photos?type=uploaded')['data']
        d={}
        i=0
        for dic in posts:
            newlist=[]
            # newlist.append(dic['message'])
            newlist.append(dic['id'])
            ##image url fetching
            pic_url=graph.request('100744415996177_'+dic['id']+'?fields=full_picture,picture')['full_picture']
            newlist.append(pic_url)
            #image saving
            path="static/" +dic['id']
            urllib.request.urlretrieve(pic_url,path)
            newlist.append(path)
            p=predict(path)
            newlist.append(p)
            c=calculate(p)
            newlist.append(c)
            d[i]=newlist
            i=i+1
        return d
    except Exception as e:
        return 0
def get_text_image_of_post():
    try:
        graph=facebook.GraphAPI(access_token=token,version=3.1)
        posts=graph.request('100744415996177/photos?type=uploaded')['data']
        msg=graph.request('100744415996177/posts')['data']
        d={}
        i=0
        for dic in posts:
            newlist=[]
            # newlist.append(dic['message'])
            newlist.append(dic['id'])
            ##image url fetching
            pic_url=graph.request('100744415996177_'+dic['id']+'?fields=full_picture,picture')['full_picture']
            newlist.append(pic_url)
            #image saving
            # path="static/" +dic['id']
            # urllib.request.urlretrieve(pic_url,path)
            # newlist.append(path)
            # p=predict(path)
            # newlist.append(p)
            # c=calculate(p)
            # newlist.append(c)
            d[i]=newlist
            i=i+1
        p={}
        j=0
        for m in msg:
            newlist=[]
            newlist.append(m['message'])
            p[j]=newlist
            j=j+1
        return d,p
    except Exception as e:
        return 0
@app.route('/dashboard',methods=['GET','POST'])
def post_table():
    #newlist={}
    newlist,msg=get_text_image_of_post()
    if newlist==0:
        print("check the facebook access")
    else:
        print("work")
    return render_template('dashboard.php',newlist=newlist,msg=msg)

if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)