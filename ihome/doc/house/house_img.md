### 发布房屋图片信息接口



#### request请求

​	POST /house/house_img/

##### params参数：

house_image file  图片文件

house_id  int  房屋id


#### response响应


##### 失效响应1

{
    "code": 900,
    "msg": "数据库访问失败"
}


##### 成功响应

{
    "code": 200,
    "image_url": image.url
}
