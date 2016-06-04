import requests
from bs4 import BeautifulSoup

"""
서울대학교 생협의 메뉴를 읽어오는 코드
"""
addr1 = "https://www.snuco.com/html/restaurant/restaurant_menu1.asp" # 직영식당
addr2 = "https://www.snuco.com/html/restaurant/restaurant_menu2.asp" # 위탁식당



class snuMenu():
    map1 = { # 직영식당 매핑
            "학관":"학생회관식당", "학생회관":"학생회관식당", "학생회관식당":"학생회관식당",
            "제3식당":"제3식당", "농식":"제3식당", "농대식당":"제3식당", 
            "긱식":"기숙사식당", "기숙사":"기숙사식당", "기숙사식당":"기숙사식당",
            "자하연식당":"자하연식당", "자하연":"자하연",
            "302동식당":"302동식당", "302":"302동식당",
            "솔밭간이식당":"솔밭간이식당", "솔밭":"솔밭간이식당",
            "동원관식당":"동원관식당", "동원관":"동원관식당",
            "감골식당":"감골식당", "감골":"감골식당"
            }
    map2 = { # 위탁식당 매핑
            "서당골":"서당골", 
            "두레미담":"두레미담", "두레":"두레미담",
            "301동식당":"301동식당", "301":"301동식당",
            "예술계식당":"예술계식당", "예술계":"예술계식당", "예술":"예술계식당",
            "공대간이식당":"공대간이식당", "공깡":"공대간이식당", "공간":"공대간이식당",
            "상아회관":"상아회관", "상아":"상아회관",
            "220동식당":"220동식당", "220":"220동식당"
            }       
    name = None         # [식당명]
    belong = 1       # [직영 1/위탁 2/잘못된 식당]
    time = None         # [아침/점심/저녁]


    def __init__(self, string):
        # 입력시 받은 문구를 [식당명]과 [아침/점심/저녁]으로 parsing한다.
        token = string.split()
        length = len(token)
        
        # 식당명과 소속 구하기
        if length == 1 or length == 2:
            self.name = self.map1.get(token[0], None)
            if not self.name:
                self.name = self.map2.get(token[0], None)
                belong = 2          # 위탁식당 소속
            if not self.name:
                belong = 3          # 잘못된 식당명
            
        if length == 2:
            # 인자가 두개 들어온 경우 [아침/점심/저녁] 인지 확인한다
            if token[1] == "아침" or token[1] == "점심" or token[1] == "저녁":
                time = token[1]
            # 올바르지 않은 경우, None으로 두고 아침/점심/저녁 메뉴를 모두 출력하게 한다


        output = str(self.name) + "의 [" + str(self.time) + "] 메뉴를 출력합니다."
        print(output)

    

    


