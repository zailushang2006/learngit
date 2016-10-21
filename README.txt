userjudge 判断用户是否是刷币用户

1、需要下载使用Python数据分析集成包anaconda3 （这个包集成Python和所需的基本数据分析库）
2、所需使用的第三方包在packages文件中，pip install 包名 即可安装 
3、有一个自定义包userjudge，放在Anaconda3安装路径的Lib\site-packages\下 
4、有一个自定义py文件conn_mongo2.py，放在放在Anaconda3安装路径的Lib\下 
5、有一个模型文件bgModel_pickle.txt请按照自己需要放在相应文件夹下 
6、运行user_judge.py文件，返回最终结果（csv文件）
   ：user_judge(modelpath, pct, days = 30)函数有三个参数（modelpath是bgModel_pickle.txt的路径；pct用来限制返回的用户是刷子的概率大小，例如pct = 0.9表示90%以上的概率；days限制多长时间的活跃用户，默认30天）；
   result.to_csv导出结果为csv文件，路径需指定 
7、凡是用到conn_mongo2的自定义py文件或包都要修改lmbdb = conn_mongo2.conn_mongo(host='127.0.0.1', port = 27017, db='lmbdb0928')这句中的参数值

test

