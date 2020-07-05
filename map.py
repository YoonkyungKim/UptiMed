from flask import render_template, Flask
import csv
# from decimal import Decimal

def read_hospital_info():
    with open("static/hospitals-new.csv") as f:
        reader = csv.reader(f, quotechar="'")
        next(reader, None)
        data = []
        for row in reader:
            d = {
                "longtitude": float(row[0]),
                "latitude": float(row[1]),
                "service_type": row[2],
                "name": row[3],
                "address_line_1": row[4],
                "address_line_2": row[5],
                "community": row[6],
                "postal-code": row[7],
                "operating_time": row[8],
                "wait_time": row[9]
            }
            data.append(d)
        return data

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def postalSearch():
    # Display default map 
    info = read_hospital_info()
    return render_template('hello.html', hospital_info=info)

if __name__=="__main__": 
    app.run()
