import configparser
from util.global_var import *


class IniParser:

    # 初始化打开ini文件
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            print("ini文件【%s】不存在！" % file_path)
            return
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path, encoding="utf-8")

    def get_sections(self):
        '''
        获取所有分组名
        '''
        return self.cf.sections()

    def get_options(self, section):
        '''
        获取指定分组的所有键
        '''
        return self.cf.options(section)

    def get_items(self, section):
        '''
        获取指定分组的键值对
        :param section:
        '''
        return self.cf.items(section)

    def get_value(self, section, key):
        '''
        获取指定分组的指定键的值
        :param section: 分组名
        :param key: 键
        '''
        return self.cf.get(section, key)


if __name__ == "__main__":
    # print(ELEMENT_FILE_PATH)
    parser = IniParser(ELEMENT_FILE_PATH)
    print(parser.get_sections())
    print(parser.get_options("EmpireCMS_indexPage"))
    print(parser.get_items("EmpireCMS_indexPage"))
    print(parser.get_value("EmpireCMS_indexPage", 'indexpage.username'))