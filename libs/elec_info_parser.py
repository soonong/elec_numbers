from bs4 import BeautifulSoup

def elec_getInfo(lists):
    dict = {"등록번호": lists[0],  # 딕셔너리해서 각각의 값을 불러온다
            "등록일": lists[1].replace(".", "-"),
            "관할시도회": lists[2],
            "상호": lists[3],
            "대표자": lists[4],
            "소재지": lists[5],
            "전화번호": lists[6],
            "팩스번호": lists[7],
            "시공능력평가액": lists[8].replace(" ", ""),
            "지역순위": lists[9],
            "전국순위": lists[10],
            }

    return dict

def elec_info_parse(fanalPage):
    soup = BeautifulSoup(fanalPage, "html.parser")
    bbs = soup.find("div", {"class": "bbs"})
    trs = bbs.findAll("tr")

    lists = []
    for tr in trs:
        nums = tr.findAll("td")
        for num in nums:
            info = num.text
            lists.append(info)  # 인포를 리스트에 넣고


    dict = {}
    try:
        dict = elec_getInfo(lists)
        print(dict)
    except Exception as e:
        print("error-", e)
    return dict
