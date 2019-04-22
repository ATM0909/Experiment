import requests
from aip import AipOcr

API_ID = "14358221"
API_Key = "z2mSGsrPm2mDG1sszbZncpH4"
Secret_Key = "8LcY2LlZrjGEWZ75aMmGF2smeyXNwDK3"
client = AipOcr(API_ID,API_Key,Secret_Key)
def haha(filepath):
    with open(filepath,'rb')as fp:
        return fp.read()
image = haha("C:\Users\Administrator\Desktop\图片\001.png")
result =  client.basicGeneral(image)
for item in result['words_result']:
    print(item['words'])



