from flask import Flask, request
from covid import Covid
import requests
javascript_mudle = requests.get('https://pastebin.com/raw/bVr4B0ny').text
javascript_Graph = requests.get('https://pastebin.com/raw/HgUcSKM0').text

data = Covid()
Country = []
optonis = []

for i in data.list_countries():
    Country.append(i['name'].lower())
    
for i in data.list_countries():
    optonis.append(f"<option value='{i['name'].lower()}'>{i['name'].lower()}</option>")
apps = Flask('covid')

@apps.route('/')
def index():
    return f"""<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.cssscript.com/demo/lightweight-modal-dialog-javascript-library-z-modal/z-modal/z-modal.min.css">
<body>
<form class="w3-container w3-card-4" action="/find" method="GET">
  <h1 style="font-family:monospace;;" >Yow Want Show More Datelites <strong style="color:blue;font-size:50px;"" id="demo1">click me</strong></h1>
  <script>{javascript_mudle}</script>
  <select class="w3-select" name="country">
    <option value="" disabled selected>Choose your country</option>
    {optonis}
  </select>

  <p><a href="#more" class="w3-btn w3-green " style="border: 2px solid #DCDCDC;width:auto;" >Read More</a>
  <button class="w3-btn w3-blue " style="border: 2px solid #DCDCDC;width:auto;" >search</button>
  <a class="w3-btn w3-blue-grey " style="border: 2px solid #DCDCDC;width:auto;" href="https://github.com" target="_blank">source code</a></p>
</form>
    <div id="more">
    <img src="https://media3.giphy.com/media/jOv9vznXSxr6Le6B75/giphy.gif?cid=ecf05e47yacvn7tx5p78d4e6k8m3o4lf5hewh19x056trpvd&rid=giphy.gif" alt="funny GIF" width="100%">
    </div>
</body>
</html>
"""
@apps.route('/find', methods=["GET"])
def all_Country():
    try:
        # 
        ERROR = """<html lang="en"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 HTML Template by Colorlib</title><link href="https://fonts.googleapis.com/css?family=Montserrat:400" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Chango" rel="stylesheet"><link type="text/css" rel="stylesheet" href="https://colorlib.com/etc/404/colorlib-error-404-13/css/style.css"></head><body><div id="notfound"><div class="notfound"><div><div class="notfound-404"><h1>!</h1></div><h2>Error<br>404</h2></div><p>The page you are looking for might have been removed had its name changed or is temporarily unavailable. <a href="/">Back to homepage</a></p></div></div><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13"></script><script> window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'UA-23581568-13');</script></body></html> <script> setTimeout("window.location.href = '/'", 3000)</script> """
        parm =  str(request.args.get('country'))
        print(parm)
        if parm.lower() in Country:
            data_user = data.get_status_by_country_name(parm)
            new = javascript_Graph.replace('[number_confirmed]', str(data_user['confirmed']))
            new = new.replace('[name_country]', data_user['country'])
            new = new.replace('[number_active]', str(data_user['active']))
            new = new.replace('[number_deaths]', str(data_user['deaths']))
            return f"""<html><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"><script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script><script>{new}</script><body><div id="chartContainer" style="height: 500px; width: 100%;"></div><p><a class="w3-btn w3-blue" style=" margin: 0 auto;width:100%;" href = '/'"> back</a> </body></html> """
        
        else:
            return ERROR
    except Exception as e:
        print(e)
        return ERROR
    
 
apps.run('127.0.0.1',port=80,debug=True)
