html = """
<script type="text/javascript">
    var fp = new FlexPaperViewer(
        'http://bulletin.sntba.com/FlexPaperViewer',
        'viewerPlaceHolder', {
            config : {
                SwfFile : escape('http://bulletin.sntba.com/project//2020-01/noticeFile/Z6101002181N01555001/8aa946a756a24b09aded43c7bdd5f348.swf'),
                EncodeURI : true,
                Scale : 0.6,
                ZoomTransition : 'easeOut',
                ZoomTime : 0.5,
                ZoomInterval : 0.05,
                FitPageOnLoad : true,
                FitWidthOnLoad : true,
                PrintEnabled: false,//是否支持打印
                FullScreenAsMaxWindow : false,
                ProgressiveLoading : true,
                MinZoomSize : 0.05,
                MaxZoomSize : 5,
                SearchMatchAll : false,
                InitViewMode : 'Portrait',
                ViewModeToolsVisible : true,
                ZoomToolsVisible : true,
                NavToolsVisible : true,
                CursorToolsVisible : true,
                SearchToolsVisible : false,
                localeChain : 'zh_CN'
            }
        });
</script>
"""

import re


# 在正则语法中具有特殊含义的字符, \d \w \s {} () . ...
result = re.findall("SwfFile : escape\('(.*?)'\),", html, re.S)
print(result)