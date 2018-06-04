### 下单接口



#### request请求

​	POST /order/

##### params参数：

house_id str  房屋id
start_time str  入住时间
end_time str    离店时间



#### response响应


##### 失效响应1

{
    "code": 900,
    "msg": "数据库访问失败"
}


##### 成功响应

{
    "code": 200,
}
