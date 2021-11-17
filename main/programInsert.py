from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('mongodb://test:test@13.125.132.62', 27017)
db = client.catchup

doc = [
    {
        "title": "제로베이스",
        "desc": "전문 직업상담사와 함께 ‘나’를 알아가고 ‘나의 미래’를 설계해보자!",
        "img": "http://www.youtheroom.kr/editor/upload/img/1625474438.png",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1625474399&status=&search=",
        "id": 1
    },
    {
        "title": "아무튼, 기대",
        "desc": "1:1 맞춤 상담, 자기 탐색, 취업 역량 강화 등을 통해 나다움을 찾는 과정",
        "img": "http://www.youtheroom.kr/editor/upload/img/1636611727.png",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1636422846&status=&search=",
        "id": 2
    },
    {
        "title": "토닥진로코디네이터",
        "desc": "청년이룸의 진로 코디네이터와함께하는 전문 진로상담 프로그램",
        "img": "http://www.youtheroom.kr/editor/upload/img/1604031777.jpg",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1604025811&status=&search=%ED%86%A0%EB%8B%A5",
        "id": 3
    },
    {
        "title": "시리즈 D",
        "desc": "협업 스킬부터 현직자 커리어 멘토와 함께 완성해 나가는 나만의 프로젝트 경험!",
        "img": "http://www.youtheroom.kr/editor/upload/img/1627461029.png",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1627459083&status=&search=",
        "id": 4
    },
    {
        "title": "미니인턴",
        "desc": "기업에서 실제 고민하고 있는 문제를 과제로 수행하는 2주  단기 실무역량 교육 프로그램",
        "img": "http://www.youtheroom.kr/editor/upload/img/1631873283.png",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1631873148&status=&search=",
        "id": 5
    },
    {
        "title": "자격증 교육",
        "desc": "실전에 앞서 스킬을 갈고 닦을 수 있는 다양한 자격증 교육",
        "img": "",
        "url": "",
        "id": 6
    },
    {
        "title": "자소서 쓱강",
        "desc": "MBTI 전문 강사님과 함께 성격 유형별 취업 전략과 자기소개서 작성법에 대해 알 수 있는 시간",
        "img": "",
        "url": "",
        "id": 7
    },
    {
        "title": "이루JOB",
        "desc": "언택트 시대, VR/AI 면접 체험을 통해 취업의 꿈을 이뤄보자!",
        "img": "http://www.youtheroom.kr/editor/upload/img/1630904775.png",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1618306845&status=&search=%EC%9D%B4%EB%A3%A8",
        "id": 8
    },
    {
        "title": "슬기로운 취업스쿨",
        "desc": "PT 발표, 보고서 작성 방법 여기 다 있다! 당당한 예비 직장인이 되고 싶은 ‘취린이’ 모여라!",
        "img": "http://www.youtheroom.kr/editor/upload/img/1603773275.png",
        "url": "http://www.youtheroom.kr/product/item.php?ca_id=10&it_id=1603773183&status=&search=%EC%8A%AC%EA%B8%B0%EB%A1%9C%EC%9A%B4",
        "id": 9
    }

]
db.program.drop()
db.program.insert_many(doc)
