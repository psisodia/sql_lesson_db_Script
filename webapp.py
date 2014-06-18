from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

#code goes here

@app.route("/")
def get_github():
    return render_template("get_github.html")

# @app.route("/student")
# def get_student_by_github():
#     hackbright_app.connect_to_db()
#     student_github = request.args.get("student")
#     row = hackbright_app.get_student_by_github(student_github)
#     html = render_template("student_info.html", first_name=row[0],
#                                                 last_name=row[1],
#                                                 github=row[2])
#     return html

@app.route("/student")
def get_student_grades():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    student_info = hackbright_app.get_student_by_github(student_github)
    student_grades = hackbright_app.get_student_grades(student_github)
    html = render_template("student_info.html", first_name=student_info[0],
                                                last_name=student_info[1],
                                                github=student_info[2],
                                                project_title=student_grades[0],
                                                grades=student_grades[1])
    return html
if __name__ == "__main__":
    app.run(debug=True)