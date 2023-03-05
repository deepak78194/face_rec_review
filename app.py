from flask import Flask,request,render_template
from datetime import date

#### Defining Flask App
app = Flask(__name__)

#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

################## ROUTING FUNCTIONS #########################

#### Our main page
@app.route('/')
def home():
    #names,rolls,times,l = extract_attendance()
    return render_template('home.html', totalreg=0,datetoday2=datetoday2)

#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)