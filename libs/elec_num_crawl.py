import requests

def elec_num_crawl(num):
    url = "http://m.keca.or.kr/service/service07.do?menuCd=4051&currentPageNo={}" \
          "&license=&gubun=page&searchSido=&searchGubun=company&searchText=&CSRFToken=92d2be8b-4d72-419a-a4cd-a21f70a8bd04".format(
        num)
    data = requests.get(url)
    print(data, url)
    result = data.content
    return result