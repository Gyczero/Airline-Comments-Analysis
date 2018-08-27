# 关于各大航空公司博文文本挖掘与可视化

# 爬虫

**爬虫爬取微博移动端关于六大航空公司的博文信息**

包括：东航、南航、海航、国航、春秋航空和国泰航空

爬虫爬取网址（以东航为例）：[东航](https://m.weibo.cn/container/getIndex?type=all&queryVal=%E4%B8%9C%E8%88%AA&luicode=10000011&lfid=106003type%3D1&title=%E4%B8%9C%E8%88%AA&containerid=100103type%3D1%26q%3D%E4%B8%9C%E8%88%AA&page=2)

爬虫模块包括：

目的      |   具体操作
:-------- |  :--:
|  确定数据源 |  分析微博数据爬取可行性，确定爬取url  |
|  确定返回数据格式   |    根据返回的Json，确定收集的字段  |
| 定义存储的数据格式     |   编写Item类  |
| 解析返回数据 |  写解析函数，根据返回Json解析所需字段
| 存储数据到本地 | 更改配置文件，配置MongoDB，存储数据


# 文本挖掘
对爬取的文本数据进行处理，包括：

| 目的      |    处理流程 | 具体操作 |
| :-------- | --------:| :--:|
| 数据清洗  |  设置删除词 | 设置如“校园”、“就业”等删除词，去除无关博文|
|          | 去除空值   |  |
|          | 清除官博数据 | 观察不同博文数对应的用户名，粗略清除博文数 > 2的用户  |
| 计算关于各大航空公司的公众情感倾向  |   训练SnowNLP模型 | 爬取大众点评关于航空公司的评价，训练 |
| | 不同航司公众情感倾向计算并可视化 | 使用[snowNLP](https://github.com/isnowfy/snownlp)计算不同航空公司对应博文得分，并用matplotlib可视化 |
| 挖掘公众对航空公司不同态度的表达内容 |  提取关键词，可视化 |  使用Jieba分词，并对高频单词进行可视化 |
| 单词间聚类，挖掘不同关键词间的关系 | 博文转化为单词矩阵 | 每一个博文对应一个向量，填充tf-idf |
| | 设置停止词，”掐头去尾” |  将过高/过低文档频率的词去掉，保证分析结果的准确性 |
| | 计算单词间相关性 | 获取与指定单词（如“服务”）相关性最高的单词，使用余弦相似度计算 |
| | 进行层次性聚类  |  探究关键词之间的关系，并进行可视化




# 结论
从微博数据得到：

1、航空公司公众情感倾向（以东航为例）：

![东航](https://github.com/Gyczero/Airline-Comments-Analysis/blob/master/ReadMe0.png)

2、航空公司博文Top30关键词（以东航为例）：

积极情感：![东航积极情感微博关键词](https://github.com/Gyczero/Airline-Comments-Analysis/blob/master/ReadMe1.png)

消极情感：![东航消极情感微博关键词](https://github.com/Gyczero/Airline-Comments-Analysis/blob/master/ReadMe2.png)

3、航空公司博文Top30关键词间联系（以春秋航空为例）：

词云：![春秋航空词云](https://github.com/Gyczero/Airline-Comments-Analysis/blob/master/ReadMe3.png)

层次性聚类后结果：![春秋航空关键词层次性聚类后结果](https://github.com/Gyczero/Airline-Comments-Analysis/blob/master/ReadMe4.png)

4、航空公司【服务】单词对应相关性最高的单词（以春秋航空为例）：

春秋航空博文中同"服务"最相关单词:![春秋航空博文中同"服务"最相关单词](https://github.com/Gyczero/Airline-Comments-Analysis/blob/master/ReadMe5.png)
