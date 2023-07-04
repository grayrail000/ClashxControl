# ClashxControl
一个批量修改Clashx配置文件的脚本

在hosts文件增加域名
```yaml
hosts:
  #设置要代理的域名
  www.nivod4.tv: 127.0.0.1
  godamanga.com: 127.0.0.1
  baozimh.org: 127.0.0.1
exclude_files:
  #排除修改的文件    
  - AddHosts.yaml
  - config.yaml
  # 默认的配置文件,不建议修改

```