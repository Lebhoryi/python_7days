#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : Restaurant.py
# @Date    : 2018-10-17 16:44:26
# @Author  : Lebhoryi@gmail.com
# @Link    : http://example.org
# @Version : V0.0.1


########################################################################################
# 项目实战一： 开餐馆
#     假如你是一家餐馆的老板，想开发一个信息系统。创建了一个餐馆类（名
# 字自取），有以下属性：餐馆名字和类型，营业时间默认 8 点，用餐人数；有
# 两个方法，第一个打印出餐馆的名字和类型 ，另外一个是指出餐馆的营业时间，
# 已经正在营业还是，休息。另外，定义方法打印出有多少人来用餐，还有修改
# 用餐人数，只能递增不能减少。
#     有一天你的朋友，小明，看你赚钱了，想开一个火锅店。请为他设计一个
# 类，并添加火锅类型的属性（四川还是重庆还是小火锅等）你的朋友除了想统
# 计用餐人数因为，他还想统计员工人数。有人离职则减少人数，有人入职则增
# 加。
#
# 最后请用文件的形式保存 类，然后导入到主程序。
########################################################################################

class Restaurant(object):
	'''开发的饭店信息系统

	有以下属性：餐馆名字和类型，营业时间默认 8 点，用餐人数；
	有两个方法，第一个打印出餐馆的名字和类型 ，另外一个是指出餐馆的营业时间，
	已经正在营业还是，休息。另外，定义方法打印出有多少人来用餐，还有修改用餐人数，只能递增不能减少。

	'''
	def __init__(self, name, classification, people):
		self.name = name    # 饭店名字
		self.classification = classification    # 饭店类型
		self.start_time = 8    # 默认的营业时间8点，不需要在init方法列出
		self.people = people    # 用餐人数

	def put_name_cla(self):
		'''打印出餐馆的名字和类型
        '''
		print(f"餐馆的名字是：{self.name}")
		print(f"餐馆的类型是：{self.classification}")

	def is_operating(self,now_time):
		'''指出餐馆现在的时间，营业时间：8-21，判断已经正在营业还是休息。
        '''
		print("餐馆现在的时间是：{}点...".format(now_time))

		# 判断是否营业
		if now_time > 8 and now_time < 21:
			print("餐馆营业中...")
		elif now_time < 0 or now_time > 24:
			print("这个不是正常人类的时间...")
		else:
			print("餐馆休息中...")

	def dining_people(self):
		'''打印现在多少人用餐
        '''
		print(f"现在的用餐人数是：{self.people}人...")

	def one_later_people(self, eating_people):
		'''过了一个小后的用餐人数，并修改，只能递增不能减少。
        '''
		print(f"过了一个小时之后的用餐人数是：{eating_people}人...")
		if eating_people < self.people:
			print(f"哎呀，不行吖，这样下去迟早破产，还不赶紧去多招些客人！")
		else:
			print("生意不错嘛，一个小时涨了{}个客人".format(eating_people-self.people))
		print("\n")

class Hotpot(Restaurant):
	'''
	设计一个类，
	属性：
		重庆火锅
	方法：
		1.统计用餐人数，2.统计员工人数，有人离职则减少人数，有人入职则增加。
	'''
	def __init__(self, name, classification, people, waiters):
		'''初始化，餐馆名字，类型，服务员人数，火锅类型
		'''
		# uper() 函数是用于调用父类(超类)的一个方法。
		# 此处是调用父类Restaurant.__init__()方法
		super().__init__(name, classification, people)
		self.waiters = waiters
        
    
# 	def dining_people2(self):
# 		'''继承父类的dining_people()函数，打印用餐人数
# 		'''
# 		super().dining_people(self)

	def update_waiters(self, update_waiter):
		'''统计员工人数，此部分借鉴参考答案
		'''
		# >0 表示有人入职； <0 表示有人离职
		if update_waiter > 0:
			self.waiters += update_waiter
			print(f"有{update_waiter}名新的员工入职啦，现在的员工人数增加到：{self.waiters}人")
		elif update_waiter < 0 and abs(update_waiter) < self.waiters:
			self.waiters += update_waiter
			print(f"有{abs(update_waiter)}名老的员工离职啦，现在的员工人数减少到：{self.waiters}人")
		else:
			print(f"好好想想是不是经营不善的问题，你的员工已经全部离职！")

            

if __name__ == "__main__":
	m = Restaurant("木南饭店", "中式", 10)
	m.put_name_cla()
	m.is_operating(10)
	m.dining_people()
	m.one_later_people(30)

	h = Hotpot("重庆老火锅", "火锅", 20, 15)
	h.put_name_cla()
	h.dining_people()
	h.update_waiters(10)
	h.update_waiters(-5)
	h.update_waiters(-20)
    
