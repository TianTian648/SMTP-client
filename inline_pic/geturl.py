import requests
def geturl(filename):

    data={
        'uid':'341d2f54d3914200a8152ac813a00346',
        'token':'e18b3869649b75f503b1b172ccb1466d'
    }
    url = "https://www.imgurl.org/api/v2/upload"
    # 通过文件上传
    resp = requests.post(url, data=data, files={"file": open(filename, "rb")})
    print(resp.json())
    print(resp.json()['data']['url'])
    return resp.json()['data']['url']
    #https://s3.uuu.ovh/imgs/2022/12/04/96015ba32a02a112.jpg
