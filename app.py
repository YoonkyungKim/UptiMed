import json, csv

from flask import Flask, render_template, redirect, url_for, request, make_response


# always refer to yourself
app = Flask(__name__)

app.config.from_pyfile('settings.py')

def read_hospital_info():
    with open("static/hospitals-final.csv") as csv_f:
        reader = csv.reader(csv_f, quotechar="'")
        first_line = True
        data = []
        for row in reader:
            if not first_line:
                data.append({
                "longtitude": row[0],
                "latitude": row[1],
                "service_type": row[2],
                "name": row[3],
                "address_line_1": row[4],
                "address_line_2": row[5],
                "community": row[6],
                "postal_code": row[7],
                "operating_time": row[8],
                "wait_time": row[9]
                })
            else:
                first_line = False
        return data

@app.route('/')
def index():
    return render_template("index.html",
        APIKEY=app.config.get("APIKEY")
    )

@app.route('/customer-login')
def cust_login():
    return render_template("customer-login.html")

@app.route('/cust_login_submit', methods=['POST'])
def cust_login_submit():
    response = make_response(redirect(url_for('search')))
    return response

@app.route('/search')
def search():
    hospitals = read_hospital_info()
    return render_template(
        "search.html",
        hospitals=hospitals,
        search_results=[]
    )

@app.route('/search-result', methods=['GET'])
def search_result():
    results = []
    hospitals = read_hospital_info()
    user_input = request.args.get('search', 'None')
    # print(hospitals)
    for e in hospitals:
        values = "".join(e.values())
        if user_input and user_input.lower() in values.lower():
            results.append(e)
    if len(results) == 0:
        results.append("No result")
    # print(results[0])
    return render_template(
        "search.html",
        hospitals=hospitals,
        search_results=results
    )


@app.route('/test')
def postalSearch():
    # Display default map 
    info = read_hospital_info()
    return render_template('map.html', hospital_info=info)


# debug=True: reload everytime we change the code and save it
if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
