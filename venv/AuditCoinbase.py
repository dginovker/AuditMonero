import json
import requests

# at height 1742081 emission was 16697487 according to Moneroblocks.info https://archive.fo/fTWWL CMC https://archive.fo/U0XfN

START = 0
END = 1742081
#END = 15 #For testing purposes

VERBOSE = True
SCARY_MULTIPLIER = 2

sum = 0

url = "http://127.0.0.1:18081/json_rpc"
headers = {'Content-Type': 'application/json'}

previous10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def scaryHigh(emission):
    emission = emission/10**13
    if (emission > SCARY_MULTIPLIER*avgOf10()):
        return True;
    return False;


def updatePrevious10(emission):
    emission = emission/10**13
    for x in range(9):
        previous10[x] = previous10[x+1]
    previous10[9] = emission


def avgOf10():
    total = 0
    for x in previous10:
        total += x

    return total/10

f = open("CoinbaseMints.csv", "w")
f.write("Block number,Coinbase emission,Total fees\n")

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

    updatePrevious10(response["result"]["emission_amount"])

    if scaryHigh(response["result"]["emission_amount"]):
        print("WARN: Block " + str(i) + " has abnormally high reward of " + str(round(response["result"]["emission_amount"]/10**13, 2)) + " with fee total of " + str(response["result"]["fee_amount"]) + "(previous avg. was " + str(avgOf10()) + ")\n\t" + str(response) + "\n")

    if response["result"]["status"] != 'OK':
        print("WARN: Block " + str(i) + " did not give the OK!\n\t" + str(response) + "\n")

    if i%10000 == 0 and VERBOSE:
        print("Currently finished parsing block " + str(i) + ". Total emission is currently " + str(round(sum/10**13, 2)) + " XMR")

    f.write(str(i) + "," + str(response["result"]["emission_amount"]) + "," + str(response["result"]["fee_amount"]) + "\n")

print("\n\nTotal Monero minted from block " + str(START) + " to " + str(END) + " was " + str(round(sum/10**13, 2)) + " XMR")