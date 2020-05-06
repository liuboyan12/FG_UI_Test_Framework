from element_infos.login.login_page import LoginPage


def test_login(url, username, password, driver):
    login = LoginPage(driver)
    login.input_username(username)
    login.input_password(password)
    login.click_login()