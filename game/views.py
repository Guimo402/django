from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line3 = '<hr>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201711%2F16%2F20171116092644_iMkX3.jpeg&refer=http%3A%2F%2Fb-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1692205451&t=e9446090dc80d7265591e1c7d9177dc3" width=1700>'
    return HttpResponse(line1 + line4 + line3 + line2)


def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line3 = '<hr>'
    line4 = '<a href="/">返回主页面</a>'
    line2 = '<img src="https://p9.itc.cn/images01/20210601/633e7fe9714b4c1bb8f50cc20ce76106.png", width=1700>'
    return HttpResponse(line1 + line4 + line3 + line2)

