# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:18:40 2017

@author: tony
"""


#===============================================================================
#截取字符串
# s='hello the curel world'
# 
# k=f=i=0
# while i<len(s):
#     if s[i]==' ':  #匹配空字符串
#         k=i        #将当前的位置赋值给k
#         print s[f:k]  #获取从0到当前位置的字符
#         f=i+1    #记录打印完字符串之后的位置给f，做初始化重新获取字符串
#    i+=1
#===============================================================================

#===============================================================================
# #去除字符串中包含的子串
# s='hello thethe curel world the dd'
# sub='the'
# 
# i=0
# while i<len(s)-len(sub)+1:
#     if s[i:i+len(sub)]==sub:   #匹配子串
#         s=s[:i]+s[i+len(sub):]   #删除匹配的子串
#         i-=1  #让匹配的位置恢复到匹配子串之前的位置重新进行匹配
#     i+=1
#print s
#===============================================================================

    

#===============================================================================
# #保留第一个匹配到的子串，删除之后的子串    
# s='hello the curel world the dd'
# s1='the'
# i=c=0
# while i<len(s)-len(s1)+1:
#     if s[i:i+len(s1)]==s1:   #匹配子串
# #        print i
#         c+=1  #统计匹配的次数
#     if c>=2:
#         s=s[:i]+s[i+len(s1):]  #删除匹配到的子串
#    i+=1
#print s
#===============================================================================

#===============================================================================
# #将字符串中的指定的子串s1替换成s2
# s='hello the curel world the dd'
# s1='the'
# s2='niu'
# 
# i=0
# while i<len(s)-len(s1)+1:
#     if s[i:i+len(s1)]==s1:
# #        s[i:i+len(s1)]=s2
#         s=s[:i]+s2+s[i+len(s1):]
#    i+=1
#print s
#===============================================================================

#===============================================================================
# #去除字符串的首尾空格
# s='    hello world china   '
# #  0123456789012345678901
# print len(s)
# i=h=0
# end=-1
# while i<len(s):
#     if not s[i].isspace(): #匹配不为空的字符位置
#         h=i
#         break  #匹配到一个匹配之后退出循环
#     i+=1
#     
# i=len(s)-1
# while i>=0:
#     if not s[i].isspace():  #确定不为空的最后一个字符
#         end=i
#         print i 
#         break     
#     i-=1
# print s[h:end+1]  #最后的end位置是不包含的，需要加1
#===============================================================================

#截取字符串中的等长图片
import urllib
s='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta name="renderer" content="webkit">
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<title>卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L</title>
<meta name="Keywords" content="卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L">
<meta name="Description" content="卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L">
<!--css start-->
<link href="//img.yihaodianimg.com/front-detail/global/css/global_site_base.css?20ce613" rel="stylesheet" type="text/css"/>
<link href="//img.yihaodianimg.com/front-detail/detail/css/productDetail.css?20ce613" rel="stylesheet" type="text/css"/>
<!--css end-->
<!--js start-->
<script type="text/javascript">
var URLPrefix = {"shop":"//shop.yhd.com","busystock":"//gps.yhd.com","img":"//image.yihaodian.com","jd_item_stock":"//c0.3.cn/stock?extraParam=%7B%22originid%22:%221%22%7D&ch=1","h5HomeUrl":"//m.yhd.com","h5Search":"//search.m.yhd.com","shoping_pms":"//pms.yihaodian.com","search":"//search.yhd.com","jd_item_stocks":"//c0.3.cn/stocks?type=getstocks","detailDomain":"//item.yhd.com","jd_item_suit":"//c0.3.cn/recommend?methods=suitv2&count=6","commentZoneMall":"//e.1mall.com/front-pe","productDetailHost":"//www.yhd.com","central":"//www.yhd.com","h5pe_yhd":"//e.m.yhd.com","search_list":"//search.yhd.com","cartDomain":"//cart.yhd.com","centralShop":"//shop.yhd.com","shoping_my_statics":"//static.yihaodian.com/statics","shoping_search":"//search.yhd.com:80","homeUrl":"//www.yhd.com","shoping_central":"//www.yhd.com","search_keyword":"//search.yhd.com","sitedomainmall":".1mall.com","products_stock":"//gps.yhd.com/busystock","commentZoneYhd":"//e.yhd.com/front-pe","tuangou":"//www.yhd.com/tuangou/index.do","centralImgDomain":".yihaodianimg.com","statics":"//img.yihaodianimg.com/front-detail","mobile":"http://m.yhd.com","cms":"//cms.yhd.com","pms":"//pms.yhd.com","my_statics":"//static.yihaodian.com/member","passportmall":"https://passport.1mall.com","pe_yhd":"//item.yhd.com","h5DetaiDomain":"//item.m.yhd.com","shoping_shop":"//shop.yhd.com","sitedomain":".yhd.com","tryUrl":"//try.yhd.com","shoping_self":"//www.yhd.com","tracker":"tracker.yhd.com","footFriendLink":"//www.yhd.com/friendlink/index.do","shoping_passport":"https://passport.yhd.com","uploadPostUrl":"//upload.yihaodian.com/upload/UploadAction","shoping_my":"//my.yhd.com","shoping_opposite":"//www.1mall.com","env":"PRODUCTION","my":"//my.yhd.com","mymall":"//my.1mall.com","selfroot":"//www.yhd.com","item":"//item.yhd.com/","jd_item_yanbao":"//cd.jd.com/yanbao/v3","productDetailUrl":"//www.yhd.com","passport":"https://passport.yhd.com","mall":"//www.1mall.com"};
var headerType="base";
var imagePath="//img.yihaodianimg.com/front-detail/global/images";
var currSiteId=1;
var currSiteType=1;
var globalEnv="PRODUCTION";
var siteStyle=1;
var siteFlag=0;
var isIndex = 0;
var indexFlag= 0;
var currProvinceId=1;
var currVersionNum= "20ce613";
var lazyLoadImageObjArry = lazyLoadImageObjArry || [];
var isFixTopNav = false;
(function(flag) {
if (flag) {
window.globalPrismFlag = '1';
window.globalPrismFeedbackURL = '//cms.yhd.com/cms/view.do?topicId=43';
window.globalPrismQRName = '';
window.globalPrismQRTitle = '手机购物更优惠';
window.globalPrismQRPng = '//img.yihaodianimg.com/front-homepage/index/images/qryhd.png';
window.globalPrismMemberLink = '//home.yhd.com/myyhdindex/index.do';
window.globalPrismCartLink = '//cart.yhd.com/cart/cart.do';
window.globalPrismCouponLink = '//coupon.yhd.com/myCoupon';
window.globalPrismTopAdvFlag = '1';
}
})(true);
<!--增加一个开关来控制是否显示搜索框下拉,为时才不调用-->
<!--搜索热词开关-->
<!--用于控制宽窄屏属性-->
<!--过滤-->
var SensitiveWords = "【京东配送】=,【京东超市】=,京东海外直采=海外直采,京东配送=,京东自营=自营,京东超市=,JD超市=";
</script>
<!--js end-->
</head>
<body id="comParamId" data-param='{"globalPageCode":"-1","currPageId":"0"}'>
<div class="hd_header_wrap">
<!-- top_bar -->
<div class="hd_top_bar">
<div class="wrap clearfix">
<a href="//www.yhd.com" class="hd_topbar_home">
<i class="hd_iconfont">&#xe623;</i>
<span>1号店首页</span>
</a>
<div class="hd_indxProvce hd_has_child" id="headerSelectProvince" clstag="pageclick|keycount|global_201709226|1">
<a class="hd_topbar_city" id="currProvince" href="javascript:void(0);">
<i class="hd_iconfont">&#xe621;</i>
<span>送货地址：</span><em></em>
</a>
<div class="hd_city_select hd_city_opacity" style="display: none" id="hd_city_select" data-hot="2817,上海市,2&&2816,北京市,1&&1601,广州市,19&&1607,深圳市,19&&904,南京市,12&&1213,杭州市,15&&1381,武汉市,17&&1930,成都市,22&&48131,重庆市,4&&988,苏州市,12&&51035,天津市,3&&1116,合肥市,14&&1233,温州市,15&&984,无锡市,12&&1158,宁波市,15&&978,常州市,12">
<a href="javascript:;" class="hd_city_close">×</a>
<div class="hd_cur_city_wrap clearfix">
<span class="hd_cur_city">搜索城市：</span>
<div class="hd_city_search">
<div class="hd_city_input">
<em class="hd_iconfont"></em>
<input type="text" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;请输入城市名称">
<span class="hd_citys_close">x</span>
</div>
<div class="hd_city_suggest" style="display: none;">
</div>
</div>
</div>
<!--热门城市-->
<div class="hd_hot_city_wrap clearfix">
<em class="hd_hotcity_icon"></em>
<span class="hd_hot_city">热门城市：</span>
<div class="hd_hotcity_list clearfix">
</div>
</div>
<!--按字母查找-->
<div class="hd_letter_search clearfix">
<p class="hd_letter_tit">按字母查找</p>
<div class="hd_city_initial clearfix">
</div>
</div>
<div class="hd_city_list" id="hd_city_list_context">
<ul>
<li class="clearfix">
</li>
</ul>
</div>
</div>
</div>
<div class="hd_topbar_right">
<ul>
<li id="global_unlogin">
<div class="hd_unlogin">
<span class="hd_hi">Hi,请</span>
<a href="https://passport.yhd.com/passport/login_input.do" class="hd_login_link"
clstag="pageclick|keycount|global_201709226|2">登录&nbsp;</a>
<a href="https://passport.yhd.com/passport/register_input.do" class="hd_regist_link"
clstag="pageclick|keycount|global_201709226|3">&nbsp;注册</a>
</div>
</li>
<li id="global_login" class="hd_has_child" style="display:none" data-type="2017"
clstag="pageclick|keycount|global_201709226|4">
<div class="hd_login">
<span class="hd_hi">Hi,</span>
<a href="//home.yhd.com/myyhdindex/index.do" target="_blank" class="hd_login_name">__nickName__</a>
<a href="//vip.yhd.com" target="_blank" class="hd_vip hd_vip__gradeStyle__">__gradeDesc__</a>
<i class="hd_iconfont">&#xe627;</i>
</div>
<div class="hd_user_privilege">
<a href="javascript:;" class="hd_login_out">退出</a>
<div class="clearfix">
</div>
<div class="hd_privilege_tit"><span>我可尊享<em>5</em>项特权</span></div>
<div class="hd_privilege_wrap hd_privilege_slide">
<a href="javascript:;" class="prev_btn hd_iconfont"></a>
<div class="hd_privilege clearfix">
<div class="hd_privilege_list" style="left: -60px; margin-left: 0px;">
</div>
</div>
<a href="javascript:;" class="next_btn hd_iconfont"></a>
</div>
</div>
</li>
<li clstag="pageclick|keycount|global_201709226|5">
<div class="hd_menu hd_notice" id="hdUserMsg" style="display: none" data-cfg="1">
<a href="//edm.yhd.com/pcMsg/myMessage.action;" rel="nofollow" target='_blank'>我的消息&nbsp;(<em
class="hd_has_num">0</em>)</a>
</div>
</li>
<li clstag="pageclick|keycount|global_201709226|6">
<div class="hd_menu">
<a href="//home.yhd.com/order/toOrderList.do" target="_blank" rel="nofollow"><i
class="hd_iconfont">&#xe612;</i>我的订单</a>
</div>
</li>
<li class="hd_has_child" clstag="pageclick|keycount|global_201709226|7">
<div class="hd_menu">
<a href="//cms.yhd.com/cms/view.do?topicId=43" target="_blank">客户服务</a>
<i class="hd_iconfont">&#xe627;</i>
</div>
<div class="hd_menu_list">
<a href="//home.yhd.com/order/toOrderList.do" target="_blank" title="包裹跟踪">包裹跟踪</a>
<a href="//rma.yhd.com/return/returnApplyList.do" target="_blank" title="在线退换货">在线退换货</a>
</div>
</li>
<li class="hd_has_child">
<div class="hd_menu">
<a href="//b2b.yhd.com/index.do" target="_blank">企业服务</a>
</div>
<div class="hd_menu_list">
</div>
</li>
</ul>
</div>
</div>
</div>
<!-- top_main -->
<div class="wrap hd_header hd_cm_global">
<div class="clearfix">
<div class="hd_logo_area" clstag="pageclick|keycount|2017091213|22">
<a href="//www.yhd.com" class="hd_logo"><img src="//d9.yihaodianimg.com/N10/M0A/DB/61/ChEi2lj4TqGAOjXwAAAbSq83IXA88700.png" alt="基础头部logo"></a>
</div>
<div class="hd_header_right">
<div class="clearfix">
<div class="hd_head_search">
<div class="hd_search_form" id="hdSearchForm">
<div class="hd_fixed_wrap">
<a href="//www.yhd.com" class="hd_fixed_logo"><img src="//d7.yihaodianimg.com/N09/M09/85/8D/ChEi11jziUSAOkn4AABJ2dwtrSw01400.jpg" alt="" width="205" height="70"></a>
<div class="hd_search_wrap clearfix">
<label for="keyword" style="display:none;">请输入关键词</label>
<input class="hd_search_ipt" name="keyword" id="keyword" type="text" value="" placeholder="请输入关键词" original="请输入关键词" url="" style="color:#333333;" maxLength="100" AUTOCOMPLETE="off" x-webkit-speech="" onwebkitspeechchange="emptySearchBar();" x-webkit-grammar="builtin:translate"/>
<button type="button" class="hd_search_btn" onclick="javascript:searchMeForClick();" clstag="pageclick|keycount|global_201709226|8"><i class="hd_iconfont">&#xe624;</i></button>
</div>
<!--搜索提示 begin-->
<div id="searchSuggest" class="hd_search_tips_result" style="display:none" onmouseover="$('#searchSuggest').show()" clstag="pageclick|keycount|global_201709226|9"></div>
<!--搜索提示 end-->
</div>
</div>
<p id="hotKeywordsShow" class="hd_hot_search" clstag="pageclick|keycount|201708178|2">
</p>
<!--搜索推荐-->
</div>
<div class="hd_mini_cart" id="miniCart" data-version="1" clstag="pageclick|keycount|2017091213|19">
<u class="hd_c_num none" id="in_cart_num"></u>
<a class="hd_prism_cart" href="//cart.yhd.com/cart/cart.do" data-ref="YHD_TOP_MINICART">
<em class="hd_iconfont">&#xe618;</em>
<span>购物车</span>
</a>
<div class="hd_cart_show none" id="showMiniCartDetail">
</div>
</div>
</div>
</div>
</div>
</div>
<!-- top_nav -->
<div class="hd_cm_wrap">
<div class="wrap">
<div class="hd_cm_nav clearfix" id="headerNav">
<div class="hd_cm_allsort_wrap" id="allSortbox">
<a href="javascript:;" class="hd_cm_tit">所有商品分类<em class="hd_iconfont">&#xe627;</em></a>
<div class="mod_hd_allsort">
</div>
</div>
<div class="hd_cm_nav_wrap">
<ul class="clearfix" id="global_menu">
<li>
<a href="//qianggou.yhd.com/" title="1号抢购" target="_blank" >1号抢购</a>
</li>
<li>
<a href="//t.yhd.com/" title="1号团" target="_blank" >1号团</a>
</li>
<li>
<a href="//coupon.yhd.com/couponCenter/home" title="领券中心" target="_blank" >领券中心</a>
</li>
<li>
<a href="https://sale.yhd.com/act/KGqzRfW23JZotYn.html" title="商城优选" target="_blank" >商城优选</a>
</li>
<li>
<a href="//channel.yhd.com/import.html" title="全球进口" target="_blank" >全球进口</a>
</li>
<li>
<a href="https://sale.yhd.com/act/kLpM7UEzshTZmv.html" title="1号生鲜" target="_blank" >1号生鲜</a>
</li>
<li>
<a href="https://sale.yhd.com/act/uf0DFM6Iahpn.html" title="美妆馆" target="_blank" >美妆馆</a>
</li>
<li>
<a href="https://sale.yhd.com/act/LPHwt8z1A5x.html" title="家居馆" target="_blank" >家居馆</a>
</li>
<li>
<a href="https://sale.yhd.com/act/PnGHmKZ4u16pab.html" title="电器城" target="_blank" >电器城</a>
</li>
</ul>
</div>
</div>
</div>
</div></div><!--content start-->
<script>
var detailParams = {
skuId: '16892520062',
isPop: 1,
availAttrbutes: [{"skuId":16892520065,"尺码":"56/190/XXXL","颜色":"大红色14"},{"skuId":16892520064,"尺码":"54/185/XXL","颜色":"大红色14"},{"skuId":16892520063,"尺码":"52/180/XL","颜色":"大红色14"},{"skuId":16892520062,"尺码":"50/175/L","颜色":"大红色14"},{"skuId":16892520061,"尺码":"48/170/M","颜色":"大红色14"}],
attributes: [{"attributeName":"颜色","attributeAlias":"选择颜色","attributeValueVOList":[{"attributePicUrl":"jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg","attributeValueName":"大红色14"}],"attributeType":2},{"attributeName":"尺码","attributeAlias":"选择尺码","attributeValueVOList":[{"attributeValueName":"48/170/M"},{"attributeValueName":"50/175/L"},{"attributeValueName":"52/180/XL"},{"attributeValueName":"54/185/XXL"},{"attributeValueName":"56/190/XXXL"}],"attributeType":0}],
//pName: '卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L',
brandId: '9939',
//brandName: '卡宾（CABBEEN）',
categoryIds: ["1315","1342","9732"],
//categoryNames: '[服饰内衣, 男装, 卫衣]',
venderId: '86251',
productKO: '',
spAttr: {"isOverseaPurchase":"0","is7ToReturn":"1","LuxuryGoods":"0","isCartshield":"0","YuShouNoWay":"0","isKO":"0","isEbay":"0","isXnzt":"0","isLOC":"0","HYKHSP":"0","YuShou":"0","isFlashPurchase":"0","isSupermarket":"0"},
curDate: 1511510441231,
isBookVideo: 0
};
</script> <div class="detail_wrap">
<!--面包屑-->
<div class="mod_detail_crumb clearfix">
<div class="crumb clearfix">
<a clstag="pageclick|keycount|product_201709214|1" target="_blank" href="//search.yhd.com/c1315-0-0"><em>服饰内衣</em><i class="iconDetail"></i></a>
<a clstag="pageclick|keycount|product_201709214|2" target="_blank" href="//search.yhd.com/c1342-0-0"><em>男装</em><i class="iconDetail"></i></a>
<a clstag="pageclick|keycount|product_201709214|3" target="_blank" href="//search.yhd.com/c9732-0-0"><em>卫衣</em><i class="iconDetail"></i></a>
<a clstag="pageclick|keycount|product_201709214|4" target="_blank" href="//search.yhd.com/c9732-0-0/mbname卡宾（CABBEEN）-b9939"><em>卡宾（CABBEEN）</em><i class="iconDetail"></i></a>
<span><em title="卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L">卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L</em></span>
</div>
</div>
<!--第一屏-->
<div class="fm_detail_one clearfix">
<!--左侧主图区域-->
<div class="l">
<div class="mod_detail_preview clearfix" id="jsModDetailPreview">
<!--左侧主图区域-->
<!-- 大图 start -->
<div class="proImg_border">
<div class="proImg">
<input type="hidden" autocomplete="off" id="sub115115PicURL" value="jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg">
<input type="hidden" autocomplete="off" id="sub120120PicURL" value="jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg">
<img id="J_prodImg" width="360" height="360" original_src="jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg">
<div class="zoomCursor"></div>
<div class="mask"></div>
</div>
</div>
<!-- 大图 end -->
<!-- middle img list start -->
<div class="proCrumb clearfix" id="jsproCrumb" clstag="pageclick|keycount|product_201709214|5">
<a href="javascript:void(0);" class="cBtn prev iconDetail" title="上一个">&#xe60b;</a>
<div class="hideBox">
<div class="mBox clearfix">
<b><img width="50" height="50" class="detail_main_pic_class" original_src="jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg"></b>
<b><img width="50" height="50" class="detail_main_pic_class" original_src="jfs/t9340/244/2041038642/290163/1669b066/59c28ad1Ndf7a4e8c.jpg"></b>
<b><img width="50" height="50" class="detail_main_pic_class" original_src="jfs/t8416/261/2001478188/282166/c3fad1f/59c28ad7Ne40c7c7d.jpg"></b>
<b><img width="50" height="50" class="detail_main_pic_class" original_src="jfs/t9442/174/2039919290/488481/79bb1aa1/59c28b4eN1c88eebf.jpg"></b>
<b><img width="50" height="50" class="detail_main_pic_class" original_src="jfs/t8836/123/2002250543/247672/588bc52e/59c28b4cNb370edc0.jpg"></b>
</div>
</div>
<a href="javascript:void(0);" class="cBtn next iconDetail" title="下一个">&#xe610;</a>
</div>
<div class="J_zoom" id="J_zoom"><img id="sub600600PicURL" width="600" height="600" original_src="jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg" alt=""></div>
<!-- middle img list end -->
</div>
<!-- btm start -->
<div class="product_rel clearfix">
<div class="prod_l">
<p class="product_id" id="pro_code"><span>商品编号</span>16892520062</p>
</div>
<p class="product_share" id="product_share" clstag="pageclick|keycount|product_201709214|8">
<a class="share_tit" href="javascript:void(0);"><em class="iconDetail">&#xe612;</em>分享<i class="iconDetail">&#xe603;</i></a>
<span class="sharelist clearfix">
<a class="ico_sina" title="分享到新浪微博" href="javascript:(function(){var rul=location.href;if(rul.indexOf('?')>0){rul = rul +'&'}else{rul = rul +'?'};rul = rul +'tarcker_u=9402576';window.open(' http://v.t.sina.com.cn/share/share.php?appkey=2794712645&title='+encodeURIComponent('【卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L】，1号店，品质保证，网上优选 @1号店')+'&url='+encodeURIComponent(rul),'_blank','width=615,height=505');})()">新浪微博</a>
<a class="ico_qq" title="分享到腾迅微博" href="javascript:void(0)" onclick="detailUtil.dzdposttoWb();" >腾讯微博</a>
</span>
</p>
</div>
<!-- btm end -->
</div>
<div class="main_content">
<div class="detail_information" id="jsModInformation">
<div class="mod_detailInfo_proName" id="detail_sku_main">
<h1 class="mh" id="productMainName" >卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L</h1>
</div>
<div class="mod_detailInfo_priceSales ">
<div class="big_promo_box clearfix" style="display: none;" id="bigPromoBanner"></div>
<div class="seckill_box clearfix none" id="oneRobBuyBanner">
<a href="javascript:void(0);" target="_blank" class="logo_enter seckill_enter">1号抢购</a>
<span class="start_time none" id="oneRobBuyStartTime"></span>
<div class="countdown_box none" id="oneRobBuyContDown"></div>
</div>
<div class="price pb0" id="currentPriceArea">
<ul class="clearfix">
<li class="tag" id="price_lable">
价格
</li>
<li class="number inte_check">
<span id="current_price"></span>
</li>
<li class="pricing" id="bookprice"></li>
</ul>
</div>
<ul class="Msgsales clearfix" id="msgsales">
<li id="skuGoodCommentRate" >
<span class="hpl paise" style="display: none;">
<a class="pl" onclick="detailPeExperience.forwardPL('p');" href="#sppj">
<span class="iconDetail"></span>好评率<strong class="rate"></strong>
</a>
</span>
<span class="pl paise_num" style="display: none;">
<a class="pl" onclick="detailPeExperience.forwardPL('p');" href="#sppj">[评论<span class="yellow"></span>条]</a>
</span>
</li>
</ul>
<div id="promoTag" style="display:none;" class="new-doing"></div>
</div>
<div class="mod_detailInfo_promotion" id="detailPromotion" clstag="pageclick|keycount|product_201709214|6"></div>
<div id="sku_unit" class="mod_detailInfo_tags warranty_box" style="display:none;padding-top:10px;" clstag="pageclick|keycount|product_201709214|7">
<div id="choose" class="clearfix p-choose-wrap" style="border-top:none;padding-top:0px;margin-top:0px;margin-bottom:5px;">
<div id="choose-attrs">
<div id="choose-attr-1" class="li p-choose" data-type="颜色" data-idx="0">
<div class="dt">选择颜色：</div>
<div class="dd">
<div class="item selected" data-value="大红色14" title="大红色14">
<b></b>
<a href="#none">
<img class="detail_serial_product_pic_class" data-img="1" original_src="jfs/t8314/224/2037523725/376040/4913ae9e/59c28ae9N808c6d0c.jpg" width="30" height="30">
<i>大红色14</i>
</a>
</div>
</div>
</div>
<div id="choose-attr-2" class="li p-choose" data-type="尺码" data-idx="1">
<div class="dt">选择尺码：</div>
<div class="dd">
<div class="item" data-value="48/170/M" title="48/170/M">
<b></b>
<a href="#none">
<i style="font-style: normal;">48/170/M</i>
</a>
</div>
<div class="item selected" data-value="50/175/L" title="50/175/L">
<b></b>
<a href="#none">
<i style="font-style: normal;">50/175/L</i>
</a>
</div>
<div class="item" data-value="52/180/XL" title="52/180/XL">
<b></b>
<a href="#none">
<i style="font-style: normal;">52/180/XL</i>
</a>
</div>
<div class="item" data-value="54/185/XXL" title="54/185/XXL">
<b></b>
<a href="#none">
<i style="font-style: normal;">54/185/XXL</i>
</a>
</div>
<div class="item" data-value="56/190/XXXL" title="56/190/XXXL">
<b></b>
<a href="#none">
<i style="font-style: normal;">56/190/XXXL</i>
</a>
</div>
</div>
</div>
</div>
</div>
<div class="mod_choise_kit" id='firstScreenCombine' style="display:none;">
</div>
</div>
<!--区域选择-->
<div class="mod_detailInfo_addressbox mod_address" id="detaiThreeAreas">
<p class="errbox_txt" style="display:none;">请选择您要的商品信息 </p>
<dl class="addressbox clearfix" id="detaiThreeAreasDl">
<dt id="haigou-area-wuliu">送货至</dt>
<dd>
<div class="add_01 myYhd clearfix">
<div class="mod_selectbox clearfix" style="z-index:1;" clstag="pageclick|keycount|product_201709214|9">
<div class="input_btn" id="area_name"><span class="value"></span><i class="iconDetail">&#xe603;</i><span class="lion"></span></div>
<div class="selectlist">
<ul class="tablist clearfix">
<li class="tab_01" tag-index='1' id="tabs_province" data-id=""><i></i></li>
<li class="tab_02" tag-index='2' id="tabs_city" data-id=""><i></i></li>
<li class="tab_03" tag-index='3' id="tabs_county" data-id=""><i></i></li>
<li class="tab_04" tag-index='4' id="tabs_town" data-id=""><i></i></li>
</ul>
<div class="sec_childs">
<div class="sec_level sec_level1 clearfix" tag-index='1'>
<div class="arealist clearfix">
<div class="dt">华北</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="1">北京</a>
<a class="sec_item" href="javascript:void(0);" data-id="3">天津</a>
<a class="sec_item" href="javascript:void(0);" data-id="5">河北</a>
<a class="sec_item" href="javascript:void(0);" data-id="6">山西</a>
<a class="sec_item" href="javascript:void(0);" data-id="11">内蒙古</a>
</div>
</div>
<div class="arealist clearfix">
<div class="dt">华东</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="2">上海</a>
<a class="sec_item" href="javascript:void(0);" data-id="12">江苏</a>
<a class="sec_item" href="javascript:void(0);" data-id="15">浙江</a>
<a class="sec_item" href="javascript:void(0);" data-id="14">安徽</a>
<a class="sec_item" href="javascript:void(0);" data-id="16">福建</a>
<a class="sec_item" href="javascript:void(0);" data-id="13">山东</a>
</div>
</div>
<div class="arealist clearfix">
<div class="dt">华南</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="19">广东</a>
<a class="sec_item" href="javascript:void(0);" data-id="20">广西</a>
<a class="sec_item" href="javascript:void(0);" data-id="23">海南</a>
</div>
</div>
<div class="arealist clearfix">
<div class="dt">华中</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="21">江西</a>
<a class="sec_item" href="javascript:void(0);" data-id="7">河南</a>
<a class="sec_item" href="javascript:void(0);" data-id="17">湖北</a>
<a class="sec_item" href="javascript:void(0);" data-id="18">湖南</a>
</div>
</div>
<div class="arealist clearfix">
<div class="dt">西南</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="4">重庆</a>
<a class="sec_item" href="javascript:void(0);" data-id="22">四川</a>
<a class="sec_item" href="javascript:void(0);" data-id="24">贵州</a>
<a class="sec_item" href="javascript:void(0);" data-id="25">云南</a>
<a class="sec_item" href="javascript:void(0);" data-id="26">西藏</a>
</div>
</div>
<div class="arealist clearfix">
<div class="dt">西北</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="27">陕西</a>
<a class="sec_item" href="javascript:void(0);" data-id="28">甘肃</a>
<a class="sec_item" href="javascript:void(0);" data-id="29">青海</a>
<a class="sec_item" href="javascript:void(0);" data-id="30">宁夏</a>
<a class="sec_item" href="javascript:void(0);" data-id="31">新疆</a>
</div>
</div>
<div class="arealist clearfix">
<div class="dt">东北</div>
<div class="dd">
<a class="sec_item" href="javascript:void(0);" data-id="8">辽宁</a>
<a class="sec_item" href="javascript:void(0);" data-id="9">吉林</a>
<a class="sec_item" href="javascript:void(0);" data-id="10">黑龙江</a>
</div>
</div>
</div>
<div class="sec_level sec_level2 clearfix" tag-index='2' id="mod_address_city">
</div>
<div class="sec_level sec_level3 clearfix" tag-index='3' id="mod_address_county">
</div>
<div class="sec_level sec_level4 clearfix" tag-index='4' id="mod_address_town">
</div>
</div>
<div class="selectclose"><a href="javascript:void(0);"></a></div>
</div>
</div>
<div class="area_info">
<p>
<span id="detailStockInfo">
</span>
</p>
</div>
</div>
<p class="add_02"></p>
</dd>
</dl>
</div>
<div class="mod_cuputing clearfix" id="computingArea">
<div class="clearfix">
<div data-sel="num" class="computing_item" id="computing_item" clstag="pageclick|keycount|product_201709214|11">
<div class="computing_num">
<input type="text" data-max="199" data-min="1" class="num" value="1" id="product_amount">
</div>
<div class="computing_act">
<input type="button" class="add">
<input type="button" class="no_reduce">
</div>
</div>
<div class="cartbox" id="BtnArea">
<a clstag="pageclick|keycount|product_201709214|10" href="javascript:void(0);" class="buy_btn6 btn_init_class" rel="addCart" id="addCart" style="display:none;"><span>加入购物车</span></a>
<a class="buy_btn3 btn_init_class" href="javascript:void(0);" style="display:none" id="sellOut"><span>已售完</span></a>
<a class="buy_btn3 btn_init_class" href="javascript:void(0);" style="display:none" id="seriesBtn_arrivalNotice"><span>加入购物车</span></a>
</div>
</div>
<div class="in_tips" id="limitNum" style="display:none"></div>
</div>
<div class="mod_favlist" id="noGoodscommand" style="display:none;" data-tpa="DATAIL_NO_GOODS_RECOMMAND" clstag="pageclick|keycount|product_201709214|18"></div>
<dl class="mod_detailInfor_ensure clearfix" id="serviceGuarantee">
<dt>保障</dt>
<dd class="clearfix">
<div id="payServiceList">
<a id="7dayReturnTag" href="javascript:void(0);" style="" title="支持7天无理由退货"><i class="iconDetail"></i>支持7天无理由退货</a>
</div>
</dd>
</dl>
</div>
</div>
<div class="r" id="r_mod" style="display: none;">
<div class="mod_change" id="r_mod_change"></div>
</div></div> <!--第二屏文描及其他框架-->
<div class="fm_detail_two laymt clearfix">
<div class="grid_4">
<div id="leftLazyLoad"></div>
<div id="detail_viewAndBuyRecomm" style="display: none;" class="mod_box mod_product_box" clstag="pageclick|keycount|product_201709214|15">
</div>
<div id="detail_buyAndBuyRecomm" style="display: none" class="mod_box mod_product_box" clstag="pageclick|keycount|product_201709214|16">
</div> </div>
<div class="grid_18">
<div id="centerLazyLoad"></div>
<dl id="detail_hot10Recomm" class="recommnad explosion clearfix" style="display: none" clstag="pageclick|keycount|product_201709214|17">
</dl>
<div class="des_fixed" id="J_fixedDes">
<div class="layout_wrap">
<div class="des">
<div class="des_search fl" clstag="pageclick|keycount|product_201709214|14">
<div class="shopdsr clearfix">
<p class="shopdsr_name">
<a class="shopdsr_name" id="detail_desc_shopname_fixed" title="" href="javascript:void(0);" target="_blank"></a>
</p>
<p id="detail_dzd_faq_fixed" style="" class="shopdsr_online">
<span class="im_online_chat big online_statu" style="display: none;">
<a href="javascript:void(0)" class="onlines online_icon_big" title="联系在线客服" onclick="detailVenderInfo.bindVenderService();"></a>
</span>
<span class="im_online_chat big offline_statu" style="display: none;">
<a href="javascript:void(0)" class="offlines online_icon_big" title="客服离线，请留言" onclick="detailVenderInfo.bindVenderService();"></a>
</span>
</p>
</div>
</div>
<ul class="des_tab">
<li class="des_tabbox" id="detail_desc_tab_fixed">
<a clstag="pageclick|keycount|product_201709214|19" tabIndex="0" href="javascript:void(0);" class="tab cur" id="spjs_fixed">商品介绍</a>
<a clstag="pageclick|keycount|product_201709214|20" tabIndex="3" href="javascript:void(0);" class="tab" id="sppj_fixed">评价<em></em></a>
<a clstag="pageclick|keycount|product_201709214|21" tabIndex="1" href="javascript:void(0);" class="tab" id="ggbz_fixed">规格及包装</a>
<a clstag="pageclick|keycount|product_201709214|22" tabIndex="2" href="javascript:void(0);" class="tab" id="shfw_fixed">售后服务</a>
</li>
<li class="des_act">
<div class="des_buy">
<div class="btnbox">
<a clstag="pageclick|keycount|product_201709214|10" class="add_cart" style="display:none;" id="detail_desc_addCartBtn_fixed" href="javascript:void(0);"><span>加入购物车</span></a>
</div>
<div class="tab_buy_info">
<a href="javascript:void(0);" target="_blank">
<img src="">
</a>
<span class="tab_buy_tit">卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L</span>
<span class="tab_price"></span>
</div>
</div>
</li>
</ul>
</div>
</div>
</div>
<div id="product_desc_tab_div_mask"></div>
<div id="descLazyLoad"></div><div class="des" id="J_des">
<ul class="des_tab">
<li class="des_tabbox" id="detail_desc_tab">
<a clstag="pageclick|keycount|product_201709214|19" tabIndex="0" href="javascript:void(0);" class="tab cur" id="spjs">商品介绍</a>
<a clstag="pageclick|keycount|product_201709214|20" tabIndex="3" href="javascript:void(0);" class="tab" id="sppj">评价<em></em></a>
<a clstag="pageclick|keycount|product_201709214|21" tabIndex="1" href="javascript:void(0);" class="tab" id="ggbz">规格及包装</a>
<a clstag="pageclick|keycount|product_201709214|22" tabIndex="2" href="javascript:void(0);" class="tab" id="shfw">售后服务</a>
</li>
</ul>
<div class="descon" id="detail_desc_content">
<div id="prodDescTabContent">
<div tabIndex="0" class="desitem" style="display:block" id="prodDetailCotentDiv">
<dl class="des_info clearfix">
<dt>
规格参数
<a id="medica_record" class="medica_record" href="" target="_blank"></a>
<a clstag="pageclick|keycount|product_201709214|23" href="javascript:void(0)" onclick="detailProdDesc.onGuigeTabSwitchEvent();" class="s_standard_more">查看更多 »</a>
</dt>
<dd title="品牌：卡宾（CABBEEN）">品牌：卡宾（CABBEEN）</dd>
<dd title="商品名称：卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L">商品名称：卡宾男装时尚红色修身长袖卫衣虎头图案连帽青年街头潮流套头衫B 大红色14 50/175/L</dd>
<dd title="商品编号：16892520062">商品编号：16892520062</dd>
<dd title="商品毛重：500.00g">商品毛重：500.00g</dd>
<!-- 扩展属性 -->
</dl>
<!-- 文描区域 -->
<div class="mod_des">
<div class="desbox">
</div>
</div>
</div>
<!-- 规格及包装tab内容 -->
<div tabIndex="1" class="desitem desqoute" id="detail_desc_prop" style="display:none">
</div>
</div>
<div class="desitem desqoute" id="detail_desc_fwcl">
</div>
</div>
</div>
<div class="clearfix" id='buyer_experience'>
<div id="productExperience" name="productExperience" class="tab"></div>
</div>
</div>
</div> </div>
<!--content end-->
<div class="ft_wrap">
<div id="globalBottomBrowseRelated" data-recordTracker="1"></div>
<div class="wrap ft_footer_service clearfix" id="footerIcon" data-tpa="YHD_GLOBAl_FOOTERICON">
<a target="_blank">
<img alt="" src="//d8.yihaodianimg.com/N05/M0B/39/F3/CgQI0lWskgmADBnsAAAPZvcSh3E68900.jpg"/>
<b>正品保障</b>
<span>正品行货 放心选购</span>
</a>
<a target="_blank">
<img alt="" src="//d6.yihaodianimg.com/N05/M09/96/23/ChEbulWsk4iADa_aAAAM544hHN818600.jpg"/>
<b>满86包邮</b>
<span>满86元 免运费</span>
</a>
<a target="_blank">
<img alt="" src="//d9.yihaodianimg.com/N07/M00/2D/8B/CgQIz1WslI-Adao3AAAN5b_ut2I80100.jpg"/>
<b>售后无忧</b>
<span>7天无理由退货</span>
</a>
<a target="_blank">
<img alt="" src="//d8.yihaodianimg.com/N09/M06/08/C8/ChEi11WsyiyALBbiAAAN9lEEK5M33200.jpg"/>
<b>准时送达</b>
<span>收货时间由你做主</span>
</a>
</div>
<div class="wrap ft_service_link clearfix">
<div id="bottomHelpLinkId" class="ft_help_list clearfix" data-tpa="YHD_GLOBAl_FOOTER_HELP">
<dl>
<dt>新手入门</dt>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=12" target="_blank">购物流程</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=17" target="_blank">会员制度</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=38" target="_blank">订单查询</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=36" target="_blank">发票制度</a></dd>
</dl>
<dl>
<dt>支付方式</dt>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=25" target="_blank">货到付款</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=26" target="_blank">网上支付</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=27" target="_blank">银行转账</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=28" target="_blank">礼品卡支付</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=29" target="_blank">其它支付</a></dd>
</dl>
<dl>
<dt>配送服务</dt>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=21" target="_blank">配送进度查询</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=20" target="_blank">商品验货与签收</a></dd>
</dl>
<dl>
<dt>售后保障</dt>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=31" target="_blank">退换货政策</a></dd>
<dd><a href="//cms.yhd.com/cms/view.do?topicId=43" target="_blank">联系客服</a></dd>
</dl>
</div>
<!--footer 二维码 begin -->
<div class="ft_code_wrap clearfix" data-tpa="YHD_GLOBAl_HEADER_MOBILE" id="footerQRcode">
<div class="ft_mobile_code clearfix">
<p>APP更优惠</p>
<img src="//img.yihaodianimg.com/front-homepage/index/images/qryhd.png?1=1" alt="APP更优惠二维码"/>
</div>
<div class="ft_mobile_code clearfix">
<p>加微信查订单</p>
<img src="//d6.yihaodianimg.com/N10/M01/EC/6D/ChEi3Fj518KAFF5SAABtGRNmQM062100.jpg" alt="加微信查订单二维码"/>
</div>
</div>
</div><div id="footer">
<p class="ft_footer_link">
</p>
<p class="ft_footer_link">
<a href="http://www.miibeian.gov.cn/" target="_blank">沪ICP备16050468号</a>
|
<a href="//cms.yhd.com/cms/view.do?topicId=16" target="_blank">经营证照</a>
|
<a href="//d9.yihaodianimg.com/N10/M05/00/A9/ChEi2lkQGRaAfaeeAAIhVwT2TYo18400.jpg" target="_blank">互联网药品信息服务资格证</a>
|
<a target="_blank">违法和不良信息举报电话：0527-88100253</a>
|
<a href="//d9.yihaodianimg.com/N11/M04/76/1C/ChEwoVnfFfeAfzKUAAg9urXNqaA12000.jpg" target="_blank">沪B2-20170039</a>
</p>
<p>Copyright© 1号店网上超市 2007-2017，All Rights Reserved</p>
<small id="footerbanner2LazyLoad" class="ft_pic_link">
<a href="https://online.unionpay.com/" target="_blank" >
<img alt="" src="//d6.yihaodianimg.com/N00/M01/1A/30/CgMBmVDzwyaAaIMBAAAJZgSEr6I65200.jpg">
</a>
<a href="http://www.gsxt.gov.cn/index.html" target="_blank" >
<img alt="" src="//d6.yihaodianimg.com/N01/M08/19/94/CgQCrlDzwnKAUkfSAAAIPrrML6M92400.jpg">
</a>
<a href="http://www.zx110.org/" target="_blank" >
<img alt="" src="//d8.yihaodianimg.com/N02/M05/19/94/CgQCsVDzw0GABUElAADHlvRfNUk94600.jpg">
</a>
<a href="http://net.china.com.cn/index.htm" target="_blank" >
<img alt="" src="//d9.yihaodianimg.com/N01/M0A/95/FD/CgQCr1PQy1CAF7vaAABDexsiEYM24800.jpg">
</a>
<a href="http://shwg.dianping.com/index.html" target="_blank" >
<img alt="" src="//d9.yihaodianimg.com/N08/M06/6C/9C/ChEi1VcfPl2AC1T8AAANFrEfJlw97300.jpg">
</a>
<a href="http://www.shjbzx.cn" target="_blank" >
<img alt="" src="//d6.yihaodianimg.com/N10/M09/0E/1F/ChEi2lh171KAJrGlAAALl_uZt0E75600.jpg">
</a>
<a href="https://search.szfw.org/cert/l/CX20150608010268010812" target="_blank" >
<img alt="" src="//d9.yihaodianimg.com/N08/M01/C7/7E/ChEi1FYXHcOAVk_WAAAL2r2-yfo10200.jpg">
</a>
<a href="https://ss.knet.cn/verifyseal.dll?sn=e13050631010040492h5mq000000&ct=df&a=1&pa=500267" target="_blank" >
<img alt="" src="//d9.yihaodianimg.com/N01/M03/A0/40/CgQCrlPYTqCASlHXAAAd82JE0eA31000.png">
</a>
</small>
</div></div>
<!--js start-->
<!--无页面级头部js时, 全局头部js下移-->
<script type="text/javascript" src="http://img.yihaodianimg.com/front-detail/global/js/global_base_top.js?20ce613" charset="utf-8"></script>
<script type="text/javascript" src="http://img.yihaodianimg.com/front-detail/detail/js/productDetail.js?20ce613" charset="utf-8"></script>
<script type="text/javascript" src="http://st.360buyimg.com/sso/synccookiepc.js?20ce613" charset="utf-8"></script>
</body>
</html>
<script type="text/javascript">
var jaq = jaq || [];
jaq.push(['account', 'JA2017_111805']); //站点编号
jaq.push(['domain', 'yhd.com']); //站点域名
var extParams = encodeURI("skuId=16892520062");
jaq.push(['extParams', extParams]);
(function () {
var ja = document.createElement('script');
ja.type = 'text/javascript';
ja.async = true;
ja.src = '//wl.jd.com/joya.js';
var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(ja, s);
})();
</script>
'''

#子串的开头匹配
sub='<img'
#子串的结尾匹配
strs='.jpg'
#需要截取的子串长度参考
st1='d6.yihaodianimg.com/N10/M09/0E/1F/ChEi2lh171KAJrGlAAALl_uZt0E75600.jpg'
i=0

pop=-len(sub)
end=-len(strs)
while i<s.count(sub):
    #匹配<img开头
    pop=s.find(sub,end+len(sub)) 
    #匹配.jpg结尾
    end=s.find(strs,pop+len(strs))
    #将上面匹配到的图片地址赋值给t
    t=s[pop:end+len(strs)]
    #在字符串t中查找子串‘d6.yihaodianimg’
    http=t.find('d6.yihaodianimg')
    #用查找的子串与上面的子串截取长度做比较
    if len(t[http:])==len(st1):
        url=t[http:]
        urllib.urlretrieve(url,str(i)+'.jpg')  #测试下载失败了
    #print t
    i+=1




