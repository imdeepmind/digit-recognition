from flask import Flask, jsonify, request
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "success" : True
    })


@app.route("/recognize/", methods=['POST'])
def recognize():
    print (request.files)
    # checking if the file is present or not.
    if 'file' not in request.files:
        return return jsonify({
                "success": False,
                "error" : "Please upload a image",
                "data" : {
                    "digit" : "",
                    "message" : ""
                }
            })
    
    file = request.files['file']
    print(file)
    file.save("temp.png")

    img_width, img_height = 28,28

    im = Image.open('temp.png')
    width, height = im.size

    if width == img_width and height == img_height:
        model = load_model('mnist.h5')

        model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['accuracy'])

        # predicting images
        img = image.load_img('temp.png', target_size=(img_width, img_height))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict_classes(images, batch_size=10)
        print(classes)
        return jsonify({
            "success" : True,
            "error" : "",
            "data" : {
                "digit" : classes[0],
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