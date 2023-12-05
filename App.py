from flask import Flask, render_template, flash, request,session


import cv2




app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



@app.route("/")
def homepage():

    return render_template('index.html')




@app.route("/Predict")
def Predict():

    return render_template('Predict.html')














@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':


        file = request.files['fileupload']
        file.save('static/Out/Test.jpg')

        import warnings
        warnings.filterwarnings('ignore')

        import tensorflow as tf
        classifierLoad = tf.keras.models.load_model('Model.h5')

        import numpy as np
        from keras.preprocessing import image

        test_image = image.load_img('static/Out/Test.jpg', target_size=(200, 200))
        img1 = cv2.imread('static/Out/Test.jpg')
        # test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = classifierLoad.predict(test_image)

        prediction = ''
        pre = ''

        if result[0][0] == 1:

            prediction = "NORMAL"


        elif result[0][1] == 1:

            prediction = "PNEUMONIA"
            pre="CDC recommends PCV13 or PCV15 for all children younger than 5 years old and children 5 through 18 years old with certain medical conditions that increase their risk of pneumococcal disease.CDC also recommends PPSV23 for children 2 through 18 years old with certain medical conditions that increase their risk of pneumococcal disease.For those who have never received any pneumococcal conjugate vaccine, CDC recommends PCV15 or PCV20 for adults 65 years or older and adults 19 through 64 years old with certain medical conditions or risk factors. If PCV15 is used, this should be followed by a dose of PPSV2"








        return render_template('Predict.html', prediction=prediction,pre=pre)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
