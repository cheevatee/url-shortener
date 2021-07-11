from flask import Flask, render_template, request

app = Flask(__name__)

#print(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not valid'
  
if __name__ == '__main__':  # Script executed directly?
#    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
     app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
        
        
