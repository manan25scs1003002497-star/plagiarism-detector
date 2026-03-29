from flask import Flask, render_template, request
from utils import check_plagiarism

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        text1 = request.form["text1"]
        text2 = request.form["text2"]
        
        result = check_plagiarism(text1, text2)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
