from flask import Flask, request, Response
import json
from flask_cors import CORS

from recommendation_spend_behavior import Spend_behavior_Prediction

app = Flask(__name__)
CORS(app)

predict = Spend_behavior_Prediction()

@app.route("/", methods = ["GET"])
def handle_recommend():
    customer_id = request.args.get("customer_id")
    print(customer_id)
    #TODO recommend products based on this id and respond
    ret = {customer_id: ['product1', 'product2', 'product3']}
    resp = Response(response=json.dumps(ret), status=200, mimetype="application/json")
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

