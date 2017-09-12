~ 用于存放本周任务成果。
# 天气查询程序

## 基础版本：
### 功能：
* 输入城市名，可以得到最新天气数据
* 输入help显示帮助文档
* 输入history,获取历史查询信息
* 输入quit, 退出该程序

### 函数说明：
* fetchWeather函数获取心知天气api数据：运用requests模块
* help_doc函数用来打印帮助文档
* parse_data函数解析数据：利用json.loads
* get_user函数得到用户输入数据
* main函数实现持续用户交互程序

## 参考资料：
* [seniverse/seniverse-api-demos: Api usage demos for seniverse api](https://github.com/seniverse/seniverse-api-demos)
