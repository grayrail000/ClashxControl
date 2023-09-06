import time

import requests
from bs4 import BeautifulSoup


def transform_the_data():
    """直接转换成.yaml"""
    search_results = [
        {'title': '动漫岛-最新好看的日本动漫大全动漫迷的秘密岛屿，新番日漫 ...', 'content': 'http://www.88dmw.com'},
        {'title': 'MX动漫-专注在线动漫的樱花动漫备用网站', 'content': 'http://www.mxdm9.com'},
        {'title': 'AnFuns动漫_在线动漫资源门户', 'content': 'https://www.anfuns.cc'},
        {'title': 'E-ACG_动漫在线播放_无修动漫_E站', 'content': 'https://eacg.net'},
        {'title': '风车动漫-动漫啦-专注动漫的网站-免费在线观看动漫', 'content': 'https://www.dmla1.com'},
        {'title': '與日同步、超多「全部免費」新番動漫', 'content': 'https://www.kktv.me'},
        {'title': 'AGE动漫', 'content': 'https://m.agemys.org'},
        {'title': '丫丫动漫- 在线动漫- 国产动漫- 日本动漫- 动漫在线观看- 免费 ...', 'content': 'https://www.yydm1.cc'},
        {'title': '国产动漫- 海外华人影视在线观看', 'content': 'https://www.haitu.tv'},
        {'title': '漫岛动漫- 专注在线动漫聚合的网站', 'content': 'https://www.mddm.tv'},
        {'title': 'AGE动漫', 'content': 'https://m.agemys.org'},
        {'title': '丫丫动漫- 在线动漫- 国产动漫- 日本动漫- 动漫在线观看- 免费 ...', 'content': 'https://www.yydm1.cc'},
        {'title': '动漫大全_高清动漫在线观看_动漫下载-布丁动画', 'content': 'https://buding3.com'},
        {'title': '路漫漫在线动漫-在线动画,日本动漫,国产动漫,动漫免费在线', 'content': 'https://www.g916.com'},
        {'title': '線上看動漫 - Yahoo奇摩', 'content': 'https://tw.tv.yahoo.com'},
        {'title': '巴哈姆特動畫瘋', 'content': 'https://ani.gamer.com.tw'},
        {'title': '高清在线动漫片大全分享_经典好看的最新动漫片排行榜推荐', 'content': 'https://www.hanpian.tv'},
        {'title': '腾讯动漫- 免费漫画- 大王饶命漫画- 我是大神仙漫画- 海贼王 ...', 'content': 'https://ac.qq.com'},
        {'title': '在线观看动漫系列- Google Play 上的应用', 'content': 'https://play.google.com'},
        {'title': '22个在线看动漫的软件App/网站汇总（免费/付费）- 追番必备 ...', 'content': 'https://www.extrabux.com'},
        {'title': '在线观看动漫系列- Google Play 上的应用', 'content': 'https://play.google.com'},
        {'title': '樱花动漫、AGE、B站、Crunchyroll等免费在线追番', 'content': 'https://www.dealmoon.ca'},
        {'title': '233动漫网- 动漫在线-动漫下载', 'content': 'https://dm233.cc.atlaq.com'},
        {'title': '最好的在线动漫商店，Akibamarket，购买动漫人物', 'content': 'https://akibamarket.com'},
        {'title': '飞极速动漫大全_高清动漫在线观看', 'content': 'http://feijisu4.com'},
        {'title': '动漫在线', 'content': 'https://m.jpbeta.net'},
        {'title': '亚洲动漫|在线观看免费正版高清动漫–爱奇艺iQIYI | iQ.com', 'content': 'https://www.iq.com'},
        {'title': '樱花动漫app官网在线观看 - 3DM手游', 'content': 'https://shouyou.3dmgame.com'},
        {'title': '分类在线动漫下的文章- AcgnHub', 'content': 'http://www.acgfans.me'},
        {'title': '动漫大全_高清动漫在线观看', 'content': 'https://halihali7.com'},
        {'title': '樱花动漫_专注动漫的网站_在线观看全集动漫', 'content': 'https://www.857dmz.com'},
        {'title': '分享14个动漫网站，打开即可在线观看！ - 马丁库资源导航', 'content': 'https://www.martinku.cn'},
        {'title': '动漫在线', 'content': 'https://m.jpbeta.net'},
        {'title': '动漫在线看', 'content': 'https://dongmanzaixiankan.com'},
        {'title': 'ACG动漫网- ACG动漫免费在线观看', 'content': 'https://www.acgvod.com'},
        {'title': '动漫在线观看 - 搜狗视频', 'content': 'https://waptv.sogou.com'},
        {'title': '去看动漫- 樱花动漫-去看动画片', 'content': 'https://www.7kdm.com'},
        {'title': '漫岛动漫- 日本新番动漫，好看的动漫大全聚合网站', 'content': 'https://www.mandaowang.com'},
        {'title': '08y-黑丝高跟视频官网(app756.com)age动漫在线 - VirtualSC', 'content': 'https://virtualsc.org'},
        {'title': '海外动漫免费在线视频-高清动漫在线-最新动漫 - 胖子视频', 'content': 'https://m.pangzitv.com'},
        {'title': '在线动漫安卓版v0.0.1-pc6手机下载', 'content': 'http://www.pc6.com'},
        {'title': '好看的日本动漫,国产动画片大全,国语动漫,在线观看_看看动漫网', 'content': 'https://www.kkdm2.com'},
        {'title': '分裂的刻板印象：在线动漫中的女性形象建构研究 - 网易', 'content': 'https://www.163.com'},
        {'title': '樱花动漫-专注动漫的网站-免费在线观看动漫', 'content': 'https://www.916dm.com'},
        {'title': '2023最佳免费在线看日本动漫App/网站分享 - 即刻学习', 'content': 'https://www.jkxuexi.com'},
        {'title': 'ACG饭团-饭团动漫-免费在线看动漫-免费看番-ACGFantuan', 'content': 'https://acgfta.com'},
        {'title': '动漫在线看- 新番追更老漫补番免费观看 - 星视界', 'content': 'https://www.histar.tv'},
        {'title': '高清动漫在线观看_动漫下载-子子影院', 'content': 'http://ziziyy1.com'},
        {'title': '动画片大全-动漫免费在线播放-日本动漫-最新动漫-爱奇动漫网 ...',
         'content': 'https://www.dongmanwan.com'},
        {'title': '動漫狂', 'content': 'https://www.cartoonmad.com'},
        {'title': '分裂的刻板印象：在线动漫中的女性形象建构研究 - 网易', 'content': 'https://www.163.com'},
        {'title': '免费在线设计制作动漫插画 - Canva可画', 'content': 'https://www.canva.cn'},
        {'title': 'Bitturing on X: "免费高清在线动漫影视网站国产动漫、动漫电影 ...', 'content': 'https://twitter.com'},
        {'title': '刚开新服的手游线路-【copy url:74ps.com】.i4t - NCBI', 'content': 'https://www.ncbi.nlm.nih.gov'},
        {'title': '在线动漫-其他- ACG盒子', 'content': 'https://www.acgbox.link'},
        {'title': '趣动漫_专注动漫的网站_在线观看全集动漫', 'content': 'https://www.qdm66.com'},
        {'title': '官方樱花动漫网- 百度', 'content': 'http://www.baidu.com'},
        {'title': '腾讯视频动漫的微博', 'content': 'https://weibo.com'},
        {'title': '人像动漫化- 在线照片转动漫 - AILab Tools', 'content': 'https://www.ailabtools.com'}]

    for result in search_results:
        url = result['content']
        hostname = url.split('//')[-1].split('/')[0]
        print(f"{hostname}: 128.2.0.1")


