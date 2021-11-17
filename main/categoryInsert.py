from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('mongodb://test:test@13.125.132.62', 27017)
db = client.catchup

doc = [
    {
        'type': 1,
        'title': '씨앗 디노',
        'step': '씨앗을 심고 새싹이 될 때까지 정성을 들이는 단계',
        'sub1': '더 나은 내일로 나아갈 무한한 잠재력을 지니고 있는 당신. 어떤 꽃으로 피어날지는 당신의 손에 달려있어요. 물을 주고, 햇볕을 쪼이면 곧 새싹이 모습을 드러낼 거예요.',
        'sub2': '내가 어떤 사람인지, 어떻게 꽃을 피워내야 할 지 모르겠다면 다른 사람의 이야기를 듣는 것도 좋은 방법! 모든 것은 나로부터 시작되니까요.',
        'img': 'https://dinoimage.s3.ap-northeast-2.amazonaws.com/dino_1.png',
        'id': [1, 2, 3]
    },
    {
        'type': 2,
        'title': '새싹 디노',
        'step': '꽃이 피어날 미래를 기대하며 싱그러움으로 가득한 단계',
        'sub1': '땅 속에 묻힌 씨앗이 싹을 틔우기까지 많은 노력을 했을 당신. 어떤 방향으로 나아가야할지 감을 잡았군요.',
        'sub2': '하지만 방심은 금물! 아직은 힘이 약한 새싹이 단단하게 성장하기 위해선 전문가의 도움이 필요할 수 있어요. 함께 구체적인 진로를 고민해줄 누군가가 있다면 도움이 될 거예요.',
        'img': 'https://dinoimage.s3.ap-northeast-2.amazonaws.com/dino_2.png',
        'id': [1, 2]
    },
    {
        'type': 3,
        'title': '꽃봉오리 디노',
        'step': '더 풍성하고 향기롭게 꽃 피우기 위해 준비하는 단계',
        'sub1': '이제 꽃을 피울 준비가 다 되었어요. 내가 좋아하는 게 무엇인지 알고, 무엇을 해야 하는 지 아는 당신.',
        'sub2': '다양한 실무경험을 할 수 있는 프로그램에서 당신의 능력을 십분 발휘해보는 건 어떨까요? 그동안의 시도와 노력들이 이번 기회를 통해 더욱 빛나게 될 거예요!',
        'img': 'https://dinoimage.s3.ap-northeast-2.amazonaws.com/dino_3.png',
        'id': [4, 5, 6]
    },
    {
        'type': 4,
        'title': '꽃 디노',
        'step': '완전히 꽃 피워 실전에 투입될 준비를 마친 단계',
        'sub1': '앞으로 한 걸음도 채 남아있지 않네요! 화분이 꽃을 더 아름답게 만들어 주듯이 우리에게도 약간의 포장이 필요할 것 같아요.',
        'sub2': '당장 취업을 앞둔 당신의 2% 부족함을 채워줄 다양한 특강이 준비되어 있어요. 전문가와 함께 포트폴리오, 자기소개서, 면접을 준비하고 최신 취업 트렌드 및 기업정보를 알아볼까요? ',
        'img': 'https://dinoimage.s3.ap-northeast-2.amazonaws.com/dino_4.png',
        'id': [7, 8, 9]
    }
]
db.category.drop()
db.category.insert_many(doc)
