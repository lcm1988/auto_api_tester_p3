#coding:utf-8
import base64
import hashlib
from pyDes import CBC,PAD_PKCS5,des

class StringEncode():
    def __init__(self,type='md5',fstr='',**kwargs):
        #type: md5, tbase64, fbase64, tdes, fdes
        self.type=type
        self.fstr=fstr
        if type.lower() in ('tdes','fdes'):
            if kwargs.get('Des_Key','') and kwargs.get('Des_IV',''):
                Des_Key,Des_IV=kwargs.get('Des_Key'),kwargs.get('Des_IV')
                self.k=des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
            else:
                raise ValueError('缺少必要参数：Des_Key | Des_IV')

    @property
    def Result(self):
        funcs={
            'md5':lambda x: self.__md5_encrypt(x),
            'tbase64': lambda x: self.__base64_encrypt(x),
            'fbase64': lambda x: self.__base64_decrypt(x),
            'tdes': lambda x: self.__des_encrypt(x),
            'fdes': lambda x:self.__des_decrypt(x)
        }
        return funcs[self.type.lower()](self.fstr)

    def __md5_encrypt(self,str=''):
        m=hashlib.md5()
        m.update(str.encode(encoding='utf-8'))
        return m.hexdigest()

    def __base64_encrypt(self,str=''):
        return base64.b64encode(str.encode(encoding='utf-8')).decode()

    def __base64_decrypt(self,str=''):
        return base64.b64decode(str).decode()

    def __des_encrypt(self,str=''):
        EncryptStr = self.k.encrypt(str)
        return base64.b64encode(EncryptStr).decode()

    def __des_decrypt(self,str=''):
        fromstr=base64.b64decode(str)
        return self.k.decrypt(fromstr).decode()

if __name__=="__main__":
    print(StringEncode('md5','12313123').Result)

