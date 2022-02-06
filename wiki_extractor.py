import argparse
from ast import arg, parse
import requests
from bs4 import BeautifulSoup
import re
import json

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', dest='keyword', type=str, help='Name of the keyword to search')
    parser.add_argument('--num_urls', dest='num_url', type=int, help='Number of URLs to search')
    parser.add_argument('--output', dest='output_file', type=str, help='Name of the file to output data')
    args = parser.parse_args()
    string = args.keyword
    res = string.split(" ")
    final_string = ""
    for i in res:
        if final_string == "":
            final_string+=f"{i}"
        else:
            final_string+=f"+{i}"
    limit = 20
    results = 0
    hrefList = []
    textList = []
    maxLimit = args.num_url
    final_data = []
    while(len(hrefList) < maxLimit):
        url = f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit={limit}&offset={limit*results}&profile=default&search={final_string}&ns0=1"
        results+=1
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find_all('li', attrs = {'class' : 'mw-search-result'})
        for i in table:
            res = i.find('div', attrs={'class' : 'mw-search-result-heading'})
            href = res.find('a')['href']
            hrefList.append(f"https://en.wikipedia.org{href}")
            f = res.find('a')
            textList.append(f.get_text())
    hrefList = hrefList[:maxLimit]
    textList = textList[:maxLimit]
    for i in hrefList:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, 'html5lib')
        res = soup.find("div", attrs={"class" : "mw-parser-output"})
        res_data = res.find_all('p')
        a = ''
        for j in res_data:
            if (j.attrs == {}):
                text = cleanhtml(j.prettify())
                text = re.sub('\n', '', text)
                text = re.sub('\[\d+\]', '', text)
                text = re.sub('\s+', ' ', text)
                text = re.sub('\\\"', "", text)
                if(len(text) < 100):
                    continue
                a+=text
                if(len(a) >= 500):
                    break
            elif(j['class'][0] == "mw-empty-elt"):
                continue
        final_data.append({
            'url' : i,
            'paragraph' : a
        })
    file_data = json.dumps(final_data)
    with open(f"{args.output_file}", 'a+') as f:
        f.write(file_data)