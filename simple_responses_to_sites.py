import requests

sites = ['https://lc.rt.ru']
N = 100

for site in sites:
        for i in range(N):
                    response = requests.get(site)
                            print(i, site, response.status.code)
