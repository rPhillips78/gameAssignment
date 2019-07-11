from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    print("*********************")
    print("The hello function")
    return "Hello World!"

@app.route('/bagofmoney')
def loose_money():
    print("*********************")
    print("This is the bag of money function")
    return render_template("bagofmoney.html")

@app.route('/storyends')
def ignore():
    print('*********************')
    print('This is the story ends function')
    return render_template("storyends.html")

@app.route('/keepit')
def pick_up():
    print('**********************')
    print("This is the keep it function")
    return render_template('keepit.html')

@app.route('/pickItUp')
def spend():
    print('********************')
    print('This is the pick it up function')
    return render_template('pickItUp.html')

@app.route('/sirens')
def sirens():
    print('***********************')
    print("This is the siren function")
    return render_template('sirens.html')

@app.route('/invest')
def invest():
    print('************************')
    print('This is the invest function')
    return render_template('invest.html')

@app.route('/turnitin')
def stocks():
    print('************************')
    print('This is the turn it in function')
    return render_template('turnitin.html')


@app.route('/bitcoin')
def bitcoin():
    print('************************')
    print('This is the bitcoin function')
    return render_template('bitcoin.html')






app.run(debug=True)