# coding=utf-8🔥

# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2023-05-17
@author: 北京-宏哥   QQ交流群：705269076
公众号：北京宏哥
Project: 《最新出炉》系列初窥篇-Python+Playwright自动化测试-1-环境准备与搭建
'''

# 3.导入模块

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)          # 启动 chromium 浏览器
    page = browser.new_page()              # 打开一个标签页
    page.goto("https://www.baidu.com")     # 打开百度地址
    print(page.title())                    # 打印当前页面title
    page.click("input[name=\"wd\"]")       # 点击输入框
    page.fill("input[name=\"wd\"]", "chromium")  # 在输入框输入浏览器名字
    page.screenshot(path=f'example-{p.chromium.name}.png')
    browser.close()                        # 关闭浏览器对象