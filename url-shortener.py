from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)

#print(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        
        if request.form['code'] in urls.keys():
            flash('That short name has already been taken. Please selecr another name.')
            return redirect(url_for('home'))
        
        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
  
if __name__ == '__main__':  # Script executed directly?
#    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
     app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
        
        
