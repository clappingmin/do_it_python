import json

#Test용 python Dictionary
customer = {
    'id' : 152352,
    'name' : '강진수',
    'history' : [
        {'date':'2015-03-11','item':'iPone'},
        {'date':'2016-02-23','item':'Monitor'}
    ]
}
#JSON 인코딩
# jsonString = json.dumps(customer) #dumps는 메모리에 로드하는거

#json.dump 파일로 바로 저장
with open('./basic/quiz/data.json','wt') as f:
    json.dump(customer,f,indent=4) #indent : 들여쓰기 해줘서 보기 좋음

