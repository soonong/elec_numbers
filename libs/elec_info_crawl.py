import requests

def elec_info_crawl(num):
    url = "http://www.keca.or.kr/ecic/ad/ad0101D.do?menuCd=6047&currentPageNo=1&license={}&gubun=detail&sido=51&hoeyn=&searchSido=&searchSigungu=&searchGubun=company&searchText=&CSRFToken=8ab9292a-389d-40b3-979a-4a7815959e3a".format(
        num)
    req = requests.get(url)
    cont = req.content
    return cont