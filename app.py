from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")

@app.route('/aml', methods=['GET','POST'])
    def aml():
        request.values['p1']
        
        import urllib.request
        import json
        import os
        import ssl

        def allowSelfSignedHttps(allowed):
        # bypass the server certificate verification on client side
        if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context

         allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

            # Request data goes here
            data = {
            "Inputs": {
            "WebServiceInput0":
            [
                {
                    'Pregnancies': "6",
                    'Glucose': "148",
                    'BloodPressure': "72",
                    'SkinThickness': "35",
                    'Insulin': "0",
                    'BMI': "33.6",
                    'DiabetesPedigreeFunction': "0.627",
                    'Age': "50",
                    'Outcome': "1",
                },
            ],
        },
        "GlobalParameters": {
        }
        }

        body = str.encode(json.dumps(data))

        url = 'http://eb89f27c-7858-42a3-9302-6b91a14d2232.eastasia.azurecontainer.io/score'
        api_key = 'IrIkhtbwxAes12yqDvRHKMsSkfzPidy3' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        htmlstr="<html><body>"

        try:
        response = urllib.request.urlopen(req)

            result = response.read()
            htmlstr=htmlstr+"依據您輸入的參數，經過分析模型比對，罹患糖尿病的風險為"
            htmlstr=htmlstr['Results']['WebServiceOutput0'][0]['Scored Probabilities']
            print(result)
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))

            htmlstr=htmlstr+"</body></html>"
    return htmlstr


@app.route('/<name>')
def hello(name):
    return "Hello" + name + "!!!" 

if __name__=="__main__":
    app.run()