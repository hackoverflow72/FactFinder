
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def LandingPage():
    return render_template('home.html')

@app.route('/home')
def hello_world():
    return render_template('home.html')

res = {'prompt' : '', 'data' : 0}
@app.route('/factchecker', methods = ["GET"])
def factchecker():
    res['prompt'] = ''
    res['data'] = 0
    return render_template('factchecker.html', data = res)
    
@app.route('/factchecker', methods = ["POST"])
def result():
    res['prompt'] = request.form['prompt']
    if res['data'] != "" :res['data'] = 1
    else : res['data'] = 0
    return render_template('factchecker.html', data = res)
    

# @app.route('/factchecker', methods = ["POST"])
# def result():
#     res = request.form['prompt']
#     print(res)
#     return render_template('factchecker.html',data = res )
    

if __name__ == '__main__':
    app.run(debug=True)