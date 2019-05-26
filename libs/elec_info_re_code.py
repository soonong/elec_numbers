# 저장된 파일을 포문으로 돌리니까..
# 한 엑셀칸에 있는 8 자리 숫자가 먼저 통째로 호츌된후
# 8자리가 각각 1글자씩 재호출 됨
# 그래서 정규식을 써서 저장된 파일안의 자료를
# 일정한 규칙으로 리스트화 하는 함수
# 먼가 조잡해보임


import re

def elec_info_code():
    file = open("elec_codes.csv")
    text = file.read()
    matches = re.findall("[0-9]{8}", text)
    result = []
    for match in matches:
        result.append(match)
    return result
