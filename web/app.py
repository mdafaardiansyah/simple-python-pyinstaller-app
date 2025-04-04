from flask import Flask, render_template, request, jsonify
import sys
import os

# Lebih robust path system
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sources_dir = os.path.join(parent_dir, 'sources')
sys.path.append(sources_dir)

import calc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    value1 = ''
    value2 = ''
    
    if request.method == 'POST':
        value1 = request.form.get('value1', '')
        value2 = request.form.get('value2', '')
        
        if value1 and value2:
            result = calc.add2(value1, value2)
    
    return render_template('index.html', result=result, value1=value1, value2=value2)

@app.route('/api/calculate', methods=['POST'])
def calculate_api():
    data = request.get_json()
    value1 = data.get('value1', '')
    value2 = data.get('value2', '')
    
    if not value1 or not value2:
        return jsonify({'error': 'Both values are required'}), 400
    
    result = calc.add2(value1, value2)
    return jsonify({'result': result})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)