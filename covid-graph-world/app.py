from flask import Flask, request, render_template
from covid import Covid
import requests
data = Covid()
Country = []
for i in data.list_countries():
    Country.append(i['name'].lower().replace(' ', '-'))

app = Flask(__name__, template_folder='tamplate')

@app.route('/')
def index():
    return render_template('index.html', option=Country)

@app.route('/find', methods=["GET"])
def all_Country():
    try:
        parm =  str(request.args.get('country')).replace('-', ' ')
        data_user = data.get_status_by_country_name(parm)
        data_user = f"return_html({data_user['confirmed']}, {data_user['deaths']}, {data_user['active']})"
        return render_template('index.html', find=data_user)

    except Exception:
        return render_template('ERROR.html')
    
 
if __name__ == '__main__':
    app.run('127.0.0.1',port=80)
