from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/amortization/payment/", methods=['POST'])
def get_payment_amount():
    if not request.json:
        abort(400)
        
    p = request.json.get('principal', 0)
    r = request.json.get('rate',0.0)
    n = request.json.get('years', 0)
    m = request.json.get('periods', 0)
   
    Nm = n * m
    rate_per_period = r / m
    
    numerator = (rate_per_period * ((1 + rate_per_period) ** Nm)) 
    divisor = ((1 + rate_per_period) ** Nm) - 1
    pmt = p * (numerator / divisor) 

    return  jsonify({ "payment_amount":  round(pmt, 2)  })
 
if __name__ == "__main__":
    app.run()

