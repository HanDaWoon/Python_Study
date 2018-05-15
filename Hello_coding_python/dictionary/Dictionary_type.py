# {Key1:Value1, Key2:Value2, Key3:Value3 ...}

#딕셔너리 쌍 추가하기
a = {1: 'a'}
print(a)
a[2] = 'b'
print(a)
a['name'] = 'HDW'
print(a)
a[3] = [1, 2, 3]
print(a)

#딕셔너리 요소 삭제하기
del a[1]
print(a)

#딕셔너리에서 Key 사용해 Value 얻기
score = {'HDW': 50, 'HAR': 30}
print(score['HDW'], score['HAR'])

#Key 리스트 만들기(keys)
a = {'name': 'HDW', 'phone': '01097150310', 'birth': '1028'}
print(list(a.keys()))

#Value 리스트 만들기(values)
print(a.values())

#Key, Value 쌍 얻기(items)
print(a.items())

#Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)

#Key로 Value얻기(get)
a = {'name': 'HDW', 'phone': '01097150310', 'birth': '1028'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('x', 'default'))

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name': 'HDW', 'phone': '01097150310', 'birth': '1028'}
print('name' in a)
print('email' in a)