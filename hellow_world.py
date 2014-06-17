app = flask(__name__)

#code goes here

@app.route("/")
def helloworld():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)