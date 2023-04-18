from selenium import webdriver
from selenium.webdriver.common.by import By

from util.datetime_util import *

'''
它提供了在程序运行时跟踪异常的功能。当程序出现错误时，
traceback 会显示错误信息的详细堆栈跟踪，包括文件名、
行号、函数名等等，这对于程序员来说非常有帮助。
'''
import traceback
from util.find_element_util import *
from util.ini_reader import *
from util.log_util import *
import time


DRIVER = ''
def init_browser(browser_name):
    '''
    初始化浏览器
    在最先启动driver的值设置driver全局变量
    1.在方法外driver初始值，赋值为driver = None
    2.在方法内定义全局变量->global driver
    3.在其他地方调用时，直接给所调用的类传输driver
    其他封装函数或者文件需要用到driver，传输driver，则不会重新再实例化启动一次APP
    :param browser_name: 浏览器名称
    :return:
    '''
    global DRIVER
    if browser_name.lower() =="chrome":
        DRIVER = webdriver.Chrome(service=CHROME_DRIVER)
    elif browser_name.lower() == "firefox":
        DRIVER = webdriver.Firefox(service=FIREFOX_DRIVER)
    elif browser_name.lower() =="ie":
        DRIVER = webdriver.Ie(service=IE_DRIVER)
    else:
        warning("浏览器【%s】不支持，已默认启动chrome"%browser_name)
        DRIVER = webdriver.Chrome(CHROME_DRIVER)

def visit(url):
    '''
    访问指定url
    :param url:地址
    '''
    global DRIVER
    DRIVER.get(url)
    DRIVER.maximize_window()
    DRIVER.implicitly_wait(5)

def input(locate_method,locate_exp,value):
    '''
    输入操作
    :param locate_method:
    :param locate_exp:
    :param value:
    '''
    global DRIVER
    #方式1：直接传定位方式和定位表达式
    if locate_method in ["id", "xpath", "classname", "name", "tag name", "link text",
                              "partial link text", "css selector"]:
        find_element(DRIVER,locate_method,locate_exp).send_keys(value)
    #通过ini文件的key找到value，再分割定位方式和定位表达式
    else:
        parser = IniParser(ELEMENT_FILE_PATH)
        locate_method,locate_exp = tuple(parser.get_value(locate_method,locate_exp).split(">"))
        find_element(DRIVER,locate_method,locate_exp).send_keys(value)

def click(locate_method,locate_exp):
    '''
    点击操作
    :param locate_method:
    :param locate_exp:
    '''
    global DRIVER
    # 方式1：直接传定位方式和定位表达式
    if locate_method in ["id", "xpath", "classname", "name", "tag name", "link text",
                              "partial link text", "css selector"]:
        find_element(DRIVER,locate_method,locate_exp).click()
    #通过ini文件的key找到value，再分割定位方式和定位表达式
    else:
        parser = IniParser(ELEMENT_FILE_PATH)
        locate_method,locate_exp = tuple(parser.get_value(locate_method,locate_exp).split(">"))
        find_element(DRIVER,locate_method,locate_exp).click()


def clear(locate_method,locate_exp):
    '''
    清空操作
    :param locate_method:
    :param locate_exp:
    '''
    # 方式1：直接传定位方式和定位表达式
    if locate_method in ["id", "xpath", "classname", "name", "tag name", "link text",
                              "partial link text", "css selector"]:
        find_element(DRIVER, locate_method, locate_exp).clear()
    # 通过ini文件的key找到value，再分割定位方式和定位表达式
    else:
        parser = IniParser(ELEMENT_FILE_PATH)
        locate_method, locate_exp = tuple(parser.get_value(locate_method, locate_exp).split(">"))
        find_element(DRIVER, locate_method, locate_exp).clear()


