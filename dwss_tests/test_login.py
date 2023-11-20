import pytest
import dwss_Combinatorial.login_combinatorial
import dwss_appium_driver.log.logger

log = dwss_appium_driver.log.logger()

@pytest.mark.parametrize("username, password", [("kentestgrp10", "12345678")])
def test_login(driver_setup, username, password):
    # 进行登录操作
    log.info("-----------用例开始---------")
    a = dwss_Combinatorial.login_combinatorial.loginpage_control()
    a.logincloud1("username", "password")
    log.info("--------输入账号密码，点击登录---------")

