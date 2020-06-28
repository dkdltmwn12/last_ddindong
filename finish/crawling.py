from bs4 import BeautifulSoup
from selenium import webdriver
import time
from urllib.request import urlopen
import requests
import json


def danggn(search):
    query_txt = search

    url = "https://www.daangn.com/search/{}".format(query_txt)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    dgdata = []
    n = 1
    for item in soup.select("a[href*=articles]"):
        dgdata.append("https://www.daangn.com" + item.get("href", "/"))
        n += 1
        if n > 6:
            break

    dgimgurl = []
    n = 1
    for i in soup.find_all(class_="card-photo"):
        dgimgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    dgtitle = []
    n = 1
    for i in soup.find_all("span", {"class": "article-title"}):
        dgtitle.append(str(i.text))
        n += 1
        if n > 6:
            break

    dgcost = []
    n = 1
    for i in soup.find_all("p", {"class": "article-price"}):
        dgcost.append(str(i.text))
        n += 1
        if n > 6:
            break

    return dgimgurl, dgdata, dgtitle, dgcost


def hellomarket(search):
    query_txt = search

    custom_header = {
        "referer": "https://www.hellomarket.com/search?q=${query_txt}",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    }

    url = "https://www.hellomarket.com/api/search/items?q={}&page=1".format(query_txt)

    req = requests.get(url, headers=custom_header)

    stock_data = json.loads(req.text)
    item_lists = stock_data["list"]

    htitle = []
    for i in range(7):
        if i == 3:
            continue
        htitle.append(item_lists[i]["item"]["title"])

    hcost = []
    for i in range(7):
        if i == 3:
            continue
        hcost.append(item_lists[i]["item"]["property"]["price"]["text"])

    himgurl = []
    for i in range(7):
        if i == 3:
            continue
        himgurl.append(item_lists[i]["item"]["media"]["imageUrl"])

    hdata = []
    count = 31
    for i in range(7):
        if i == 3:
            continue
        if count == 34:
            count = count + 1
        a = item_lists[i]["item"]["linkUrl"].split("/")
        whole_url = (
            "https://www.hellomarket.com/item/"
            + str(a[4])
            + "?viewPath=search_list&clickPath=search&feedPosition="
            + str(count)
        )
        count = count + 1
        hdata.append(whole_url)

    return himgurl, hdata, htitle, hcost


def sellit(search):
    query_txt = search

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("lan=ko_KR")
    path = "C:\\Users\\dydtj\\Desktop\\test\\chromedriver.exe"
    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    driver.get("https://www.withsellit.com/search?query=" + query_txt)

    full_html = driver.page_source
    soup = BeautifulSoup(full_html, "html.parser")

    sdata = []
    n = 0
    for item in soup.select("a[href*=products]"):
        sdata.append("https://www.withsellit.com" + item.get("ng-href", "/"))
        if sdata[n] == "https://www.withsellit.com/":
            del sdata[n]
            n = n - 1
        n = n + 1
        if n > 5:
            break

    simgurl = []
    n = 1
    for i in soup.find_all(class_="gdidx-img"):
        simgurl.append(i.find("img")["src"])
        n += 1
        if n > 6:
            break

    stitle = []
    n = 1
    for i in soup.find_all("div", {"class": "gdidx-name ng-binding"}):
        stitle.append(str(i.text))
        n += 1
        if n > 6:
            break

    scost = []
    n = 1
    for i in soup.find_all("div", {"class": "gdidx-original-price ng-binding"}):
        scost.append(i.text)
        n += 1
        if n > 6:
            break

    return simgurl, sdata, stitle, scost