def switch_frame(locate_method,locate_exp):
    '''
    切换frame
    :param locate_method:
    :param locate_exp:
    '''
    # 方式1：直接传定位方式和定位表达式
    if locate_method in ["id", "xpath", "classname", "name", "tag name", "link text",
                              "partial link text", "css selector"]:
        DRIVER.switch_to.frame(find_element(DRIVER, locate_method, locate_exp))
        # 通过ini文件的key找到value，再分割定位方式和定位表达式
        # 通过ini文件的key找到value，再分割定位方式和定位表达式
    else:
        parser = IniParser(ELEMENT_FILE_PATH)
        locate_method, locate_exp = tuple(parser.get_value(locate_method, locate_exp).split(">"))
        DRIVER.switch_to.frame(find_element(DRIVER, locate_method, locate_exp))

def switch_home_frame():
    '''
    切换回主框架
    :return:
    '''
    global DRIVER
    DRIVER.switch_to.default_content()

def assert_word(keyword):
    '''
    断言
    :param keyword:
    '''
    global DRIVER
    # print(DRIVER.page_source)
    assert keyword in DRIVER.page_source

def assert_noword(keyword):
    '''
    断言 关键字不存在
    :param keyword:
    '''
    global DRIVER
    # print(DRIVER.page_source)
    assert keyword not in DRIVER.page_source

def sleep(times):
    '''休眠时间'''
    time.sleep(int(times))

def quit():
    '''关闭浏览器'''
    global DRIVER
    DRIVER.quit()

def take_screenshot():
    '''截图'''
    global DRIVER
    '''创建当前日期目录'''
    dir = os.path.join(SCREENSHOT_PATH,get_chinese_date())
    if not os.path.exists(dir):
        os.makedirs(dir)
    '''以当前时间为文件名'''
    file_name = get_chinese_time()
    file_path = os.path.join(dir,file_name+".png")
    try:
        DRIVER.get_screenshot_as_file(file_path)
        return file_path
    except:
        error("截图发生异常【{}】\n{}".format(file_path,traceback.format_exc()))
        return file_path

def accpet_alert():
    '''
    确认弹窗
    '''
    global DRIVER
    alert = DRIVER.switch_to.alert
    alert.accept()

def dismiss_alert():
    '''
    取消弹窗
    '''
    global DRIVER
    alert = DRIVER.switch_to.alert
    alert.dismiss()



def del_table_tr(locate_method,locate_exp,row):
    '''
    获取表格中指定行数据进行删除
    '''
    global DRIVER
    if locate_method in ["id", "xpath", "classname", "name", "tag name", "link text",
                         "partial link text", "css selector"]:
        table = find_element(DRIVER,locate_method,locate_exp)

    else:
        parser = IniParser(ELEMENT_FILE_PATH)
        locate_method,locate_exp = tuple(parser.get_value(locate_method,locate_exp).split(">"))
        table = find_element(DRIVER,locate_method,locate_exp)

    # print(table)

    table_tr_list = table.find_elements("tag name", "tr")
    # print(table_tr_list)

    #获取指定行数据
    table_tr_list[int(row)].find_element("link text", "删除").click()

def change_table_tr(locate_method,locate_exp,row):
    '''
    获取表格中指定行数据进行修改
    '''
    global DRIVER
    if locate_method in ["id", "xpath", "classname", "name", "tag name", "link text",
                         "partial link text", "css selector"]:
        table = find_element(DRIVER,locate_method,locate_exp)

    else:
        parser = IniParser(ELEMENT_FILE_PATH)
        locate_method,locate_exp = tuple(parser.get_value(locate_method,locate_exp).split(">"))
        table = find_element(DRIVER,locate_method,locate_exp)

    # print(table)

    table_tr_list = table.find_elements("tag name", "tr")
    # print(table_tr_list)

    #获取指定行数据
    table_tr_list[int(row)].find_element("link text", "修改").click()








if __name__ == "__main__":

    init_browser("chrome")
    visit("http://192.168.1.219:8080/")
    clear("name","username")
    input("name","username","lisan")
    input("name","password","940729abcd")
    click("name","Submit")
    # sleep(2)
    # assert_word("lisan")
    click("link text","会员中心")
    click("link text","好友列表")
    sleep(2)
    del_table_tr("xpath","/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody",1)
    sleep(1)
    accpet_alert()
    sleep(5)
    assert_noword("lhong124")
    quit()



