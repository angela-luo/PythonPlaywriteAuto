"""
用户信息模块测试数据
创建日期: 2025-06-05
创建人: Angel
"""

# 用户信息测试数据
USER_INFO_DATA = [
    # 正向测试用例 (P1级别)
    {
        "test_id": "USER_INFO_001",
        "test_name": "更新所有用户信息字段",
        "level": "P1",
        "user_data": {
            "username": "testuser",
            "password": "newpass",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "address1": "123 Main St",
            "address2": "Apt 4B",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345",
            "country": "USA",
            "language": "english",
            "favorite_category": "DOGS",
            "enable_mylist": True,
            "enable_banner": True
        },
        "expected": "Account details saved.",
        "is_positive": True
    },
    {
        "test_id": "USER_INFO_002",
        "test_name": "更新信息但不修改密码",
        "level": "P1",
        "user_data": {
            "username": "testuser",
            "password": "",
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "phone": "098-765-4321",
            "address1": "456 Oak Ave",
            "city": "Othertown",
            "state": "NY",
            "zip": "54321",
            "country": "USA",
            "language": "japanese",
            "favorite_category": "CATS",
            "enable_mylist": False,
            "enable_banner": False
        },
        "expected": "Account details saved.",
        "is_positive": True
    },
    {
        "test_id": "USER_INFO_003",
        "test_name": "更新语言和偏好类别",
        "level": "P2",
        "user_data": {
            "username": "testuser",
            "password": "",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "address1": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345",
            "country": "USA",
            "language": "japanese",
            "favorite_category": "FISH"
        },
        "expected": "Account details saved.",
        "is_positive": True
    },

    # 逆向测试用例 (P1级别)
    {
        "test_id": "USER_INFO_004",
        "test_name": "使用无效邮箱格式更新",
        "level": "P1",
        "user_data": {
            "username": "testuser",
            "password": "",
            "first_name": "John",
            "last_name": "Doe",
            "email": "invalid-email",
            "phone": "123-456-7890",
            "address1": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345",
            "country": "USA",
            "language": "english",
            "favorite_category": "DOGS"
        },
        "expected": ["Email format is invalid."],
        "is_positive": False
    },
    {
        "test_id": "USER_INFO_005",
        "test_name": "更新时缺少必填字段",
        "level": "P1",
        "user_data": {
            "username": "testuser",
            "password": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone": "",
            "address1": "",
            "city": "",
            "state": "",
            "zip": "",
            "country": "",
            "language": "english",
            "favorite_category": "DOGS"
        },
        "expected": [
            "First name is required.",
            "Last name is required.",
            "Email is required.",
            "Phone is required.",
            "Address (1) is required.",
            "City is required.",
            "State is required.",
            "ZIP is required.",
            "Country is required."
        ],
        "is_positive": False
    },
    {
        "test_id": "USER_INFO_006",
        "test_name": "使用不匹配的密码更新",
        "level": "P2",
        "user_data": {
            "username": "testuser",
            "password": "password1",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "address1": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345",
            "country": "USA",
            "language": "english",
            "favorite_category": "DOGS"
        },
        "expected": ["Passwords do not match."],
        "is_positive": False
    },
    {
        "test_id": "USER_INFO_007",
        "test_name": "使用无效电话号码更新",
        "level": "P2",
        "user_data": {
            "username": "testuser",
            "password": "",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "abc-def-ghij",
            "address1": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345",
            "country": "USA",
            "language": "english",
            "favorite_category": "DOGS"
        },
        "expected": ["Phone format is invalid."],
        "is_positive": False
    }
]