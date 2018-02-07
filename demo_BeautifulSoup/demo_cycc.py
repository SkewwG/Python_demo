import re
from bs4 import BeautifulSoup
html_doc = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<title>诚殷网络安全技术论坛—CYWL TEAM专注WEB网络安全培训！|渗透培训|WEB安全培训|网站渗透|黑客技术|渗透培训|渗透测试|网站渗透|WEB安全培训|黑客技术培训 - </title>

<meta name="keywords" content="诚殷网络|CYWLTEAM|技术培训|渗透思路|渗透教程|黑客新闻|入侵工具|渗透培训|网站安全培训|入侵基础培训|黑客基础培训|渗透免费培训|网络安全网站|网络安全技术|网络安全|安全bbs" />
<meta name="description" content="CYWL TEAM专注于WEB网络安全培训，我们不收取任何费用，不管你有没有基础，只要你有一颗想学习的心能坚持下去，你学我们就教，欢迎加入我们！ " />
<meta name="MSSmartTagsPreventParsing" content="True" />
<meta http-equiv="MSThemeCompatible" content="Yes" />
<base href="http://www.chinacycc.com/" /><link rel="stylesheet" type="text/css" href="data/cache/style_28_common.css?pLI" />
    <script src="template/qu_zear/img/js/jquery.js" type="text/javascript" type="text/javascript"></script>
    <script src="template/qu_zear/img/js/jquery-1.10.2.min.js" type="text/javascript" type="text/javascript"></script>
<script type="text/javascript">var STYLEID = '28', STATICURL = 'static/', IMGDIR = 'static/image/common', VERHASH = 'pLI', charset = 'gbk', discuz_uid = '1723', cookiepre = '4DGo_2132_', cookiedomain = '', cookiepath = '/', showusercard = '1', attackevasive = '0', disallowfloat = '', creditnotice = '2|金钱|', defaultstyle = '', REPORTURL = 'aHR0cDovL3d3dy5jaGluYWN5Y2MuY29tL3BvcnRhbC5waHA=', SITEURL = 'http://www.chinacycc.com/', JSPATH = 'data/cache/', CSSPATH = 'data/cache/style_', DYNAMICURL = '';var q_jq=jQuery.noConflict();</script>
<script src="data/cache/common.js?pLI" type="text/javascript"></script>
<meta name="application-name" content="诚殷网络安全技术论坛—CYWL TEAM专注WEB网络安全培训！|渗透培训|WEB安全培训|网站渗透|黑客技术|渗透培训|渗透测试|网站渗透|WEB安全培训|黑客技术培训" />
<meta name="msapplication-tooltip" content="诚殷网络安全技术论坛—CYWL TEAM专注WEB网络安全培训！|渗透培训|WEB安全培训|网站渗透|黑客技术|渗透培训|渗透测试|网站渗透|WEB安全培训|黑客技术培训" />
<meta name="msapplication-task" content="name=网站首页;action-uri=http://www.chinacycc.com/portal.php;icon-uri=http://www.chinacycc.com/static/image/common/portal.ico" /><meta name="msapplication-task" content="name=社区;action-uri=http://www.chinacycc.com/forum.php;icon-uri=http://www.chinacycc.com/static/image/common/bbs.ico" />
<script src="data/cache/portal.js?pLI" type="text/javascript"></script>

    <script type="text/javascript">
<!--
window.onerror=function(){return true;}
// -->
</script>
</head>

<body id="nv_portal" class="pg_index" onkeydown="if(event.keyCode==27) return false;">
<div id="append_parent"></div><div id="ajaxwaitid"></div>
        <div class="ainuo_toptb cl">
<div class="wp">
<div class="z"></div>
<div class="y">
                	<a href="javascript:openDiy();" class="diy">打开 DIY 面板</a></div>
</div>
</div>
<div id="toptb" class="cl">
<div class="wp">
            	<div class="z">
                	<a href="./" title="诚殷网络安全技术论坛—CYWL TEAM专注WEB网络安全培训！|渗透培训|WEB安全培训|网站渗透|黑客技术|渗透培训|渗透测试|网站渗透|WEB安全培训|黑客技术培训"><img src="template/qu_zear/img/logo.png" alt="诚殷网络安全技术论坛—CYWL TEAM专注WEB网络安全培训！|渗透培训|WEB安全培训|网站渗透|黑客技术|渗透培训|渗透测试|网站渗透|WEB安全培训|黑客技术培训" border="0" /></a>                </div>
<div class="z qing_toptb">
                	<ul>
                                        <li class="a" id="mn_portal" ><a href="portal.php" hidefocus="true" title="Portal"  >网站首页<span>Portal</span></a></li><li id="mn_forum" ><a href="forum.php" hidefocus="true" title="BBS"  >社区<span>BBS</span></a></li><li id="mn_N7ad4" ><a href="portal.php?mod=topic&topicid=1" hidefocus="true"   style="font-weight: bold;color: red">团队成员</a></li><li id="mn_Nc119" onmouseover="showMenu({'ctrlid':this.id,'ctrlclass':'hover','duration':2})"><a href="#" hidefocus="true"   style="font-weight: bold;color: red">网站导航</a></li><li id="mn_N8261" ><a href="portal.php?mod=topic&topicid=2" hidefocus="true"   style="font-weight: bold;color: purple">加入培训</a></li>                    </ul>
</div>
                <div class="y">
                <style>
#qing_user_menu .showmenu{display:none;}
</style>
<div class="cl qing_af_login">

<a href="space-uid-1723.html" id="qing_user" onMouseOver="showMenu({'ctrlid':'qing_user','ctrlclass':'a'});">skeleton ( <font color="#FF0000">内部成员</font> )<i></i></a>

    <a href="home.php?mod=space&amp;do=notice" id="myprompt" class="a showmenu" onmouseover="showMenu({'ctrlid':'myprompt'});" style="padding-right:0;">提醒</a><span id="myprompt_check"></span>


    <div id="qing_user_menu" class="qing_user_pop" style="display: none;">
<a href="home.php?mod=spacecp&amp;ac=avatar" class="qing_userinfo_avtar" target="_blank"><div class="grid_edit">编辑</div><img src="http://www.chinacycc.com/uc_server/avatar.php?uid=1723&size=middle" /></a>
        <div class="qing_qmenu cl">
