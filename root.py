from flask import Flask, render_template
app=Flask('MyPage')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")   

@app.route("/journey")
def journey():
    return render_template("journey.html")   
        

if __name__ == '__main__':
    app.run(debug='False')   

