### 实名认证接口



#### request请求

​	POST /user/login/

##### params参数：

real_name  str 真实姓名

id_num  int  身份证号码


#### response响应

##### 失效响应1

{
    "code": 901,
    "msg": "参数错误"
}

##### 失效响应2

{
    "code": 900,
    "msg": "数据库访问失败"
}

##### 失效响应3

{
    "code": 1008,
    "msg": "身份证号码格式错误"
}

##### 失效响应3

{
    "code": 1009,
    "msg": "身份证号码已被注册"
}

##### 成功响应

{
    "code": 200,
    "msg": "请求成功"
}