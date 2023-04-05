from flask import Flask, render_template_string, request, jsonify
from web3 import Web3
from decimal import Decimal
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire Flask app

# The rest of your app.py code



@app.route('/')
def index():
    with open("index.html", "r") as f:
        index_content = f.read()
    return render_template_string(index_content)

@app.route('/load-data', methods=['GET'])

def load_data():
    eth_address = request.args.get('address')
    
    # Check if the address is not empty
    if not eth_address:
        return jsonify({"error": "Empty address"}), 400
  
    provider_url = "https://eth-mainnet.g.alchemy.com/v2/FmCDwUEtFiPsWb4Ru6c_srky6kJyfVR8"
    w3 = Web3(Web3.HTTPProvider(provider_url))

    balance = w3.eth.get_balance(eth_address)
    eth_balance = w3.from_wei(balance, 'ether')

    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(api_url)
    price_data = response.json()
    eth_price_usd = price_data["ethereum"]["usd"]
    eth_price_decimal = Decimal(eth_price_usd)

    # Print the eth_price_usd variable
    print("ETH Price USD:", eth_price_usd)

    portfolio_value = eth_balance * eth_price_decimal

    return jsonify({
        'address': eth_address,
        'eth_balance': str(eth_balance),
        'eth_price_usd': '{:.2f}'.format(eth_price_decimal),
        'portfolio_value': str(portfolio_value)
    })



if __name__ == '__main__':
    app.run(debug=True)
