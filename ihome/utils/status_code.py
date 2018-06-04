OK = 200
SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 900, 'msg': '数据库访问失败'}
PARAMS_ERROR = {'code': 901, 'msg': '参数错误'}

# 用户模块
USER_REGISTER_PARAMS_ERROR = {'code': 1000, 'msg': '参数错误'}
USER_REGISTER_MOBILE_ERROR = {'code': 1001, 'msg': '手机号码不符合规则'}
USER_REGISTER_MOBILE_IS_EXIST = {'code': 1002, 'msg': '手机号码已存在'}
USER_REGISTER_PASSWORD_IS_ERROR = {'code': 1003, 'msg': '两次密码不一致'}

USER_LOGIN_NOT_EXIST = {'code': 1004, 'msg': '用户不存在'}
USER_LOGIN_PASSWORD_ERROR = {'code': 1005, 'msg': '密码错误'}

USER_UPLOAD_IMAGE_ERROR = {'code': 1006, 'msg': '上传图片不符合标准'}
USER_NAME_EXIST = {'code': 1007, 'msg': '用户名已被占用'}
USER_ID_NUMBER_ERROR = {'code': 1008, 'msg': '身份证号码格式错误'}
USER_ID_NUMBER_EXIST = {'code': 1009, 'msg': '身份证号码已被注册'}

MYHOUSE_USER_IS_NOT_AUTH = {'code': 2000, 'msg': '用户没有实名认证'}

ORDER_START_TIME_GT_END_TIME = {'code': 3000, 'msg': '订单时间错误'}
