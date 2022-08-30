import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

filename = 'linear_model.sav'
model = pickle.load(open(filename, 'rb'))


# 127.0.0.1

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    region_northeast = 0
    region_northwest = 0
    region_southeast = 0
    region_southwest = 0
    if request.method == "POST":
        age = request.form['age']
        bmi = request.form['bmi']
        children = request.form['children']
        gender = request.form['gender']
        region = request.form['region']
        smoker = request.form['smoker']

        if region == "region_northeast":
            region_northeast = 1
            region_northwest = 0
            region_southeast = 0
            region_southwest = 0
        elif region == "region_northwest":
            region_northeast = 0
            region_northwest = 1
            region_southeast = 0
            region_southwest = 0
        elif region == "region_southeast":
            region_northeast = 0
            region_northwest = 0
            region_southeast = 1
            region_southwest = 0
        else:
            region_northeast = 0
            region_northwest = 0
            region_southeast = 0
            region_southwest = 1

        # prediction = model.predict(standerd_scal.fit_transform([[19, 27.900, 0, 0,	0, 0, 0, 1, 1]]))

        prediction = model.predict([[age, bmi, children, gender, region_northeast,
                                     region_northwest, region_southeast, region_southwest,
                                     smoker]])

        output = round(prediction[0], 2)

        return render_template('index.html', prediction="Your premium is {}".format(prediction))
    else:
        return render_template('index.html', prediction="No result found")


if __name__ == "__main__":
    app.run(debug=True)
