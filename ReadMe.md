# Cms_Identify

CMS识别脚本，基于指纹库识别，也就是说只需要更新指纹库，就可以识别更多的框架。

**requirements** : `pip install -r requirements.txt`

**env** : python3

### Usage

```sh
> python3 Awrrays.py -h

usage:
    _____ ___ _   _  ____ _____ ____  ____  ____  ___ _   _ _____
   |  ___|_ _| \ | |/ ___| ____|  _ \|  _ \|  _ \|_ _| \ | |_   _|
   | |_   | ||  \| | |  _|  _| | |_) | |_) | |_) || ||  \| | | |
   |  _|  | || |\  | |_| | |___|  _ <|  __/|  _ < | || |\  | | |
   |_|   |___|_| \_|\____|_____|_| \_\_|   |_| \_\___|_| \_| |_|

                                                        by: Awrrays.

CMS recognition tool.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Single url recognition.
  -f FILENAME, --filename FILENAME
                        For batch recognition, please enter the file name.
  -t THREADNUM, --threadnum THREADNUM
                        Specify the number of threads, default=15
  --level {1,2,3}       Level 1: index identify; Level 2: keyword identify;
                        Level 3: md5 identify; default=1
```

### Scan Level

1. Level 1 ： Index为请求首页的响应  (列表格式，正则匹配，添加指纹注意转义)
   1. head - Response header
   2. title - Html Title
   3. body - Html code
2. Level 2 ：Keywords为匹配特定文件的特定字符串
3. Level 3 ：文件md5值匹配(不推荐)

### Finger Json

指纹库放置于"/lib/CMS_FINGER.json"。

<!--指纹库更新于2020/05/05-->

模板如下：

```json
{
	"cms": {
        "md5": {
            "/images/submit.jpg": "47f025f42749b4c802cbd00cc3b57c74",
        },
        "index": {
            "head": [
             	"response",   
            ],
            "title": [
             	"Power by xxcms"   
            ],
            "body": [
                "/templates/default/css/common.css",
                "content=\"xxCMS"
            ]
        },
        "keyword": {
            "/robots.txt": "/index.php"
        }
}
```

![](https://img.shields.io/badge/Powerd%20By-Awrrays-blue)

