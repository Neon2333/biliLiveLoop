## Ubuntu环境

## 安装ffmpeg库

```bash
sudo apt install ffmpeg
```

## 安装python3

```bash
sudo apt install python3
```

## 你自己的直播间

URL：

https://link.bilibili.com/p/center/index#/my-room/start-live

步骤：

* 选择直播分类

* 输入房间标题

* 点击【开始直播】

* 点击【串流秘钥】右侧【复制】

* 运行`biliLiveLoop.py`脚本

  ```bash
  ./biliLiveLoop.py
  ```

* 根据提示输入并回车

  将直播间拷贝的【串流秘钥】按下shift+insert复制到脚本提示输入处

* Ctrl+c终止进程

