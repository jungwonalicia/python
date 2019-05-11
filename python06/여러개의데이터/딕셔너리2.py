사전 = {'apple':'사과', 
      'banana':'바나나',
      'melon':'메론'
      }
#값 변경
사전['apple'] = '푸른사과'

#값 제거
del 사전['apple']

for key in 사전:
    print(사전[key])

#값 추가
#사전.append() 사용 불가
사전['computer'] = '컴퓨터'
for key in 사전:
    print(사전[key])
    
print(사전.keys())
print(사전.values())






