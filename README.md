# EmpireCMS1
EmpireCMS 关键字驱动+数据驱动 
-------------------Selenium+Pytest自动化测试框架----------------------------------
|-目录文件名-|       |----说明-----|                       |----是否为python包----|
-------------------------------------------------------------------------------
conf              conf 目录属于第一层测试工具层，用于存储各配置文件   否
Logger.conf            日志功能的配置
elements_repository.ini   配置文件存储了各页面的元素对象的定位方式和定位表达式
--------------------------------------------------------------------------------
action           框架第二层“服务层”                             是
                 相当于对测试对象的一个业务封装。
                 对于接口测试，是对远程方法的一个实现；
                 对于 UI 测试，是对页面元素或操作的一个封装。
page_action.py   该模块基于关键字格式，封装了页面操作的常用函数，
                 如打开浏览器、点击、输入文本等
--------------------------------------------------------------------------------
config               配置文件目录                              是
ElementsRepository.ini存储了各页面的元素
                     对象的定位方式和定位表达式
Logger.conf          日志功能配置信息
--------------------------------------------------------------------------------
business_process     框架第三层“测试用例逻辑层”，
                     该层主要是将服务层封装好的各个业务对象，        是
                     组织成测试逻辑，进行校验
case_process.py
data_source_process.py  获取数据驱动所需的数据源集合
main_process.py      基于 case_process.py 和 data_source_process.py，
                     实现关键字驱动+数据驱动的测试用例集的执行

--------------------------------------------------------------------------------
page             对selenium的方法进行封装                        是
webpage.py        selenium方法的封装
--------------------------------------------------------------------------------
page_element     页面元素封装 ，存放定位元素                       否
search.yaml      定位元素配置文件（根据自己测试的功能命名）
--------------------------------------------------------------------------------
test_data                                                      是
--------------------------------------------------------------------------------
test_report                                                    否
--------------------------------------------------------------------------------
utils            第一层的测试工具层，用于实现测试过程中调用的工具类方法，
                 例如读取配置文件、页面元素的操作方法 、操作 Excel 文   是
                 件、生成测试报告、 发送邮件等。
global_var.py    定义测试过程中所需的全局变量。
find_element_util.py     封装了基于显式等待的界面元素定位方法。
excel_util.py     对excel 的读写操作（需要安装openpyxl模块）
datetime_util.py  实现了获取各种格式的当前日期时间
log_util.py       该模块封装了日志打印输出、级别设定等功能
ini_reader.py     封装了对 ini 配置文件的读取操作
email_util.py     封装了邮件发送功能
report_util.py    生成测试结果文件并发送邮件
--------------------------------------------------------------------------------
main.py           本模块是本框架的运行主入口，属于第四层“测试场景层”，
                  将测试用例组织成测试场景，实现各种级别 cases 的管理，
                  如冒烟，回归等测试场景
---------------------------------------------------------------------------------
