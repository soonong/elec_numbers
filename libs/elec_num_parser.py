from bs4 import BeautifulSoup

def elec_num_parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    div = bsObj.find("div", {"class": "userList"})
    lis = div.findAll('li')
    links = []
    for li in lis:
        link = li.find('a')['onclick'].replace("javascript:js_detailAction('", "").replace("');", "")
        links.append(link)
    return links
