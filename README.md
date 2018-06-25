# jumpserver_script
自己写的一些jumpserver辅助脚本集

## jumpserver_key_restore.py
- 还原被jumpserver加密的数据和密码等
- 默认目录在 JumpServer 的config文件中找到你的key
- 用法 : python  jumpserver_key_restore.py  type  content
- type :  enc 是加密 dec 是解密
- content: 你的明文或者密文
- 在 assets_admin,assets_sysytemuser表中的: password private_key public_key 字段均可以解密
