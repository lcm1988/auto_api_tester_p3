# auto_api_tester_p3
<pre>
工具功能：
    1，支持冒烟测试：@APIdecorator(True)
    2，支持全数据对比：@APIdecorator(False)
    3，支持调用其他case的接口结果：expect_json=self.test_iphone_restart1(func_data=True)
    4，支持case归类管理、case方法预期归类管理、极大程度上减少了case编写的工作量
    5，用户可以自定义输出带关键标志的输出文案，然后在run方法中根据关键字获取相关统计数据，本工具预先设定的关键字为：@地址、@耗时
    6，可扩展业务测试脚本（需添加相应业务脚本方法）
    7，可扩UI自动化测试脚本（需添加相应UI脚本方法）

用例规范：
    1，用例均放置在cases目录下，不放与用例无关的文件
    2，cases下为项目目录，均为以“case_”开头、后缀用例名称的package包；
    3，项目目录内存放多个用例脚本，名称为case*.py；
    4，用例文件中的类均以“case_”开头，后缀用例名称；
    5，类中须包含setUp和tearDown方法，以保证各个case执行的完整性
    6，用例方法均以“test_”开头，后缀方法名称；
    7，涉及数据共享或基础数据准备的，可以在cases目录或各case的包内增加数据文件；
    8，如无转义需要，尽可能用单引号
    9，原则上所有case预期均放在expects目录下，但支持case内自定义case预期（例如动态对比线上线下接口等）

自定义工具类规范：
    1，自定义工具类均放置在tools目录下
    2，工具类文件和类命名均为驼峰命名法
    3，工具类内方法命名均为小写，多个单词的中间用下划线隔开
    4，如无转义需要，尽可能用单引号

</pre>