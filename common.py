# fool the server into thinking we're chrome, otherwise will return HTTP 418
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}


# http://free-proxy.cz/en/proxylist/country/CN/http/ping/all
# Used to sidestep IP flags. Update as needed
# Thanks to https://stackoverflow.com/a/63095099/10176917

def get_new_proxy():
    return {"http": f"http://{proxies[random.randrange(0, len(proxies))]}"}


proxies = [
    '114.236.81.176:8008',
    '106.75.86.177:80',
    '121.226.248.241:8118',
    '219.138.229.131:9091',
    '120.26.14.114:8888',
    '121.37.227.255:8888',
    '182.103.254.196:8118',
    '120.26.0.11:8880',
    '113.195.12.168:8085',
    '171.110.10.40:8800',
    '124.204.33.162:8000',
    '58.221.193.74:8888',
    '39.175.75.8:30001',
    '39.175.92.35:30001',
    '39.175.84.157:30001',
    '39.175.75.144:30001',
    '183.247.202.226:30001',
    '183.247.194.121:30001',
    '39.175.75.15:30001',
    '120.196.179.73:9091',
    '39.175.67.28:30001',
    '183.247.202.208:30001',
    '221.131.158.246:8888',
    '183.247.194.229:30001',
    '39.175.94.90:30001',
    '183.247.199.131:30001',
    '218.201.71.75:8060',
    '183.247.211.50:30001',
    '183.247.199.215:30001',
    '223.96.90.216:8085',
    '27.220.136.254:8888',
    '125.118.28.114:81',
    '61.191.56.60:8085',
    '49.7.19.74:80',
    '180.76.237.75:80',
]
