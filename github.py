from flask import Flask,render_template,request
import requests

app = Flask(__name__)

base_url ="https://api.github.com/users/"

@app.route('/',methods = ['GET','POST'])
def github():
    if request.method == 'POST':
        githubname = request.form.get('githubname')
        response = requests.get(base_url + githubname)
        repos = requests.get (base_url + githubname + "/repos")
        repos_info = repos.json()
        app.logger.info(repos_info)
        response_info = response.json()
        app.logger.info(response_info)
        if "message" in response_info:
            return render_template ('index.html', error = "Please try again that your entered username....")
        return render_template('index.html',user=response_info,repos=repos_info)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)