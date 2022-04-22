from flask import Flask, Response, render_template
import json
import data

### 避免html模板与vue冲突
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',
        variable_end_string='%%',
        ))
    ###

app = Flask(__name__)

@app.route('/iotDatas')
def temperature():
    iotDatas = data.select()
    iotData = [{
	'temperature': data[0],
	'time': data[1],
	} for data in iotDatas ]
    js = json.dumps({
     	'iotDatas': iotData
     	})
    return Response(js, mimetype='application/json')

@app.route('/')    
def index():
    return render_template('vue.html')

app.run()
