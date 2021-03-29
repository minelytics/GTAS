import json

import requests
from bs4 import BeautifulSoup

# headers = requests.utils.default_headers()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "edi-dir-ad=1; PHPSESSID=otavjlu47dfff2961llvuvkid9; _ga=GA1.2.1396582637.1616484300; _gid=GA1.2.845304958.1616484300; _lfa=LF1.1.39f2d18227f8d45c.1616487675295; edi-cnt=12:12; SIGNUP_REF=edifact; TawkConnectionTime=0; __tawkuuid=p::.truugo.com::g6/7QLc8/a3Ep3cbJC2zktOFeFme8jTxPxx7LdZIZO/X4qE4V8ZCpT2BVKZCrexo::2",
    "Host": "www.truugo.com",
    "If-Modified-Since": "Wed, 24 Mar 2021 07:34:32 GMT",
    "Referer": "https://duckduckgo.com/",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
}

url = "https://www.truugo.com/edifact/d02b/cl0065/"

html_content = requests.get(url, headers=headers).text

print(html_content)

# soup = BeautifulSoup(html_content, "html.parser")
# # print(soup.find_all("tr"))
# cl_name = soup.find("h1").text.split(" ")[-1]
# cl_file = f"../codelists/codelist_{cl_name}.json"
#
# description = soup.find("h2").text
#
# codelist = dict()
#
# for cl in soup.find_all("tr"):
#     cd = cl.find("td", attrs={"class": "cd"}).text
#     name = cl.find("div", attrs={"class": "name"}).text
#     desc = cl.find("div", attrs={"class": "desc"}).text
#
#     codelist[cd] = {
#         "name": name,
#         "desc": desc
#     }
#
# with open(cl_file, "w") as json_file:
#     json.dump(codelist, json_file, indent=4, sort_keys=False)
#
# print(f"{cl_file} created successfully")