def Get_google_search(q, _start=0):
    """获取google搜索结果"""
    _data = []
    try:
        response = requests.get(
            url="https://www.google.com/search",
            params={
                "q": q,
                "start": f"{str(_start)}",
            },
            headers={
                "Host": "www.google.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
            },
        )

        soup = BeautifulSoup(response.content, "html.parser")

        div_elements = soup.find_all("div", class_="kb0PBd cvP2Ce jGGQ5e")

        for div in div_elements:
            if div is not None:
                h3_element = div.find('h3', {'class': 'LC20lb MBeuO DKV0Md'})
                cite_element = div.find('cite', {'class': ['tjvcx GvPZzd cHaqb', 'qLRx3b tjvcx GvPZzd cHaqb']})

                if h3_element is not None and cite_element is not None:
                    # 删除多余的 span 标签
                    span_element = cite_element.find('span', {'class': 'dyjrff ob9lvb'})
                    if span_element is not None:
                        span_element.decompose()

                    h3_text = h3_element.get_text()
                    cite_text = cite_element.get_text()
                    _data.append({
                        'title': h3_text,
                        'content': cite_text
                    })

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return _data


def crawl_google_search():
    start = 0
    all_results = []

    while True:
        search_list = Get_google_search('在线动漫', start)
        all_results.extend(search_list)
        start = start + 10
        time.sleep(0.5)
        print('采集数量', len(all_results))
        if start > 50:
            # 只屏蔽头部的100条
            break
    print(all_results)


if __name__ == '__main__':
    # crawl_google_search()
    # print(Get_google_search('在线动漫', 0))
    transform_the_data()
