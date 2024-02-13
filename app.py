from flask import Flask,render_template,request
  
app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Blind',methods=['POST'])
def Blind_btn():
    if request.method=='POST':
        return render_template('blind.html')
    
@app.route('/Deaf',methods=['POST'])
def deaf_btn():
    if request.method=='POST':
        return render_template('deaf.html')
    
if __name__=="__main__":
    app.run(debug=True)