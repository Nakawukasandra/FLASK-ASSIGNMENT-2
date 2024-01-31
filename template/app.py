from flask import Flask  ,render_template , request

app = Flask (__name__)


@app.route('/')
def home():
    return render_template("home.html")

#Routing
@app.route('/about')
def about():
    return render_template('about.html')
 

@app.route('/Contact')
def Submission():
    return render_template('contact.html')



@app.route('/User/<Username>')
def Username(Sandra):
    return f'User,{Sandra}! Thats her name.'

#Form
@app.route('/submit' , methods =['GET' ,'POST'])
def submit():
           if request . method == 'POST' :
            name = request . form['name']
            email =request.form ['email']
            return f'Thank you {name} !We received your submission with email: {email}'
            return render_template ('Submissionform.html')

if -__name__ == '__main__' :
     app.run(debug=True)
