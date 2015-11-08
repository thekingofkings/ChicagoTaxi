"""

Author: Hongjian
date: 11/7/2015

Chicago map

"""



from flask import Flask, request, jsonify
from flask import render_template
from Block import Block


app = Flask(__name__)



@app.route('/')
def main_map():
    return render_template('maps.html')
    


@app.route('/getCAs')
def getCAs():
    cas = Block.createAllCAObjects()
    ca_bounds = {}
    for t, ca in cas.items():
        l = list(ca.polygon.exterior.coords)
        ca_bounds[t] = l
    return jsonify(ca_bounds)
    
    
if __name__ == '__main__':
    app.run(debug=True)