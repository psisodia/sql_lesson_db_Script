from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

#code goes here

@app.route("/")
def get_student_by_github():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    return hackbright_app.get_student_by_github(student_github)
    
if __name__ == "__main__":
    app.run(debug=True)