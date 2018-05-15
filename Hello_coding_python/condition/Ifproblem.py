id = input("id:")
N_id = ['HDW', 'HAR', 'HFA']
N_pw = ['zxc', 'asd', 'qwe']
if id in N_id:
    print("Hello, %s" %(id))
    pw = input("pw:")
    if pw in N_pw:
        print("success login")
    else:
        print("Who are you!")
else:
    print("Who are you!")