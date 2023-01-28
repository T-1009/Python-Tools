import wx
import requests
import random
import json
import base64
from hashlib import md5
from tools import MyFrame


class toolfun(MyFrame):
    # 进制转换
    def transf(self, event):
        # 获取输入的进制
        outvalue = ''
        getinputbase = self.m_comboBox1.GetValue()
        getoutputbase = self.m_comboBox2.GetValue()

        if getinputbase == '2':
            if getoutputbase == '8':
                outvalue = oct(int(self.m_textCtrl1.Value, 2))[2:]
            elif getoutputbase == '10':
                outvalue = str(int(self.m_textCtrl1.Value, 2))
            elif getoutputbase == '16':
                outvalue = hex(int(self.m_textCtrl1.Value, 2))[2:]
            else:
                outvalue = self.m_textCtrl1.Value

        elif getinputbase == '8':
            if getoutputbase == '2':
                outvalue = bin(int(self.m_textCtrl1.Value, 8))[2:]
            elif getoutputbase == '10':
                outvalue = str(int(self.m_textCtrl1.Value, 8))
            elif getoutputbase == '16':
                outvalue = hex(int(self.m_textCtrl1.Value, 8))[2:]
            else:
                outvalue = self.m_textCtrl1.Value

        elif getinputbase == '10':
            if getoutputbase == '2':
                outvalue = bin(int(self.m_textCtrl1.Value))[2:]
            elif getoutputbase == '8':
                outvalue = oct(int(self.m_textCtrl1.Value))[2:]
            elif getoutputbase == '16':
                outvalue = hex(int(self.m_textCtrl1.Value))[2:]
            else:
                outvalue = self.m_textCtrl1.Value

        elif getinputbase == '16':
            if getoutputbase == '2':
                outvalue = bin(int(self.m_textCtrl1.Value, 16))[2:]
            elif getoutputbase == '10':
                outvalue = str(int(self.m_textCtrl1.Value, 16))
            elif getoutputbase == '8':
                outvalue = oct(int(self.m_textCtrl1.Value, 16))[2:]
            else:
                outvalue = self.m_textCtrl1.Value

        self.m_textCtrl2.AppendText(outvalue)

    def clear_fun1(self, event):
        self.m_textCtrl1.Clear()
        self.m_textCtrl2.Clear()

    def translate(self, event):
        # Set your own appid/appkey.
        alp = 'abcdefghijklmnopqrstuvwsyz'
        appid = '20221011001385841'
        appkey = '_bQWbmyfJ8fgVWIWjPGu'

        # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
        from_lang = 'auto'
        if self.m_comboBox3.GetValue() == '汉译英':
            to_lang = 'en'
        else:
            to_lang = 'zh'

        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        url = endpoint + path

        query = self.m_textCtrl3.Value

        # Generate salt and sign
        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        salt = random.randint(32768, 65536)
        sign = make_md5(appid + query + str(salt) + appkey)

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

        # Send request
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        self.m_textCtrl4.AppendText(result['trans_result'][0]['dst'])

    def clear_fun2(self, event):
        self.m_textCtrl3.Clear()
        self.m_textCtrl4.Clear()

    def vigenere_decrypt(self, event):
        def testIC(text):
            word_count = {}
            word_probability = {}
            for i in range(65, 91):
                word_count[chr(i)] = 0
                word_probability[chr(i)] = 0
            for i in text:
                word_count[i] += 1
            for i in range(65, 91):
                word_probability[chr(i)] = word_count[chr(i)] / len(text)
            text_IC = 0
            for i in range(65, 91):
                text_IC += pow(word_probability[chr(i)], 2)

            return text_IC

        def get_encryption_method(textIC):
            global flag
            if abs(textIC - 0.0385) < abs(textIC - 0.0655):
                flag = 1
            else:
                flag = 0

        def substitude(cipher, keys):
            result = ''
            # ! start
            index = 0
            key_size = len(keys)
            for c in cipher:
                if c < 'A' or c > 'Z':
                    result += c
                else:
                    i = index % key_size
                    ch = chr(65 + (ord(c) - ord(keys[i]) + 26) % 26)
                    result += ch
                    index += 1
            return result

        def decode(text):
            get_encryption_method(testIC(text))
            global flag
            p = 0
            key_lenth = 0
            # 进行多表替换解密
            if flag == 1:
                for i in range(0, 20):
                    sum_IC = 0
                    for j in range(0, i + 1):
                        decode_str = ''
                        text_IC = 0
                        for k in range(j, len(text), i + 1):
                            decode_str += text[k]

                        text_IC = testIC(decode_str)

                        sum_IC += text_IC

                    if abs(sum_IC / (i + 1) - 0.0655) < 0.008 and p == 0:
                        key_lenth = i + 1
                        p = 1

                key = []
                for i in range(0, key_lenth):
                    key.append(0)

                # 判断位移差量
                decode_str = ''
                temp = []
                for i in range(0, 26):
                    temp.append(0)

                for j in range(0, len(text), key_lenth):
                    decode_str += text[j]
                word_count_first = {}
                word_probability_first = {}
                for m in range(65, 91):
                    word_count_first[chr(m)] = 0
                    word_probability_first[chr(m)] = 0
                for m in decode_str:
                    word_count_first[m] += 1
                for m in range(65, 91):
                    word_probability_first[chr(m)] = word_count_first[chr(m)] / len(decode_str)

                constant_str = decode_str
                decode_str_list = list(decode_str)

                n = 1
                d = 0
                first_count = 0
                for k in range(0, 26):
                    decode_str = constant_str
                    for a in range(0, len(decode_str)):
                        m = ((ord(decode_str[a]) - 65) - k) % 26
                        decode_str_list[a] = chr(m + 65)
                    decode_str = ''.join(decode_str_list)
                    word_count = {}
                    word_probability = {}
                    for m in range(65, 91):
                        word_count[chr(m)] = 0
                        word_probability[chr(m)] = 0
                    for m in decode_str:
                        word_count[m] += 1
                    for m in range(65, 91):
                        word_probability[chr(m)] = word_count[chr(m)] / len(decode_str)
                    temp[k] = word_probability['E']

                for j in range(0, 26):
                    g = abs(temp[j] - 0.1225)
                    if n > g:
                        n = g
                        d = j
                first_count = d

                key[0] = chr(d + 65)

                for i in range(1, key_lenth):
                    MIC = 0
                    n = 0
                    d = 0
                    decode_str = ''
                    for j in range(i, len(text), key_lenth):
                        decode_str += text[j]
                    word_count = {}
                    word_probability = {}
                    for m in range(65, 91):
                        word_count[chr(m)] = 0
                        word_probability[chr(m)] = 0
                    for m in decode_str:
                        word_count[m] += 1
                    for m in range(65, 91):
                        word_probability[chr(m)] = word_count[chr(m)] / len(decode_str)
                    for s in range(0, 26):
                        MIC = 0
                        for m in range(65, 91):
                            t = (((m - 65) - s) % 26) + 65
                            MIC += word_probability[chr(t)] * word_probability_first[chr(m)]
                        temp[s] = MIC
                    for j in range(0, 26):
                        g = temp[j]
                        if n < g:
                            n = g
                            d = j
                    key[i] = chr((first_count - d) % 26 + 65)

                cipher = self.m_textCtrl5.Value

                return substitude(cipher, key)

        text = self.m_textCtrl5.Value
        text = text.replace(" ", "")
        text = text.replace("\n", "")
        text = text.upper()
        self.m_textCtrl6.AppendText(decode(text))

    def clear_fun3(self, event):
        self.m_textCtrl5.Clear()
        self.m_textCtrl6.Clear()

    def base_encrypt(self, event):
        ans = ''
        base = self.m_comboBox4.GetValue()
        strb = self.m_textCtrl7.Value
        if base == 'base16':
            ans = base64.b16encode(strb.encode('utf-8')).decode("utf-8")
        elif base == 'base32':
            ans = base64.b32encode(strb.encode('utf-8')).decode("utf-8")
        elif base == 'base64':
            ans = base64.b64encode(strb.encode('utf-8')).decode("utf-8")
        elif base == 'base85':
            ans = base64.b85encode(strb.encode('utf-8')).decode("utf-8")
        self.m_textCtrl8.AppendText(ans)

    def base_decrypt(self, event):
        ans = ''
        base = self.m_comboBox4.GetValue()
        strb = self.m_textCtrl7.Value
        if base == 'base16':
            ans = base64.b16decode(strb.encode('utf-8')).decode("utf-8")
        elif base == 'base32':
            ans = base64.b32decode(strb.encode('utf-8')).decode("utf-8")
        elif base == 'base64':
            ans = base64.b64decode(strb.encode('utf-8')).decode("utf-8")
        elif base == 'base85':
            ans = base64.b85decode(strb.encode('utf-8')).decode("utf-8")
        self.m_textCtrl8.AppendText(ans)

    def clear_fun4(self, event):
        self.m_textCtrl7.Clear()
        self.m_textCtrl8.Clear()


app = wx.App()
toolfun(None).Show()
app.MainLoop()
