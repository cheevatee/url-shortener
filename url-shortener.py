from flask import Flask, render_template

app = Flask(__name__)

#print(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'This is a url-shortener app.'
  
if __name__ == '__main__':  # Script executed directly?
#    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