<a href="home.php?mod=magic">道具</a>
    <a href="home.php?mod=medal">勋章</a>
    <a href="home.php?mod=task">任务</a>
    <a href="home.php?mod=space&amp;do=blog">日志</a>
    <a href="home.php?mod=space&amp;do=album">相册</a>
    <a href="home.php?mod=space&amp;do=doing">记录</a>
</div>                                <a href="home.php?mod=spacecp&amp;ac=credit&amp;showcredit=1"><span class="z">积分</span><span class="y">609</span></a>
<a href="home.php?mod=spacecp">设置</a>


<a href="member.php?mod=logging&amp;action=logout&amp;formhash=0bb88d56">退出</a>

    </div>
</div>

                </div>

</div>
</div>

<ul id="myprompt_menu" class="p_pop" style="display: none;">
<li><a href="home.php?mod=space&amp;do=pm" id="pm_ntc" style="background-repeat: no-repeat; background-position: 0 50%;"><em class="prompt_news_0"></em>消息</a></li>
<li><a href="home.php?mod=follow&amp;do=follower"><em class="prompt_follower_0"></em>新听众</a></li>
<li class="ignore_noticeli"><a href="javascript:;" onClick="setcookie('ignore_notice', 1);hideMenu('myprompt_menu')" title="暂不提醒"><em class="ignore_notice"></em></a></li>
</ul>
<ul id="myitem_menu" class="p_pop" style="display: none;">
<li><a href="forum.php?mod=guide&amp;view=my">帖子</a></li>
<li><a href="home.php?mod=space&amp;do=favorite&amp;view=me">收藏</a></li>
<li><a href="home.php?mod=space&amp;do=friend">好友</a></li>
</ul>
<div id="hd">
<ul class="p_pop h_pop" id="mn_Nc119_menu" style="display: none"><li><a href="/plugin.php?id=dsu_paulsign:sign" hidefocus="true" >每日签到</a></li><li><a href="/forum.php?mod=guide&view=my" hidefocus="true" >我的帖子</a></li><li><a href="/home.php?mod=space&do=friend" hidefocus="true" >我的好友</a></li><li><a href="/home.php?mod=space&do=wall" hidefocus="true" >我的留言</a></li><li><a href="/home.php?mod=space&do=favorite&view=me" hidefocus="true" >我的收藏</a></li></ul><div class="p_pop h_pop" id="mn_userapp_menu" style="display: none"></div><div id="mu" class="cl">
                <div class="wp cl" style="padding:0;">
</div>
                </div></div>

<script>
		(function(){
		   var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?c7cd27eee126072a3ab03e0ca147d864":"https://jspassport.ssl.qhimg.com/11.0.1.js?c7cd27eee126072a3ab03e0ca147d864";
		   document.write('<script src="' + src + '" id="sozz"><\/script>');
		})();
		</script>
<div id="wp" class="wp"></div>
<style id="diy_style" type="text/css">#frameEP51vR {  background-color:transparent !important;background-image:none !important;}#frameoBizbR {  background-color:transparent !important;background-image:none !important;}#framenFimri {  background-color:transparent !important;background-image:none !important;}#framepMv54p {  background-color:transparent !important;background-image:none !important;}#frameNvpm5V {  background-color:transparent !important;background-image:none !important;}#frameGRyiXs {  background-color:transparent !important;background-image:none !important;}#frameMbPRzB {  background-color:transparent !important;background-image:none !important;}#frameOF1X7y {  background-color:transparent !important;background-image:none !important;}#framefMxM2h {  background-color:transparent !important;background-image:none !important;}#framefmv21M {  background-color:transparent !important;background-image:none !important;}#framecpPMeV {  background-color:transparent !important;background-image:none !important;}#frameF5MFpv {  background-color:transparent !important;background-image:none !important;}#frameAf2bfV {  background-color:transparent !important;background-image:none !important;}#frameEYixMi {  background-color:transparent !important;background-image:none !important;}#frameFp625i {  background-color:transparent !important;background-image:none !important;}#framef1yfZM {  background-color:transparent !important;background-image:none !important;}#framefTRyaL {  background-color:transparent !important;background-image:none !important;}#portal_block_1116 {  background-color:transparent !important;background-image:none !important;}#portal_block_1117 {  background-color:transparent !important;background-image:none !important;}#frameHagENA {  background-color:transparent !important;background-image:none !important;}#portal_block_1118 {  background-color:transparent !important;background-image:none !important;}#framed7zvmt {  background-color:transparent !important;background-image:none !important;}#portal_block_1119 {  background-color:transparent !important;background-image:none !important;}#frameZvPM7v {  background-color:transparent !important;background-image:none !important;}#portal_block_1120 {  background-color:transparent !important;background-image:none !important;}#frameyYGlgw {  background-color:transparent !important;background-image:none !important;}#portal_block_1121 {  background-color:transparent !important;background-image:none !important;}#frameUG7FpL {  background-color:transparent !important;background-image:none !important;}#portal_block_1122 {  background-color:transparent !important;background-image:none !important;}#framen5PlEz {  background-color:transparent !important;background-image:none !important;}#portal_block_1123 {  background-color:transparent !important;background-image:none !important;}#framehzTvaF {  background-color:transparent !important;background-image:none !important;}#portal_block_1124 {  background-color:transparent !important;background-image:none !important;}#frameDaL5mY {  background-color:transparent !important;background-image:none !important;}#portal_block_1125 {  background-color:transparent !important;background-image:none !important;}#frameqptllf {  background-color:transparent !important;background-image:none !important;}#portal_block_1126 {  background-color:transparent !important;background-image:none !important;}#portal_block_1127 {  background-color:transparent !important;background-image:none !important;}#frameSLelV7 {  background-color:transparent !important;background-image:none !important;}#portal_block_1128 {  background-color:transparent !important;background-image:none !important;}#frameK5tWrG {  background-color:transparent !important;background-image:none !important;}#frameoAmM7W {  background-color:transparent !important;background-image:none !important;}#frameR7V77m {  background-color:transparent !important;background-image:none !important;}#framenj5TNv {  background-color:transparent !important;background-image:none !important;}#frameazewEa {  background-color:transparent !important;background-image:none !important;}#portal_block_1129 {  background-color:transparent !important;background-image:none !important;}#portal_block_1130 {  background-color:transparent !important;background-image:none !important;}#portal_block_1131 {  background-color:transparent !important;background-image:none !important;}#portal_block_1132 {  background-color:transparent !important;background-image:none !important;}#portal_block_1133 {  background-color:transparent !important;background-image:none !important;}</style>
<div class="wp">
<!--[diy=diy1]--><div id="diy1" class="area"></div><!--[/diy]-->
</div>
<link href="template/qu_zear/img/index/global.css" rel="stylesheet" type="text/css" />
<link href="template/qu_zear/img/index/page.css" rel="stylesheet" type="text/css" />
<div class="wrap">
    <div id="main" style="overflow: initial;">
        <div id="main_banner">
        	<!--[diy=adiy2]--><div id="adiy2" class="area"><div id="framefTRyaL" class="cl_frame_bm frame move-span cl frame-1"><div id="framefTRyaL_left" class="column frame-1-c"><div id="framefTRyaL_left_temp" class="move-span temp"></div><div id="portal_block_1116" class="cl_block_bm block move-span"><div id="portal_block_1116_content" class="dxb_bc"><ul class="banner_first cl"><li class="banner_firstBig">
        <a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" target="_blank">
            <img src="data/attachment/block/9e/9e3fd8e836bf78678e8199e912971f03.jpg" width="560" height="355" />
            <div class="banner_cover"></div>
        </a>
    </li><li>
        <a href="thread-2455-1-1.html" title="Win鬼影集群源码" target="_blank">
            <img src="data/attachment/block/f5/f5da6afa924ee932adc0ef38271f1770.jpg" width="560" height="355" />
            <div class="banner_cover"></div>
        </a>
    </li><li>
        <a href="thread-2454-1-1.html" title="New御剑1.5 - 源码" target="_blank">
            <img src="data/attachment/block/2f/2ff1f0320e3ffdf03fdc3e45b4ca456a.jpg" width="560" height="355" />
            <div class="banner_cover"></div>
        </a>
    </li><li>
        <a href="thread-2453-1-1.html" title="【厉害】一个黑客直播撸京东手机10元！竟然成功了！" target="_blank">
            <img src="data/attachment/block/12/12b4c61a21b6af22bf895b6144d506b9.jpg" width="560" height="355" />
            <div class="banner_cover"></div>
        </a>
    </li><li>
        <a href="thread-2451-1-1.html" title="_(:3 」∠)_记帮表弟(哥)的一次提权" target="_blank">
            <img src="data/attachment/block/87/870ea2e6c5d7e133d4a0f0cc6a23fba6.jpg" width="560" height="355" />
            <div class="banner_cover"></div>
        </a>
    </li></ul>
