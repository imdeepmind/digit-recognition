from flask import Flask, jsonify, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from flask_cors import CORS, cross_origin
import base64
from io import BytesIO
from PIL import Image
from keras.backend import clear_session

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def resize_to_28():
    img = Image.open('temp.png')
    new_width  = 28
    new_height = 28
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save('temp.png')

def convert_and_save(file):
    starter = file.find(',')
    image_data = file[starter+1:]
    image_data = bytes(image_data, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save('temp.png')
    resize_to_28()


@app.route("/")
def index():
    return jsonify({
        "success" : True
    })


@app.route("/recognize/", methods=['POST'])
def recognize():
    try:
        data = request.form
        img = data['file']
        if img:
            convert_and_save(img)

            img_width, img_height = 28,28

            im = Image.open('temp.png')
            width, height = im.size

            if width == img_width and height == img_height:
                model = load_model('mnist.h5')
                model.compile(loss='binary_crossentropy',
                            optimizer='rmsprop',
                            metrics=['accuracy'])
                img = image.load_img('temp.png', target_size=(img_width, img_height))
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                images = np.vstack([x])
                classes = model.predict_classes(images, batch_size=10)
                clear_session()
                return jsonify({
                    "success" : True,
                    "error" : "",
                    "data" : {
                        "digit" : str(classes[0]),
                        "message" : ""
                    }
                })
            else:
                return jsonify({
                    "success": False,
                    "error" : "Invalid Image",
                    "data" : {
                        "digit" : "",
                        "message" : ""
                    }
                })
        else:
            return jsonify({
                "success": False,
                "error" : "Please upload a image",
                "data" : {
                    "digit" : "",
                    "message" : ""
                }
            })
    except Exception as ex:
        print(ex)
        return jsonify({
            "success": False,
            "error" : "Something went wrong",
            "data" : {
                "digit" : "",
                "message" : ""
            }
        })