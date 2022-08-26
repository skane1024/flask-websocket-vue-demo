# Vue and Flask SocketIO 简单示例

# Backend后端

### Prerequisites

python3.9

`pip install -r requirements.txt`

### 运行

进入到backend目录下，运行app.py:

```bash
python app.py
```

# Fronted 前端

### Prerequisites

安装yarn

```
conda install yarn
```

### 运行前端

进入到fronted目录下. 运行一下的命令. 然后在浏览器中打开

```bash
yarn install
yarn run serve --port 8111

# http://your_ip:8111
```

注意:若修改了后端的端口，需要在fronted/src/components/HelloWorld.vue中也修改后端的端口

在建立了socket连接后，后端会不断的向前端推送一些随机数字显示




# References

1. https://github.com/iodriller/VueJs-Flask-SocketIO-Example-Templatehttps://github.com/bioudi/Flask-VueJs-SocketI
   做了一些简化
