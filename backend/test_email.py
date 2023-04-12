import yagmail

try:
    yag = yagmail.SMTP(
        user="1320598294@qq.com", password="tzauqgpeswiphifd", host="smtp.qq.com"
    )
    yag.send(to="emt0re0@gmail.com", subject="test", contents="Hello")
    print("Email send success")
except:
    print("Email send fail")
