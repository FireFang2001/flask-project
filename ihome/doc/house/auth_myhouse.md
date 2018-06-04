### 获取实名用户发布的房屋信息接口



#### request请求

​	GET /house/auth_myhouse/

##### params参数：



#### response响应

##### 失效响应1

{
    "code": 2000,
    "msg": "用户没有实名认证"
}

##### 成功响应

{
    "code": 200,
    "msg": "请求成功"
}