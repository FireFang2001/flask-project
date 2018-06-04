### 发布房屋信息接口



#### request请求

​	POST /house/newhouse/

##### params参数：

title str  标题
price int  价格
area_id int   区域id
address str   地址
room_count int   房间数
acreage int   面积
unit = str   户型
capacity int   可住人数
beds = str   卧床配置
deposit int  押金
min_days str  最小入住天数
max_days str  最大入住天数
facility list  设施列表


#### response响应


##### 失效响应1

{
    "code": 900,
    "msg": "数据库访问失败"
}


##### 成功响应

{
    "code": 200,
    "house_id": house.id  房屋id
}
