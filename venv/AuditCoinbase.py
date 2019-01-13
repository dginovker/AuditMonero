import json
import requests

# at height 1742081 emission was 16697487 according to Moneroblocks.info https://archive.fo/fTWWL CMC https://archive.fo/U0XfN

START = 0
END = 1742081

previousAvgOf10 = 0
sum = 0

url = "http://127.0.0.1:18081/json_rpc"
headers = {'Content-Type': 'application/json'}

for i in range(END):
    payload = {
        "jsonrpc" : "2.0",
        "id" : "0",
        "method" : "get_coinbase_tx_sum",
        "params": {
        "height" : i,
        "count" : 1
        }
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()


    sum += response["result"]["emission_amount"]

print("Total Monero minted from block " + str(START) + " to " + str(END) + " was " + str(round(sum/10**13, 2)) + " XMR")