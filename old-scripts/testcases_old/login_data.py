"""
登录模块测试数据
创建日期: 2025-06-05
创建人: Angel
"""

# 登录测试数据
LOGIN_DATA = [
    # 正向测试用例 (P1级别)
    {
        "test_id": "LOGIN_001",
        "test_name": "使用正确凭据登录",
        "level": "P1",
        "username": "angel",
        "password": "123456",
        "expected": "Welcome testuser!",
        "is_positive": True
    },
    {
        "test_id": "LOGIN_002",
        "test_name": "使用大写用户名登录",
        "level": "P1",
        "username": "TESTUSER",
        "password": "testpass",
        "expected": "Welcome testuser!",
        "is_positive": True
    },
    {
        "test_id": "LOGIN_003",
        "test_name": "使用带空格的用户名登录",
        "level": "P1",
        "username": " testuser ",
        "password": " testpass ",
        "expected": "Welcome testuser!",
        "is_positive": True
    },
    {
        "test_id": "LOGIN_004",
        "test_name": "使用特殊字符密码登录",
        "level": "P2",
        "username": "testuser",
        "password": "!@#$%^&*()_+",
        "expected": "Welcome testuser!",
        "is_positive": True
    },

    # 逆向测试用例 (P1级别)
    {
        "test_id": "LOGIN_005",
        "test_name": "使用错误密码登录",
        "level": "P1",
        "username": "testuser",
        "password": "wrongpass",
        "expected": "Invalid username or password. Signon failed.",
        "is_positive": False
    },
    {
        "test_id": "LOGIN_006",
        "test_name": "使用空用户名登录",
        "level": "P1",
        "username": "",
        "password": "testpass",
        "expected": "Please enter your username and password.",
        "is_positive": False
    },
    {
        "test_id": "LOGIN_007",
        "test_name": "使用空密码登录",
        "level": "P1",
        "username": "testuser",
        "password": "",
        "expected": "Please enter your username and password.",
        "is_positive": False
    },
    {
        "test_id": "LOGIN_008",
        "test_name": "使用不存在的用户登录",
        "level": "P2",
        "username": "nonexistent",
        "password": "password",
        "expected": "Invalid username or password. Signon failed.",
        "is_positive": False
    },
    {
        "test_id": "LOGIN_009",
        "test_name": "使用SQL注入尝试登录",
        "level": "P3",
        "username": "' OR '1'='1",
        "password": "anything",
        "expected": "Invalid username or password. Signon failed.",
        "is_positive": False
    }
]