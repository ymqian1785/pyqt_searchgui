# pyqt_searchgui
need for searching in the  mysql
gui6为利用pyqt4设计的查询界面源码
进入账号admin密码为admin
查询功能函数是buttonTest(self)
数据格式和航班数据在图片中显示
现在需要在buttonTest这个函数添加代码实现动态SQL语句，将查询得到的结果显示在self.tableWidget
姓名对应self.checkBox和self.lineEdit
证件号对应self.checkBox_2和self.lineEdit_2
航班号对应self.checkBox_3和self.lineEdit_3
座位号对应self.checkBox_4和self.lineEdit_15
登机口对应self.checkBox_6和self.lineEdit_16
序号对应self.checkBox_8和self.lineEdit_17
self.conn = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='zdki',
            db='wenzhou',
            #
            charset='utf8',
        )
        self.cur = self.conn.cursor()
        self.sqlstring = "select * from tourist2 where "
