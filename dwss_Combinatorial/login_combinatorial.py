import time

import dwss_Foundation.login
import dwss_Foundation.index

"---登录组合类"
class loginpage_control:

    "登录智建云(不带企业编码)"
    def logincloud1(self,username,pwd):
        a = dwss_Foundation.index.cloudIndex()
        t = dwss_Foundation.login.Loginel()
        a.click_allow()
        t.sendUsename(username)
        t.sendPwd(pwd)
        t.checkAgree()
        t.clickLoginButoon()

    "登录智建云（带企业编码）"
    def logincloud2(self,username,pwd,code):
        a = dwss_Foundation.index.cloudIndex()
        t = dwss_Foundation.login.Loginel()
        a.click_allow()
        t.sendUsename(username)
        t.sendPwd(pwd)
        t.sendBusinesscode(code)
        t.checkAgree()
        t.clickLoginButoon()

