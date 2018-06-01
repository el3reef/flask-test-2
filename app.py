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

    model = Sequential()
    model.add(Dense(2,input_dim=2,activation='relu'))
    model.add(Dense(16,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))
    
    
    sgd = SGD(lr=0.005)
    model.compile(loss='binary_crossentropy',optimizer=sgd,metrics=['accuracy'])
    
    model.summary()
    
    model.fit(x_train,y_train,batch_size=1,nb_epoch=10)
    
    
    #print(model.predict_proba(x))
    
    score = model.evaluate(x_test,y_test, verbose=0) 


    return "hi"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

