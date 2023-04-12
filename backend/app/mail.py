# 使用邮箱发送验证码，用来验证登入
import yagmail
from fastapi import HTTPException
from yagmail.error import (
    YagAddressError,
    YagConnectionClosed,
    YagInvalidEmailAddress,
)

"""
邮箱服务器配置
emailh:邮箱服务器地址
emailu:邮箱用户名
emailpsw:邮箱密码
"""
emailh = "smtp.qq.com"
emailu = "1320598294@qq.com"
emailpsw = "tzauqgpeswiphifd"


# 发送邮件
def mail_engine(email: str, sub: str, con: str) -> None:
    sender = None
    try:
        sender = yagmail.SMTP(host=emailh, user=emailu, password=emailpsw)  # 与邮箱服务器建立连接
        """
        to:收件人邮箱地址
        subject:邮件主题
        contents:邮件内容
        """
        sender.send(to=email, subject=sub, contents=con)
    except YagConnectionClosed:
        raise HTTPException(status_code=500, detail="服务器连接失败")
    except (YagInvalidEmailAddress, YagAddressError):
        raise HTTPException(status_code=400, detail="无法识别的电子邮件")
    finally:
        if sender is not None:
            sender.close()  # 关闭连接


# 获取邮箱验证码
def get_code_email(email: str, code: str) -> None:
    mail_engine(email, "验证码", code)


# 创建新账号通知
def new_account(email: str, name: str) -> None:
    mail_engine(email, "注册成功", name + ": 欢迎加入")


# 找回账号通知
def recovery_code(email: str, code: str) -> None:
    mail_engine(email, "验证码", code)


# 修改密码成功通知
def recovery_success(email: str) -> None:
    mail_engine(email, "操作成功", "已成功重设密码")
