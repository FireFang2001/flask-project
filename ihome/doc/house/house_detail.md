### 获取房屋详情信息接口



#### request请求

​	GET /house/detail/<int:id>/

##### params参数：

id  int  房屋id


#### response响应


##### 失效响应1

{
    "code": 900,
    "msg": "数据库访问失败"
}


##### 成功响应

{
    "code": 200,
    "house": house.to_full_dict(),   房屋详情
    "facilities": facility_dict_list,  房间设施
    "booking": bookings  是否是本人，0为本人
}
