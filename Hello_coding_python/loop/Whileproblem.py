name = input("때릴사람의 이름을 말하세요.\n")
hitnum = int(input("몇대를 때리시겠습니까?\n"))
namehit = 0
while namehit < hitnum:
    namehit = namehit + 1
    print("%s 을(를) %d번 때렸습니다." % (name, namehit))
    if namehit == hitnum:
        print("%s 이(가) 기절했습니다." %name)
    if namehit < 10:
        print("%s  이(가) 매우 아파합니다." %name)
    if 10 < namehit < 100:
        print("%s 이(가) 눈을 못 뜹니다." %name)