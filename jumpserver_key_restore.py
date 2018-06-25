
from itsdangerous import TimedJSONWebSignatureSerializer, JSONWebSignatureSerializer, \
    BadSignature, SignatureExpired

import sys


# 解密代码
class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance

class Signer(metaclass=Singleton):
    """用来加密,解密,和基于时间戳的方式验证token"""

    def __init__(self, secret_key=None):
        self.secret_key = secret_key

    def sign(self, value):
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        s = JSONWebSignatureSerializer(self.secret_key)
        return s.dumps(value)

    def unsign(self, value):
        s = JSONWebSignatureSerializer(self.secret_key)
        try:
            return s.loads(value)
        except BadSignature:
            return {}

    def sign_t(self, value, expires_in=3600):
        s = TimedJSONWebSignatureSerializer(self.secret_key, expires_in=expires_in)
        return str(s.dumps(value), encoding="utf8")

    def unsign_t(self, value):
        s = TimedJSONWebSignatureSerializer(self.secret_key)
        try:
            return s.loads(value)
        except (BadSignature, SignatureExpired):
            return {}

def get_signer(key):
    signer = Signer(key)
    return signer

if __name__ == "__main__":

    # 默认目录在 JumpServer 的config文件中找到你的key
    # 用法 : python  jumpserver_key_restore.py  type  content
    # type :  enc 是加密 dec 是解密
    # content: 你的明文或者密文
    # 在 assets_admin,assets_sysytemuser中的: password private_key public_key 字段均可以解密

    SECRET_KEY =  "123456"
    si = get_signer(SECRET_KEY)
    result = ""
    if len(sys.argv ) ==  3 :
        if sys.argv[1] == "enc":
            result = si.sign(sys.argv[2])
        elif  sys.argv[1] == "dec":
            result = si.unsign(sys.argv[2])
        else :
            print(" python  jumpserver_key_restore.py  key , type ")
    else:
        print(" python  jumpserver_key_restore.py  key , type ")

    print(result)