from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def init():
    if request.method == 'GET':
        return render_template("Home.html")
    elif request.method == 'POST':
        username=request.form['username']
        return render_template("display.html", name=username)
if __name__=='__main__':
  app.run(host='0.0.0.0',debug = True)