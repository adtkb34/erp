DATABASES = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'data_230118',  # 数据库名字
    'USER': 'root',
    'PASSWORD': 'solutionrx+1',
    'HOST': '127.0.0.1',  # 那台机器安装了MySQL
    'PORT': 3306,
}

STATIC_URL = 'static'
DYNAMIC_URL = 'dynamic'
ORDER_HOME_PAGE = '界面显示/GB-D1-1.5.2 订单首页.xlsx'
SECRET_KEY = 'BUCKS_CHAMPIONSHIP' #md5 的盐
