from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver,locate_method,locate_exp):
    '''
    显示等待一个元素
    显示等待对象（最多10秒，每0.2秒判断一次等待的条件）
    :param driver:
    :param locate_method:定位方法
    :param locate_ecp:定位元素值
    '''
    return WebDriverWait(driver,10,0.2).until(lambda x:x.find_element(locate_method,locate_exp))

def find_elements(driver,locate_method,locate_exp):
    '''
    显示等待一组元素
    显示等待对象（最多10秒，每0.2秒判断一次等待的条件）
    :param driver:
    :param locate_method:定位方法
    :param locate_exp:定位元素值
    '''
    return WebDriverWait(driver,10,0.2).until(lambda x:x.find_elements(locate_method,locate_exp))
