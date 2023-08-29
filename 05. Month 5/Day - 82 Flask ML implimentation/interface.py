from flask import Flask,jsonify,request
import project_db
import utils
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

############################################################
##########################Multiplication API################
############################################################

@app.route('/multiplication')
def multiplication():
    print('We are testing multiplicatuion API')
    a = 100
    b = 200
    mul = a * b
    print(f'Multiplication of {a} and {b} is {mul}')
    return jsonify({'Message':f'Multiplication is {mul}'})

#################################################################
########################Login API################################
#################################################################

@app.route('/login',methods = ['POST'])
def login():
    print('We are testing Login API')
    data = request.form
    if request.method == 'POST':
        print('Input data is:',data)
        user_id = data['user_id']
        password = data['password']

        msg = project_db.get_login_details(user_id,password)

        return jsonify({'Message': msg})
    else:
        return jsonify({'Message':'Unsuccessful'})

#######################################################################
############################ML MOdel Prediction########################
#######################################################################

@app.route('/predict', methods = ['POST'])
def prediction():
    print('Testing prediction API')
    data = request.form
    if request.method == 'POST':
        print('Input data is :',data)
        x1 = float(data['SepalLengthCm'])
        x2 = float(data['SepalWidthCm'])
        x3 = float(data['PetalLengthCm'])
        x4 = float(data['PetalWidthCm'])

        prediction = utils.predict_class(x1,x2,x3,x4)

        return jsonify({'Message':f'Predicted Class is :{prediction}'})

    else:
        return jsonify({'Message':'Unsuccessful'})



if __name__ == "__main__":
    app.run()