from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')  #Base API
def welcome():
    print('We are learning Flask')
    return jsonify({'Message':'Welcome API Successful'})

###########################################################
###########################################################

@app.route('/name')
def get_name():
    print('We are testing name API')
    return jsonify({'Message':'Name API Successful'})

###########################################################
###########################################################

@app.route('/name/<name>')
def Name(name):
    print('We are testing name API')
    return jsonify({'Message':f'name is {name}'})

##########################################################
##########################################################

@app.route('/marks/<int:mark>')
def get_marks(mark):
    print('We are testing mark API')
    return jsonify({'Message':f'Student mark is {mark}'})

##########################################################
##########################################################

@app.route('/cgpa/<float:cgpa>')
def get_cgpa(cgpa):
    print('We are testing cgpa API')
    return jsonify({'Message':f'Student CGPA is {cgpa}'})

##########################################################
########################Addition API######################
##########################################################

@app.route('/addition')
def addition():
    print('We are testing addition API')
    a = 100
    b = 200
    add = a + b
    print(f'Addition of {a} and {b} is {add}')
    return jsonify({'Message':f'Addition of given Nnumber is {add}'})



if __name__ == "__main__":
    app.run()