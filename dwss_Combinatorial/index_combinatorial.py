import dwss_Foundation.index
"---首页组合类"
class index_control:

    "同意声明"
    def agree(self):
        t = dwss_Foundation.index()
        t.click_agree()

    "暂时不使用"
    def refuse(self):
        t = dwss_Foundation.index()
        t.click_no()

    "允许访问"
    def allow(self):
        t = dwss_Foundation.index()
        for i in range(2) :
            t.click_allow()

    "同意授权并点击马上登录"
    def click_loginNow(self):
        t = dwss_Foundation.index()
        t.click_agree()
        for i in range(2) :
            t.click_allow()
        t.click_btngotologin()

    "同意授权并点击免费注册"
    def click_freeregister(self):
        t = dwss_Foundation.index()
        t.click_agree()
        for i in range(2):
            t.click_allow()
        t.click_btnregister()