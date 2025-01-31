from flask import Flask, render_template, request, redirect, flash
import csv

app = Flask(__name__)

# Function to write into csv file
def writeCSV(row):
    with open("credentials.csv", 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)
    print(f"Credentials saved for {row[0]}")

# Function to verify login credentials from login
def verifyCredentials(userName, password):
    with open("credentials.csv", 'r') as csvfile:
        content = csv.reader(csvfile)
        for list in content:
            if list[0] == userName and list[2] == password:
                print("Credentials Verified!!")
                return True
    print("Invalid Credentials")
    return False


@app.route("/")
def home():
    """ 
    Add link to register and login page here.  
    """
    return render_template('form-index.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Ask for new user's details and
    Save it in csv file.
    """
    if request.method == 'POST':
        name = request.form.get('user_name')
        email = request.form.get('user_email')
        password = request.form.get('user_pw')
        
        row = [name, email, password]
        writeCSV(row)

        return redirect('login')
    

    else: 
        return render_template('form-register.html')



@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('user_name')
        password = request.form.get('user_pw')
        print(name, password)
        if verifyCredentials(name, password):
            return redirect(f'/dashboard/{name}')
        else:
            return redirect('login')
    else: 
        return render_template('form-login.html')
    
@app.route("/dashboard/<name>")
def dashboard(name):
    # name = request.form.get('user_name')
    return render_template('form-dashboard.html', user = name)


if __name__ == '__main__':
    app.run(debug=True)
