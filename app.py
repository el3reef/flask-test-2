from flask import Flask
from datetime import datetime
import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Dropout,Activation
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    x = np.array([[0,0],[0,1],[1,0],[1,1]])
    y = np.array([[0],[1],[1],[0]])
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.10)

 


    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

