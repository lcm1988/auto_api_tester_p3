#coding:utf-8
import base64
import hashlib
from pyDes import CBC,PAD_PKCS5,des
import rsa

class StringCryptor():
    def __init__(self,type='md5',fstr='',**kwargs):
        #type: md5, tbase64, fbase64, tdes, fdes, trsa, frsa
        self.type=type
        self.fstr=fstr

        if type.lower() in ('tdes','fdes'):
            if kwargs.get('Des_Key','') and kwargs.get('Des_IV',''):
                Des_Key,Des_IV=kwargs.get('Des_Key'),kwargs.get('Des_IV')
                self.k=des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
            else:
                raise ValueError('缺少必要参数：Des_Key | Des_IV')

        if type.lower() in ('trsa','frsa'):
            if type.lower() == 'trsa' and kwargs.get('public_key_file',''):
                 with open(kwargs.get('public_key_file')) as file:
                    pub=file.read()
                    self.__public_key=rsa.PublicKey.load_pkcs1(pub)
            elif type.lower() == 'frsa' and  kwargs.get('private_key_file',''):
                with open(kwargs.get('private_key_file')) as file:
                    prv=file.read()
                    self.__private_key=rsa.PrivateKey.load_pkcs1(prv)
            else:
                raise ValueError('缺少必要参数：public_key_file | private_key_file')

    @property
    def Result(self):
        funcs={
            'md5':lambda x: self.__md5_encrypt(x),
            'tbase64': lambda x: self.__base64_encrypt(x),
            'fbase64': lambda x: self.__base64_decrypt(x),
            'tdes': lambda x: self.__des_encrypt(x),
            'fdes': lambda x:self.__des_decrypt(x),
            'trsa': lambda x:self.__rsa_encrypt(x),
            'frsa': lambda x:self.__rsa_decrypt(x)
        }
        return funcs[self.type.lower()](self.fstr)

    def __md5_encrypt(self,str=''):
        m=hashlib.md5()
        m.update(str.encode(encoding='utf-8'))
        return m.hexdigest()

    def __base64_encrypt(self,str=''):
        return base64.b64encode(str.encode(encoding='utf-8'))

    def __base64_decrypt(self,str=''):
        return base64.b64decode(str)

    def __des_encrypt(self,str=''):
        EncryptStr = self.k.encrypt(str)
        return base64.b64encode(EncryptStr)

    def __des_decrypt(self,str=''):
        fromstr=base64.b64decode(str)
        return self.k.decrypt(fromstr)

    def __rsa_encrypt(self,str=''):
        str=str.encode('utf-8')
        return base64.b64encode(rsa.encrypt(str,self.__public_key))

    def __rsa_decrypt(self,str=''):
        str=base64.b64decode(str)
        return rsa.decrypt(str,self.__private_key)

if __name__=="__main__":
    #print(StringCryptor('md5','12313123').Result)
    print(StringCryptor('trsa','12313123',public_key_file='pbk',private_key_file='pk').Result)
    str='H0PfabdvNX9NoUws/GGbKHX7iBtbFjQkFP8d6K6gWuJ1jIGVKdPt7f0cUXuBADOY0lsqtwCSAtx6zG3m8KgeiDCrgLsZMkGYfkE8G2n3rnzX+eJvRAy263HCf+oXiwdApntkK2OwLf30TLmsZx7C9YzRQkOhgt6gKJHtOzRnLasSDTBJAx6obF2pH4psZw/66n5plTCIY4t8NL4xiEm5JAifAGECsS2tJ7VChMO7GCDCX7kkpO51YWCCcjh0C/DMKuDlTYjOXsDCuwWY/VUHT9aYszEK/D6PV6WfQmMqzTDdrgOudmhCgYs+C6Cn/xk4Lmzm5wspX8EEtzX+49OuEw=='
    print(StringCryptor('frsa',str,public_key_file='e:\\pbk',private_key_file='e:\\pk').Result)






