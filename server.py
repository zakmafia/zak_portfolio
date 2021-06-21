from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def default_page():
    return render_template("index.html")

@app.route("/<string:html_page>")
def html_pages(html_page):
    return render_template(html_page)

def write_to_text(data):
    with open('database.txt', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}")

def write_to_csv_file(data):
    with open('database.csv', mode="a") as database1:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv_file(data)
        return redirect("thankyou.html")
        
    else:
        print("Something went wrong!")