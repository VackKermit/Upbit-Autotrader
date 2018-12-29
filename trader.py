import time
from pprint import pprint
from urllib.parse import urlencode
from requests import get, post, delete
from jwt import encode

ACCESS_KEY = "E10F3xqOUGAYxxFmExfGBo2xxx5Q1IsrpHqDszgx"
SECRET_KEY = "1DjcP3cRxk7J4ymY4xkDxcnt9R1hXRT68FHDv3x3"

# Start with "_" is private function normally
# Implicit promise of no use in external modules

##############################################################

def get_account():
    # check available for all accounts
    payload = {
        "access_key": ACCESS_KEY,
        "nonce": int(time.time() * 1000)
    }


    token = encode(payload, SECRET_KEY).decode()
    # Python3 are encoded with utf-8 basically

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://api.upbit.com/v1/accounts"
    resp = get(url, headers=headers)
    resp_data = resp.json()
    return resp_data

def orderable_info(market):
    # orderable information
    query = {
        "market": market
    }

    query_encoded = urlencode(query)

    payload = {
        "access_key": ACCESS_KEY,
        "nonce": int(time.time() * 1000),
        "query": query_encoded
    }

    token = encode(payload, SECRET_KEY).decode()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://api.upbit.com/v1/orders/chance?" + query_encoded
    resp = get(url, headers=headers)
    resp_data = resp.json()
    return resp_data

def order(market, side, volume, price, ord_type):
    # order
    query = {
        "market": market,
        "side": side,
        "volume": volume,
        "price": price,
        "ord_type": ord_type
    }

    query_encoded = urlencode(query)

    payload = {
        "access_key": ACCESS_KEY,
        "nonce": int(time.time() * 1000),
        "query": query_encoded
    }

    token = encode(payload, SECRET_KEY).decode()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://api.upbit.com/v1/orders"
    resp = post(url, headers=headers, json=query)
    resp_data = resp.json()
    return resp_data    

def order_list(state="wait", page=1):
    query = {
        "state": state,
        "page": page
    }

    query_encoded = urlencode(query)

    payload = {
        "access_key": ACCESS_KEY,
        "nonce": int(time.time() * 1000),
        "query": query_encoded
    }

    token = encode(payload, SECRET_KEY).decode()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://api.upbit.com/v1/orders?" + query_encoded
    resp = get(url, headers=headers)
    resp_data = resp.json()
    return resp_data

def order_cancle(uuid):
    query = {
        "uuid": uuid
    }

    query_encoded = urlencode(query)

    payload = {
        "access_key": ACCESS_KEY,
        "nonce": int(time.time() * 1000),
        "query": query_encoded
    }

    token = encode(payload, SECRET_KEY).decode()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = "https://api.upbit.com/v1/order?" + query_encoded
    resp = delete(url, headers=headers)
    resp_data = resp.json()
    return resp_data    

def ticker(markets):
    # ticker
    url = "https://api.upbit.com/v1/ticker?markets=" + markets
    resp = get(url)
    resp_data = resp.json()
    return resp_data

def candle_minute(market):
    # candle information for minute
    url = "https://api.upbit.com/v1/candles/minutes/1?market=" + market
    resp = get(url)
    resp_data = resp.json()
    return resp_data

##############################################################

def main():
    resp = order_cancle("0d3173e5-3a5a-42bf-ab26-951918ac15e8")
    pprint(resp)

if __name__ == '__main__':
    main()