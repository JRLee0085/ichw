#!/usr/bin/env python
# coding: utf-8

# In[3]:


from urllib.request import urlopen
# 引入后续打开URL所需模块
def before_space(s):
    s=s.split(" ",1)
    a=s[0]
    return a
# 从含有数值和货币名称的字符串中分离出数值
def get_from(s):
    s=s.replace(", ",",")
    s=s.replace(" : ",":")
    s=s.replace(",",":")
    s=s.replace("{ ","{")
    s=s.replace(" }","}")
    if s.find("invalid")==-1:
        list1=s.split(":")
        n1=len(list1)
        for i in range(n1):
            x=list1[i].find(" ")
            if x!=-1:
                y=list1[i]
                break
            else:
                pass
        n2=len(y)
        y="'"+y[1:n2-1]+"'"  
    else:
        y=""  
    
    return y
# 从decode出的字符串中找出含有想要被兑换的货币数值与名称的信息
def get_to(s):
    s=s.replace(", ",",")
    s=s.replace(" : ",":")
    s=s.replace(",",":")
    s=s.replace("{ ","{")
    s=s.replace(" }","}")
    if s.find("invalid")==-1:
        list1=s.split(":")
        n1=len(list1)
        i=n1-1
        while 0<=i:
            x=list1[i].find(" ")
            if x!=-1:
                y=list1[i]
                i=i-1
                break
            else:
                i=i-1
        n2=len(y)
        y="'"+y[1:n2-1]+"'"  
    else:
        y=""  
    
    return y
# 从decode出的字符串中找出含有想要兑换出的货币数值与名称的信息
def has_error(s):
    if s.find("invalid")==-1:
        return "False"
    else:
        return "True"   
    
# 判断decode出的字符串是否意味着存在无效的的货币名称
def currency_response(currency_from, currency_to, amount_from):
    list1=["http://cs1110.cs.cornell.edu/2016fa/a1server.php?",
           "from=",currency_from,"&to=",currency_to,"&amt=",amount_from]
    str1="".join(list1)
    doc = urlopen(str1)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr
# 从网站中decode出有效的含信息的字符串
def iscurrency(currency):
    jstr=currency_response(currency,currency,"1")
    if has_error(jstr)=="True":
        return "False"
    else:
        return "True"
# 判断货币名称是否正确有效
def exchange(currency_from, currency_to, amount_from):
    if iscurrency(currency_from)=="False":
        return "The name of the currency you have is invalid."
    elif iscurrency(currency_to)=="False":
        return "The name of the currency you want to exchange for is invalid."
    else:
        s=currency_response(currency_from, currency_to, amount_from)
        a=get_from(s)
        b=get_to(s)
        c=before_space(b)
        c=c.replace("'","")
        return c
# 进行货币间兑换，若存在无效的货币名称缩写，则会返回说明兑换无效的信息    
def test_before_space():
    assert("2.5"==before_space("2.5 United States Dollars"))
def test_get_from1():
    assert("'2 United States Dollars'"==
           get_from('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'))
def test_get_from2():
    assert(""==get_from('{"from":"", "to":"", "success":false, "error":"Source currency code is invalid." }'))
def test_get_from3():
    assert(""==get_from('{"from":"", "to":"", "success":false, "error":"Currency amount is invalid." }'))
def test_get_to1():
    assert("'1.825936 Euros'"==
           get_to('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'))
def test_get_to2():
    assert(""==get_to('{"from":"", "to":"", "success":false, "error":"Source currency code is invalid." }'))
# 验证如果decode的信息无效的话会不会返回空字符串
def test_get_to3():
    assert(""==get_from('{"from":"", "to":"", "success":false, "error":"Currency amount is invalid." }'))
# 验证如果decode的信息无效的话会不会返回空字符串
def test_has_error1():
    assert("False"==has_error('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'))
def test_has_error2():
    assert("True"==has_error('{"from":"", "to":"", "success":false, "error":"Source currency code is invalid." }'))
def test_has_error3():
    assert("True"==has_error('{"from":"", "to":"", "success":false, "error":"Currency amount is invalid." }'))
def test_currency_response():
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'==
           currency_response("USD","EUR","2.5"))
def test_iscurrency1():
    assert("True"==iscurrency("USD"))
def test_iscurrency2():
    assert("False"==iscurrency("ABC"))
def test_exchange():
    assert("2.1589225"==exchange("USD","EUR","2.5"))
def testAll():
    test_before_space()
    test_get_from1()
    test_get_from2()
    test_get_from3()
    test_get_to1()
    test_get_to2()
    test_get_to3()
    test_has_error1()
    test_has_error2()
    test_has_error3()
    test_currency_response()
    test_iscurrency1()
    test_iscurrency2()
    test_exchange()
    print("All tests passed")    

def main():
    testAll()
    currency_from=input("Please input the currency you have:")
    # 输入的货币名称应为缩写(三个大写字母的形式)
    currency_to=input("Please input the currency you want to exchange for:")
    # 输入的货币名称应为缩写(三个大写字母的形式)
    amount_from=input("Please input the amount of currency you have:")
    # 输入的应为不含文字的数
    c=exchange(currency_from, currency_to, amount_from)
    if c=="The name of the currency you have is invalid.":
        print("The name of the currency you have is invalid.")
    elif c=="The name of the currency you want to exchange for is invalid.":
        print("The name of the currency you want to exchange for is invalid.")
    # 确保当输入的货币名称无效时会返回货币信息无效的说明
    else:
        print("You can exchange",amount_from,currency_from,'for',c,currency_to)
    
if __name__ == "__main__":
    main()

