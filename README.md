# encrypt_pymongo
##基于pymongo开发的数据库存储加密包
通过向pymongo中添加加密模块，并改变其读写模块，实现对数据库进行加密读写。使用encrypt_pymongo的过程中，数据库中存储的是加密数据，增删改查中使用的都是明文数据。

config.py文件用于配置加密的密钥，aes.py是加密算法模块。

为了实现加密读写的功能collection.py和cursor.py的相关代码有被修改。