</div></div><div id="portal_block_1117" class="cl_block_bm block move-span"><div id="portal_block_1117_content" class="dxb_bc"><div class="banner_sliderWrap cl">
    <div class="slider_arrow slider_arrowLeft index_icons global_gaNode" data-galabel="home_banner_arrow_left"></div>
    <div class="slider_arrow slider_arrowRight index_icons global_gaNode" data-galabel="home_banner_arrow_right"></div>
    <div class="banner_slider">
        <ul class="slider_list banner_sliderUl clear"><li class="slider_iterm slider_item8">
                <a href="thread-293-1-1.html" title="织梦日志分析“新姿势”获取密码" target="_blank">
                    <img src="data/attachment/block/47/47fb0e7d2bf3fe904568bbacfca24a7e.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">织梦日志分析“新姿势”获取密</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-284-1-1.html" title="关于如和织梦后台过百度云加速上传网马" target="_blank">
                    <img src="data/attachment/block/b1/b1b077e3fb490f6c84b72830817f20fa.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">关于如和织梦后台过百度云加速</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" target="_blank">
                    <img src="data/attachment/block/cf/cfacfc485e470d10138fcd06a119e8a8.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">Burp详解之Proxy代理模块</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-2446-1-1.html" title="对某c段的一次检测" target="_blank">
                    <img src="data/attachment/block/b9/b9a7eab4e5f298aa57b5848612e663da.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">对某c段的一次检测</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-239-1-1.html" title="审核元素拿企业webshell(新手必学教程)" target="_blank">
                    <img src="data/attachment/block/e3/e37984a85a9ad21f3ab9d411c55f5ef6.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">审核元素拿企业webshell(新手</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-2424-1-1.html" title="【首发】诚殷网络免杀PHP大马" target="_blank">
                    <img src="data/attachment/block/f9/f9883cbd8b8dc23d59bff73422aac066.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">【首发】诚殷网络免杀PHP大马</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-2343-1-1.html" title="诚殷网络WEB渗透工具包" target="_blank">
                    <img src="data/attachment/block/f8/f859b818156f70c2d10e957ecd92ba35.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">诚殷网络WEB渗透工具包</h2>
                    </div>
                </a>
            </li><li class="slider_iterm slider_item8">
                <a href="thread-2218-1-1.html" title="诚殷网络远控使用方法图解" target="_blank">
                    <img src="data/attachment/block/6f/6fdb9969abaf1b1a5a5e906a79f031b1.jpg" width="265" height="168" />
                    <div class="secbanner_cover"></div>
                    <div class="secbanner_title_wrap">
                        <h2 class="secbanner_title">诚殷网络远控使用方法图解</h2>
                    </div>
                </a>
            </li></ul>
    </div>
</div></div></div></div></div><div id="frameEP51vR" class="cl_frame_bm frame move-span cl frame-1"><div id="frameEP51vR_left" class="column frame-1-c"><div id="frameEP51vR_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
        </div>

        <!--瀹樻柟瑙嗛-->
        <div id="main_video">
            <div class="video_wrap">
            	<!--[diy=adiy3]--><div id="adiy3" class="area"><div id="frameHagENA" class="cl_frame_bm frame move-span cl frame-1"><div id="frameHagENA_left" class="column frame-1-c"><div id="frameHagENA_left_temp" class="move-span temp"></div><div id="portal_block_1118" class="cl_block_bm block move-span"><div id="portal_block_1118_content" class="dxb_bc"><div class="portal_block_summary"><div class="index_title cl">
    <div class="index_titleMain">
        <a href="forum.php" target="_blank"><h1>交流版块</h1></a>
        <a href="forum.php" class="index_titleMore" target="_blank">MORE ></a>
    </div>
    <ul class="index_titleList clear">
        <li><a href="forum-56-1.html" target="_blank">渗透思路</a></li>
        <li><a href="forum-64-1.html" target="_blank">新人报道</a></li>
        <li><a href="forum-50-1.html" target="_blank">培训报名</a></li>
        <li><a href="forum-51-1.html" target="_blank">业界资讯</a></li>
    </ul>
</div></div></div></div></div></div><div id="frameoBizbR" class="cl_frame_bm frame move-span cl frame-1"><div id="frameoBizbR_left" class="column frame-1-c"><div id="frameoBizbR_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                <div class="video_container cl">
                	<div class="video_left">
                		<!--[diy=adiy4]--><div id="adiy4" class="area"><div id="framed7zvmt" class="cl_frame_bm frame move-span cl frame-1"><div id="framed7zvmt_left" class="column frame-1-c"><div id="framed7zvmt_left_temp" class="move-span temp"></div><div id="portal_block_1119" class="cl_block_bm block move-span"><div id="portal_block_1119_content" class="dxb_bc"><a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" target="_blank">
    <img src="data/attachment/block/84/847872d1783b14d4c1c18d5c149980a4.jpg" width="374" height="569" />
    <div class="video_titleWrap">
        <span class="video_tip">网站安全-思路</span>
        <h2 class="video_title">Burp详解之Proxy代理模块</h2>
    </div>
    <span class="video_icon index_icons"></span>
    <div class="video_cover video_cover0"></div>
</a></div></div></div></div><div id="framenFimri" class="cl_frame_bm frame move-span cl frame-1"><div id="framenFimri_left" class="column frame-1-c"><div id="framenFimri_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
</div>
                    <ul class="video_right">
                    	<!--[diy=adiy5]--><div id="adiy5" class="area"><div id="frameZvPM7v" class="cl_frame_bm frame move-span cl frame-1"><div id="frameZvPM7v_left" class="column frame-1-c"><div id="frameZvPM7v_left_temp" class="move-span temp"></div><div id="portal_block_1120" class="cl_block_bm block move-span"><div id="portal_block_1120_content" class="dxb_bc"><li class="video_list1">
    <a href="thread-284-1-1.html" title="关于如和织梦后台过百度云加速上传网马" target="_blank">
        <img src="data/attachment/block/df/df598cb9e3eb24bea3b0b6eba26015bb.jpg" width="353" height="275" />
        <div class="video_titleWrap">
            <span class="video_tip">网站安全-思路</span>
            <h2 class="video_title">关于如和织梦后台过百度云加速上传网马</h2>
        </div>
        <span class="video_icon index_icons"></span>
        <div class="video_cover video_cover1"></div>
    </a>
</li><li class="video_list2">
    <a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" target="_blank">
        <img src="data/attachment/block/63/63352fe9b1f975f93e8cc4f14d9b3831.jpg" width="353" height="275" />
        <div class="video_titleWrap">
            <span class="video_tip">网站安全-思路</span>
            <h2 class="video_title">Burp详解之Proxy代理模块</h2>
        </div>
        <span class="video_icon index_icons"></span>
        <div class="video_cover video_cover1"></div>
    </a>
</li><li class="video_list3">
    <a href="thread-2446-1-1.html" title="对某c段的一次检测" target="_blank">
        <img src="data/attachment/block/17/17f01db85ff59e4169df282d4565502f.jpg" width="353" height="275" />
        <div class="video_titleWrap">
            <span class="video_tip">网站安全-思路</span>
            <h2 class="video_title">对某c段的一次检测</h2>
        </div>
        <span class="video_icon index_icons"></span>
        <div class="video_cover video_cover1"></div>
    </a>
</li><li class="video_list4">
    <a href="thread-293-1-1.html" title="织梦日志分析“新姿势”获取密码" target="_blank">
        <img src="data/attachment/block/02/02726c65926ddcf0edc6d36cc923f80b.jpg" width="353" height="275" />
        <div class="video_titleWrap">
            <span class="video_tip">网站安全-思路</span>
            <h2 class="video_title">织梦日志分析“新姿势”获取密码</h2>
        </div>
        <span class="video_icon index_icons"></span>
        <div class="video_cover video_cover1"></div>
    </a>
</li></div></div></div></div><div id="framepMv54p" class="cl_frame_bm frame move-span cl frame-1"><div id="framepMv54p_left" class="column frame-1-c"><div id="framepMv54p_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                    </ul>
                </div>
                <!--[diy=adiy6]--><div id="adiy6" class="area"><div id="frameyYGlgw" class="cl_frame_bm frame move-span cl frame-1"><div id="frameyYGlgw_left" class="column frame-1-c"><div id="frameyYGlgw_left_temp" class="move-span temp"></div><div id="portal_block_1121" class="cl_block_bm block move-span"><div id="portal_block_1121_content" class="dxb_bc"><div class="video_series">
    <div class="series_split_line"></div>
    <ul class="series_list cl"><li class="series_item1">
            <a href="thread-293-1-1.html" title="织梦日志分析“新姿势”获取密码" class="series_itemImg" target="_blank">
                <img src="data/attachment/block/e2/e2cd3d6fc1ef16d98a3f0d7d2c658a96.jpg" width="265" height="145" />
                <span class="video_icon index_icons"></span>
                <div class="video_seriesCover"></div>
            </a>
            <a href="thread-293-1-1.html" title="织梦日志分析“新姿势”获取密码" target="_blank">
                <h3 class="series_subTitle">织梦日志分析“新姿势”获取密码</h3>
            </a>
        </li><li class="series_item2">
            <a href="thread-284-1-1.html" title="关于如和织梦后台过百度云加速上传网马" class="series_itemImg" target="_blank">
                <img src="data/attachment/block/45/45b1026fb752629d8df0b7d9c073b0fe.jpg" width="265" height="145" />
                <span class="video_icon index_icons"></span>
                <div class="video_seriesCover"></div>
            </a>
            <a href="thread-284-1-1.html" title="关于如和织梦后台过百度云加速上传网马" target="_blank">
                <h3 class="series_subTitle">关于如和织梦后台过百度云加速上传网马</h3>
            </a>
        </li><li class="series_item3">
            <a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" class="series_itemImg" target="_blank">
                <img src="data/attachment/block/e6/e66adde5eab67a1f39e8f9e70299dd39.jpg" width="265" height="145" />
                <span class="video_icon index_icons"></span>
                <div class="video_seriesCover"></div>
            </a>
            <a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" target="_blank">
                <h3 class="series_subTitle">Burp详解之Proxy代理模块</h3>
            </a>
        </li><li class="series_item4">
            <a href="thread-2446-1-1.html" title="对某c段的一次检测" class="series_itemImg" target="_blank">
                <img src="data/attachment/block/75/750f6570a7668cb4b62f894b9a4b5800.jpg" width="265" height="145" />
                <span class="video_icon index_icons"></span>
                <div class="video_seriesCover"></div>
            </a>
            <a href="thread-2446-1-1.html" title="对某c段的一次检测" target="_blank">
                <h3 class="series_subTitle">对某c段的一次检测</h3>
            </a>
        </li></ul>
</div>
</div></div></div></div><div id="frameNvpm5V" class="cl_frame_bm frame move-span cl frame-1"><div id="frameNvpm5V_left" class="column frame-1-c"><div id="frameNvpm5V_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
            </div>
        </div>

        <!--OK鎺ㄨ崘-->
        <div id="main_plusRecom">
            <div class="plus_wrap">
            	<!--[diy=adiy7]--><div id="adiy7" class="area"><div id="frameUG7FpL" class="cl_frame_bm frame move-span cl frame-1"><div id="frameUG7FpL_left" class="column frame-1-c"><div id="frameUG7FpL_left_temp" class="move-span temp"></div><div id="portal_block_1122" class="cl_block_bm block move-span"><div id="portal_block_1122_content" class="dxb_bc"><div class="portal_block_summary"><div class="index_title cl">
    <div class="index_titleMain">
        <a class="plusRecom_title" href=""><h1>最新资讯</h1></a>
        <a class="index_titleMore" href="">MORE ></a>
    </div>
</div></div></div></div></div></div><div id="frameGRyiXs" class="cl_frame_bm frame move-span cl frame-1"><div id="frameGRyiXs_left" class="column frame-1-c"><div id="frameGRyiXs_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->

                <div class="plus_recommend">
                    <div class="recom_wrap cl">
                        <div class="recom_top cl">
                            <div class="recom_topLeft">
                            	<!--[diy=adiy8]--><div id="adiy8" class="area"><div id="framen5PlEz" class="cl_frame_bm frame move-span cl frame-1"><div id="framen5PlEz_left" class="column frame-1-c"><div id="framen5PlEz_left_temp" class="move-span temp"></div><div id="portal_block_1123" class="cl_block_bm block move-span"><div id="portal_block_1123_content" class="dxb_bc"><a href="thread-2453-1-1.html" title="【厉害】一个黑客直播撸京东手机10元！竟然成功了！" target="_blank">
    <img src="data/attachment/block/28/283a3c1263363a14664b842ac05ffbf2.jpg" width="834" height="260" />
    <div class="recom_titleWrap">
        <h3 class="recom_title">【厉害】一个黑客直播撸京东手机10元！竟然成功了！</h3>
        <span class="recom_total index_icons">159</span>
    </div>
    <div class="plus_cover"></div>
</a></div></div></div></div><div id="frameMbPRzB" class="cl_frame_bm frame move-span cl frame-1"><div id="frameMbPRzB_left" class="column frame-1-c"><div id="frameMbPRzB_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->

                            </div>
                            <div class="recom_topRight">
                            	<!--[diy=adiy9]--><div id="adiy9" class="area"><div id="framehzTvaF" class="cl_frame_bm frame move-span cl frame-1"><div id="framehzTvaF_left" class="column frame-1-c"><div id="framehzTvaF_left_temp" class="move-span temp"></div><div id="portal_block_1124" class="cl_block_bm block move-span"><div id="portal_block_1124_content" class="dxb_bc"><a href="thread-196-1-1.html" title="[全网最新]中新网今日11时左右网站被黑" target="_blank">
    <img src="data/attachment/block/86/8650eec05e7fe7ff99601b2ca78bac9c.jpg" width="265" height="261" />
    <div class="recom_titleWrap">
        <h3 class="recom_title">[全网最新]中新网今日11时左右网站被黑</h3>
        <span class="recom_total index_icons">3309</span>
    </div>
    <div class="plus_cover plus_coverR"></div>
</a></div></div></div></div><div id="frameOF1X7y" class="cl_frame_bm frame move-span cl frame-1"><div id="frameOF1X7y_left" class="column frame-1-c"><div id="frameOF1X7y_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                            </div>
                        </div>
                        <!--[diy=adiy10]--><div id="adiy10" class="area"><div id="frameDaL5mY" class="cl_frame_bm frame move-span cl frame-1"><div id="frameDaL5mY_left" class="column frame-1-c"><div id="frameDaL5mY_left_temp" class="move-span temp"></div><div id="portal_block_1125" class="cl_block_bm block move-span"><div id="portal_block_1125_content" class="dxb_bc"><div class="recom_list">
    <ul><li class="recom_item1">
            <a href="thread-2453-1-1.html" title="【厉害】一个黑客直播撸京东手机10元！竟然成功了！" target="_blank">
                <img src="data/attachment/block/ac/acfcf410da52ff357ab93d9dd3c6aede.jpg" width="265" height="155" />
                <div class="plus_cover plus_coverBottom"></div>
            </a>
            <a href="thread-2453-1-1.html" title="【厉害】一个黑客直播撸京东手机10元！竟然成功了！" target="_blank"><h3 class="recom_title">【厉害】一个黑客直播撸京东手机10元！竟然成功了！</h3></a>
            <span class="recom_total index_icons">159</span>
        </li><li class="recom_item2">
            <a href="thread-2403-1-1.html" title="下一波“永恒之蓝”6月见？Shadow Brokers组织宣布将公开更多0day漏洞！" target="_blank">
                <img src="data/attachment/block/2f/2f2e1e1d0ee97d1532e3c94fcdb0c26a.jpg" width="265" height="155" />
                <div class="plus_cover plus_coverBottom"></div>
            </a>
            <a href="thread-2403-1-1.html" title="下一波“永恒之蓝”6月见？Shadow Brokers组织宣布将公开更多0day漏洞！" target="_blank"><h3 class="recom_title">下一波“永恒之蓝”6月见？Shadow Brokers组织宣布将公开更多0</h3></a>
            <span class="recom_total index_icons">1212</span>
        </li><li class="recom_item3">
            <a href="thread-2402-1-1.html" title="企业遇到黑客勒索，我们应该怎么办？" target="_blank">
                <img src="data/attachment/block/90/90d56c80431ce42dd69397d28f3cf477.jpg" width="265" height="155" />
                <div class="plus_cover plus_coverBottom"></div>
            </a>
            <a href="thread-2402-1-1.html" title="企业遇到黑客勒索，我们应该怎么办？" target="_blank"><h3 class="recom_title">企业遇到黑客勒索，我们应该怎么办？</h3></a>
            <span class="recom_total index_icons">1140</span>
        </li><li class="recom_item4">
            <a href="thread-2375-1-1.html" title="【CVE-2017-0290】Windows 史上最严重高危漏洞，可远程控制任意系统【附带POC】" target="_blank">
                <img src="data/attachment/block/72/72548364ba125fe3b1cc73df0c270e20.jpg" width="265" height="155" />
                <div class="plus_cover plus_coverBottom"></div>
            </a>
            <a href="thread-2375-1-1.html" title="【CVE-2017-0290】Windows 史上最严重高危漏洞，可远程控制任意系统【附带POC】" target="_blank"><h3 class="recom_title">【CVE-2017-0290】Windows 史上最严重高危漏洞，可远程控制任</h3></a>
            <span class="recom_total index_icons">1347</span>
        </li></ul>
</div>
</div></div></div></div><div id="framefMxM2h" class="cl_frame_bm frame move-span cl frame-1"><div id="framefMxM2h_left" class="column frame-1-c"><div id="framefMxM2h_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                    </div>
                </div>
            </div>
        </div>

        <!--娣卞害濂芥枃-->
        <div id="main_plusArt">
            <div class="plus_article">
            	<!--[diy=adiy11]--><div id="adiy11" class="area"><div id="frameqptllf" class="cl_frame_bm frame move-span cl frame-1"><div id="frameqptllf_left" class="column frame-1-c"><div id="frameqptllf_left_temp" class="move-span temp"></div><div id="portal_block_1126" class="cl_block_bm block move-span"><div id="portal_block_1126_content" class="dxb_bc"><div class="portal_block_summary"><div class="index_title cl">
    <div class="index_titleMain">
        <a class="plusArt_title" href=""><h1>最新好文</h1></a>
        <a class="index_titleMore" href="">MORE ></a>
    </div>
</div></div></div></div><div id="portal_block_1127" class="cl_block_bm block move-span"><div id="portal_block_1127_content" class="dxb_bc"><div class="art_wrap cl">
    <ul class="art_list cl"><li class="article_item article_item1">
            <a href="thread-2458-1-1.html" title="Burp详解之Proxy代理模块" target="_blank">
                <div class="img_box"><img src="data/attachment/block/76/768cff9f5921e6946156b7efe4f232b8.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">Burp详解之Proxy代理模块</h3>
                <p class="article_content">
1   Proxy代理模块

Forward 只放过当前一个包Drop丢包2   History2-1、审查元素的功能


2-2   过滤器


3   Options
</p>
                <span class="article_total index_icons">2</span>
            </a>
        </li><li class="article_item article_item2">
            <a href="thread-2453-1-1.html" title="【厉害】一个黑客直播撸京东手机10元！竟然成功了！" target="_blank">
                <div class="img_box"><img src="data/attachment/block/ac/acfcf410da52ff357ab93d9dd3c6aede.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">【厉害】一个黑客直播撸京东手机10元！竟然</h3>
                <p class="article_content">
近日有个FD群，小编准备去看看小学生是怎么玩转逻辑漏洞的
于是我加了下面这个群





1900多人，但是群主的QQ才1星
</p>
                <span class="article_total index_icons">159</span>
            </a>
        </li><li class="article_item article_item3">
            <a href="thread-2451-1-1.html" title="_(:3 」∠)_记帮表弟(哥)的一次提权" target="_blank">
                <div class="img_box"><img src="data/attachment/block/9c/9c21a70865f93575b93ecf541a721c4f.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">_(:3 」∠)_记帮表弟(哥)的一次提权</h3>
                <p class="article_content">
废话不多说，事情是这样的。
------------------我是华丽的分割线
然后

过程我就不还原了，我知识跟大家说一下思路！（马好
</p>
                <span class="article_total index_icons">119</span>
            </a>
        </li><li class="article_item article_item4">
            <a href="thread-2449-1-1.html" title="一些脑图分享（NMAP，python，php，逻辑等）" target="_blank">
                <div class="img_box"><img src="data/attachment/block/86/868443b177d4a5c0f96d538c6ed02bd1.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">一些脑图分享（NMAP，python，php，逻辑等</h3>
                <p class="article_content">
运维安全
渗透的艺术
渗透测试
浏览器安全思维导图
情报收集脑图
密码找回逻辑漏洞
安全运维脑图
企业安全防御思维
</p>
                <span class="article_total index_icons">0</span>
            </a>
        </li><li class="article_item article_item5">
            <a href="thread-2446-1-1.html" title="对某c段的一次检测" target="_blank">
                <div class="img_box"><img src="data/attachment/block/a6/a6e346329cb1a1ad640f4a9f36852f38.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">对某c段的一次检测</h3>
                <p class="article_content">
1.进入后台

我用论坛上下的诚殷web渗透工具包扫描某c段，意外的扫到了一个初始化快云web服务器管理助手的页面，进去一看可以
</p>
                <span class="article_total index_icons">158</span>
            </a>
        </li><li class="article_item article_item6">
            <a href="thread-2444-1-1.html" title="_(:3 」∠)_ 检测网站之不一样的思路(另类)" target="_blank">
                <div class="img_box"><img src="data/attachment/block/ab/ab18a91ef22d8d781f5e9c915f4efba5.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">_(:3 」∠)_ 检测网站之不一样的思路(另类)</h3>
                <p class="article_content">
今天在做项目的时候检测到一个网站很有意思，给大家分享一下。系统基本上都是一个登陆界面啊，很烦不扯淡了，界面主要是这样的。
</p>
                <span class="article_total index_icons">67</span>
            </a>
        </li><li class="article_item article_item7">
            <a href="thread-2439-1-1.html" title="代码安全之上传漏洞的几种方式" target="_blank">
                <div class="img_box"><img src="data/attachment/block/d5/d5dc92d55c527f753109115fa38e1814.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">代码安全之上传漏洞的几种方式</h3>
                <p class="article_content">
上传数据包

从数据包中可以看出，验证文件类型的参数有：Content-Type、Filename、Filedata。
客户端JS验证
原理介绍

通
</p>
                <span class="article_total index_icons">100</span>
            </a>
        </li><li class="article_item article_item8">
            <a href="thread-2437-1-1.html" title="逆向追踪之反查Ddos攻击" target="_blank">
                <div class="img_box"><img src="data/attachment/block/63/6356e9cc73fe5bccdfdf985699933e06.jpg" width="265" height="155" />
                    <div class="plus_article_cover"></div>
                </div>
                <h3 class="article_title yellow_line">逆向追踪之反查Ddos攻击</h3>
                <p class="article_content">
一个朋友叫我帮忙看看一个国内某金融公司服务器一直被D，叫我 看看源头是那，于是干着白帽子职业的开始了反追踪的路。首先导
</p>
                <span class="article_total index_icons">53</span>
            </a>
        </li></ul>
    <div class="art_listArrow">
        <span class="page_arrow arrow_left index_icons" data-galabel="home_plus_dot_left"></span>
        <span class="page_arrow arrow_right index_icons unclick" data-galabel="home_plus_dot_right"></span>
    </div>
</div>
</div></div></div></div><div id="framefmv21M" class="cl_frame_bm frame move-span cl frame-1"><div id="framefmv21M_left" class="column frame-1-c"><div id="framefmv21M_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
            </div>
        </div>

        <!--鎵嬫満宸ュ叿-->
        <div id="main_phone">
            <div class="phone_wrap cl">
            	<!--[diy=adiy12]--><div id="adiy12" class="area"><div id="frameSLelV7" class="cl_frame_bm frame move-span cl frame-1"><div id="frameSLelV7_left" class="column frame-1-c"><div id="frameSLelV7_left_temp" class="move-span temp"></div><div id="portal_block_1128" class="cl_block_bm block move-span"><div id="portal_block_1128_content" class="dxb_bc"><div class="portal_block_summary"><div class="index_title cl">
    <div class="index_titleMain">
        <a class="plusArt_title" href="forum.php?mod=forumdisplay&fid=60"target="_blank"><h1>渗透工具</h1></a>
        <a class="index_titleMore" href="forum.php?gid=55"target="_blank">MORE ></a>
    </div>
</div></div></div></div></div></div><div id="framecpPMeV" class="cl_frame_bm frame move-span cl frame-1"><div id="framecpPMeV_left" class="column frame-1-c"><div id="framecpPMeV_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                <ul class="phone_component list_pic_3 cl">
                    <li class="each_0">
                    	<!--[diy=adiy13]--><div id="adiy13" class="area"><div id="frameK5tWrG" class="cl_frame_bm frame move-span cl frame-1"><div id="frameK5tWrG_left" class="column frame-1-c"><div id="frameK5tWrG_left_temp" class="move-span temp"></div><div id="portal_block_1129" class="cl_block_bm block move-span"><div id="portal_block_1129_content" class="dxb_bc"><a href="thread-2455-1-1.html" title="Win鬼影集群源码" target="_blank"><img src="data/attachment/block/d2/d2b095b103071756271f880b4822fc62.jpg" width="560" height="448" /></a></div></div></div></div><div id="frameF5MFpv" class="cl_frame_bm frame move-span cl frame-1"><div id="frameF5MFpv_left" class="column frame-1-c"><div id="frameF5MFpv_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                    </li>
                    <li class="each_1">
                    	<!--[diy=adiy14]--><div id="adiy14" class="area"><div id="frameoAmM7W" class="cl_frame_bm frame move-span cl frame-1"><div id="frameoAmM7W_left" class="column frame-1-c"><div id="frameoAmM7W_left_temp" class="move-span temp"></div><div id="portal_block_1130" class="cl_block_bm block move-span"><div id="portal_block_1130_content" class="dxb_bc"><a href="thread-1785-1-1.html" title="常见的网站源码打包" target="_blank"><img src="data/attachment/block/dc/dc1bb10ae2c414b0b7ac0ef2ada384fb.jpg" width="560" height="224" /></a></div></div></div></div><div id="frameAf2bfV" class="cl_frame_bm frame move-span cl frame-1"><div id="frameAf2bfV_left" class="column frame-1-c"><div id="frameAf2bfV_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                    </li>
                    <li class="each_2">
                    	<!--[diy=adiy15]--><div id="adiy15" class="area"><div id="frameR7V77m" class="cl_frame_bm frame move-span cl frame-1"><div id="frameR7V77m_left" class="column frame-1-c"><div id="frameR7V77m_left_temp" class="move-span temp"></div><div id="portal_block_1131" class="cl_block_bm block move-span"><div id="portal_block_1131_content" class="dxb_bc"><a href="thread-462-1-1.html" title="08exp/DZ/phpcms/phpweb/等等40多种CMS/exp大集合" target="_blank"><img src="data/attachment/block/b7/b7832906dd50cbd56d7e16f9ec69f43c.jpg" width="280" height="224" /></a></div></div></div></div><div id="frameEYixMi" class="cl_frame_bm frame move-span cl frame-1"><div id="frameEYixMi_left" class="column frame-1-c"><div id="frameEYixMi_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                    </li>
                    <li class="each_3">
                    	<!--[diy=adiy16]--><div id="adiy16" class="area"><div id="framenj5TNv" class="cl_frame_bm frame move-span cl frame-1"><div id="framenj5TNv_left" class="column frame-1-c"><div id="framenj5TNv_left_temp" class="move-span temp"></div><div id="portal_block_1132" class="cl_block_bm block move-span"><div id="portal_block_1132_content" class="dxb_bc"></div></div></div></div><div id="frameFp625i" class="cl_frame_bm frame move-span cl frame-1"><div id="frameFp625i_left" class="column frame-1-c"><div id="frameFp625i_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->
                    </li>
                </ul>
                <!--[diy=adiy17]--><div id="adiy17" class="area"><div id="frameazewEa" class="cl_frame_bm frame move-span cl frame-1"><div id="frameazewEa_left" class="column frame-1-c"><div id="frameazewEa_left_temp" class="move-span temp"></div><div id="portal_block_1133" class="cl_block_bm block move-span"><div id="portal_block_1133_content" class="dxb_bc"><ul class="phone_listWrap cl"><li class="phone_listItem phone_listItem1">
    <a href="thread-2455-1-1.html" title="Win鬼影集群源码" target="_blank">
        <img src="data/attachment/block/c7/c7b227be0b53c02cffff067f80572005.jpg" width="265" height="205" class="phone_listImg" />
        <div class="lab_title_wrap">
            <h2 class="secbanner_title">Win鬼影集群源码</h2>
        </div>
    </a>
</li><li class="phone_listItem phone_listItem2">
    <a href="thread-2454-1-1.html" title="New御剑1.5 - 源码" target="_blank">
        <img src="data/attachment/block/22/22421d28fdd954b9f6bc04ce3d535d44.jpg" width="265" height="205" class="phone_listImg" />
        <div class="lab_title_wrap">
            <h2 class="secbanner_title">New御剑1.5 - 源码</h2>
        </div>
    </a>
</li><li class="phone_listItem phone_listItem3">
    <a href="thread-2450-1-1.html" title="一款不错的PowerShell后门（无毒，隐蔽性极强！）" target="_blank">
        <img src="data/attachment/block/75/75013b341fb0804cb8200c5d71f13a3e.jpg" width="265" height="205" class="phone_listImg" />
        <div class="lab_title_wrap">
            <h2 class="secbanner_title">一款不错的PowerShell后门（无毒，</h2>
        </div>
    </a>
</li><li class="phone_listItem phone_listItem4">
    <a href="thread-2440-1-1.html" title="邮箱信息收集工具Py版本" target="_blank">
        <img src="data/attachment/block/9c/9ca4e7bfeef6f1768b6e49bf2081ba6c.jpg" width="265" height="205" class="phone_listImg" />
        <div class="lab_title_wrap">
            <h2 class="secbanner_title">邮箱信息收集工具Py版本</h2>
        </div>
    </a>
</li></ul></div></div></div></div><div id="framef1yfZM" class="cl_frame_bm frame move-span cl frame-1"><div id="framef1yfZM_left" class="column frame-1-c"><div id="framef1yfZM_left_temp" class="move-span temp"></div></div></div></div><!--[/diy]-->

            </div>
        </div>
    </div>
</div>

<script src="template/qu_zear/img/js/libs_bd5c2.js" type="text/javascript"></script>
<script src="template/qu_zear/img/js/page_d849ffd152.js" type="text/javascript"></script>
<script>
q_jq(function() {

Z.use('index/page');
Z.use('global/header');
Z.use('footer/footer');
});
</script>

<div id="wp" class="wp">	</div>


<script type="text/javascript">
_attachEvent(window, 'load', getForbiddenFormula, document);
function getForbiddenFormula() {
var toGetForbiddenFormulaFIds = function () {
ajaxget('plugin.php?id=cloudsearch&formhash=0bb88d56');
};
var a = document.body.getElementsByTagName('a');
for(var i = 0;i < a.length;i++){
if(a[i].getAttribute('sc')) {
a[i].setAttribute('mid', hash(a[i].href));
a[i].onmousedown = function() {toGetForbiddenFormulaFIds();};
}
}
var btn = document.body.getElementsByTagName('button');
for(var i = 0;i < btn.length;i++){
if(btn[i].getAttribute('sc')) {
btn[i].setAttribute('mid', hash(btn[i].id));
btn[i].onmousedown = function() {toGetForbiddenFormulaFIds();};
}
}
}
</script>



<div id="ft" class="qing_foot cl">
<div class="wp cl">
<div id="flk" class="z">
<p>
<a href="http://wpa.qq.com/msgrd?V=3&amp;Uin=800800800&amp;Site=诚殷网络安全技术论坛—CYWL TEAM专注WEB网络安全培训！|渗透培训|WEB安全培训|网站渗透|黑客技术|渗透培训|渗透测试|网站渗透|WEB安全培训|黑客技术培训&amp;Menu=yes&amp;from=discuz" target="_blank" title="QQ"><img src="static/image/common/site_qq.jpg" alt="QQ" /></a><span class="pipe">|</span><a href="javascript:;"  onclick="showWindow('miscreport', 'misc.php?mod=report&url='+REPORTURL);return false;">举报</a><span class="pipe">|</span><a href="forum.php?mobile=yes" >手机版</a><span class="pipe">|</span><a href="forum.php?mod=misc&action=showdarkroom" >小黑屋</a><span class="pipe">|</span><a href="http://www.chinacycc.com/" target="_blank">诚殷网络安全技术论坛</a>
( <a href="http://www.miitbeian.gov.cn/" target="_blank">琼ICP备15002356号</a> )<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1260964552'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s95.cnzz.com/z_stat.php%3Fid%3D1260964552%26show%3Dpic' type='text/javascript'%3E%3C/script%3E"));</script></p>
</div>
<div id="frt" class="y">
<p>Powered by <a href="http://www.discuz.net" target="_blank">Discuz!</a> <em>X3.3</em> &copy; 2001-2016 <a href="http://www.comsenz.com" target="_blank">Comsenz Inc.</a></p>
</div></div>
</div>
<script src="home.php?mod=spacecp&ac=pm&op=checknewpm&rand=1497074943" type="text/javascript"></script>
<script src="home.php?mod=misc&ac=sendmail&rand=1497074943" type="text/javascript"></script>
<div id="scrolltop" class="js_scrolltop">
<a title="返回顶部" class="scrolltopa">
    	<s class="scrolltopb"><img src="template/qu_zear/img/icon/scrolltop_2.png" /></s>
        <b>返回顶部</b>
</a>
</div>
<script src="template/qu_zear/img/js/jquery.forum.js" type="text/javascript"></script>
<script type="text/javascript">_attachEvent(window, 'scroll', function () { showTopLink(); });checkBlind();</script>
			<div id="discuz_tips" style="display:none;"></div>
			<script type="text/javascript">
				var tipsinfo = '38338147|X3.3|0.6||1|C71CBAA6B29A538679F2B82F9B535B42|1723|35|1497074943|6a02d6d10ee89c08769a429be8983d4e|2';
			</script>
			<script src="http://discuz.gtimg.cn/cloud/scripts/discuz_tips.js?v=1" type="text/javascript" charset="UTF-8"></script></body>
</html>
'''

soup = BeautifulSoup(html_doc,'html.parser')
print('获取所有链接')
links = soup.find_all('a')
for link in links:
    print(link['href'],link.get_text())