### 修改用户信息接口



#### request请求

​	PUT /user/user/

##### params参数：

name  str 用户名

avatar  imagefile  图片文件


#### response响应

##### 失效响应1

{
    "code": 1007,
    "msg": "用户名已被占用"
}

##### 失效响应2

{
    "code": 900,
    "msg": "数据库访问失败"
}

##### 失效响应3

{
    "code": 1006,
    "msg": "上传图片不符合标准"
}

##### 成功响应

{
    "code": 200,
    "msg": "请求成功"
}