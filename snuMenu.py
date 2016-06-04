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

    soup1 = None
    soup2 = None
    map_req={ # 식당 소속에 따른 크롤링 매핑
            1:requests.get(addr1, verify=False), 2:requests.get(addr2, verify=False), 3:None
            }
    map_soup={ # 식당 소속에 따른 코드 추출 결과 매핑
            1:soup1, 2:soup2
            }


    def __init__(self, string):
        # instance에 고유한 변수들을 생성한다
        self.name = None        # [식당명]
        self.belong = 1         # [직영 1/위탁 2/잘못된 식당]
        self.time = None        # [아침/점심/저녁]

        # 입력시 받은 문구를 [식당명]과 [아침/점심/저녁]으로 parsing한다.
        token = string.split()
        length = len(token)
        
        if length != 1 and length != 2:
            print("잘못된 명령어")
            return

        
        # 식당명과 소속 구하기
        self.name = snuMenu.map1.get(token[0], None)
        if not self.name:
            self.name = snuMenu.map2.get(token[0], None)
            self.belong = 2          # 위탁식당 소속
        if not self.name:
            self.belong = 3          # 잘못된 식당명
   
        if length == 2:
            # 인자가 두개 들어온 경우 [아침/점심/저녁] 인지 확인한다
            # 올바르지 않은 경우, None으로 두고 아침/점심/저녁 메뉴를 모두 출력하게 한다
            if token[1] == "아침" or token[1] == "점심" or token[1] == "저녁":
                time = token[1]

        output = str(self.name) + "의 [" + str(self.time) + "] 메뉴를 출력합니다."
        print(output)

    def update(self):
        # 식단 정보 업데이트
        req = snuMenu.map_req[self.belong]
        req.encoding = "euc-kr"
        s_raw = BeautifulSoup(req.text, "html.parser")
        s_raw = s_raw.find_all('tbody')
        soup = s_raw[3].find_all('tr')
        print(soup)
        snuMenu.map_soup[self.belong] = soup


