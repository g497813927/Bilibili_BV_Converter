# Bilibili_BV_Converter

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fg497813927%2FBilibili_BV_Converter.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fg497813927%2FBilibili_BV_Converter?ref=badge_shield)

[English Version](/README_ENG.md)

### 免责声明

**此项目仅作学习参考，请勿将此项目用于任何的违法行为！由于自己的不当行为使用此项目而导致的一切法律风险，此项目概不负责！**

### TL;DR

Bilibili（B站）BV号转换器，用户只需运行对应的文件，即可快速实现转换。

### BV2CID

---

#### 使用方法

1、带参数

在命令行或终端中直接输入以下内容

```bash
python3 bv2cid.py <BV号> <p数>
```

将此处的\<BV号\>更换为视频的BV号，<p数>更换为视频所需获取的对应p数（第一p为0，第二p为1，以此类推，目前一次只能查询一个p的cid号）。按下回车，即可返回对应CID号（显示语言为系统语言，仅支持`简体中文`和`英文`）

2、不带参数

在命令行或终端内输入以下内容

```bash
python3 bv2cid.py
```

根据提示，选择是否使用系统默认语言运行（目前仅支持`简体中文`和`英文`）

```bash
你当前的系统语言是简体中文，需要更改程序显示语言吗？
Your current language display is Chinese Simplified, do you want to switch language?
(Y/N)
```

选择语言

```bash
1. 简体中文
2. English
请选择语言(Select language):
```

然后根据提示，输入BV号（此处以`简体中文`举例）

```bash
请输入BV号：
```

随后，输入视频所需获取的对应p数（第一p为0，第二p为1，以此类推，目前一次只能查询一个p的cid号）（此处以中文举例）

```bash
请输入你需要查询的对应视频的p数（仅限数字）
（0代表视频第一p，1代表视频第二p，以此类推）
```

稍等片刻，即可获得其对应的CID号

### BV2AV

---

#### 使用方法

1、带参数

在命令行或终端中直接输入以下内容

```bash
python3 bv2av.py <BV号>
```

将此处的\<BV号\>更换为视频的BV号，按下回车，即可返回对应AV号（显示语言为系统语言，仅支持`简体中文`和`英文`）

2、不带参数

在命令行或终端内输入以下内容

```bash
python3 bv2av.py
```

根据提示，选择是否使用系统默认语言运行（目前仅支持`简体中文`和`英文`）

```bash
你当前的系统语言是简体中文，需要更改程序显示语言吗？
Your current language display is Chinese Simplified, do you want to switch language?
(Y/N)
```

选择语言

```bash
1. 简体中文
2. English
请选择语言(Select language):
```

然后根据提示，输入BV号（此处以`简体中文`举例）

```bash
请输入BV号：
```

稍等片刻，即可获得其对应的AV号

### iOS & iPadOS设备兼容方案（BV号转CID号）

正在开发，将在不久后上线。

### iOS & iPadOS设备兼容方案(BV号转AV号)

对于iOS或者iPadOS用户，可以通过“捷径”做到相同效果，请在Safari中直接点击[这里](https://www.icloud.com/shortcuts/75df12ce50e54e62a3bd33b5aefa7218)，导入后即可快速使用

### FAQ

1. Q:

   我没有python，能运行这一个程序吗？

   A:

   此程序必须依赖于python，请从[官网](https://www.python.org/downloads/)下载Python！如果你之前从未用过python或者对python的安装并不熟悉，建议参考这一个网址：[Python3 环境搭建 | 菜鸟教程](https://www.runoob.com/python3/python3-install.html)

2. Q:

   在运行的过程中，程序出现了这样的报错：

   `ModuleNotFoundError: No module named 'requests'`

   应该如何解决？

   A:

   你可能是没有安装所需的依赖`requests`，请通过以下两种方式中的一种进行安装依赖：

   方法一：

   ```bash
   pip3 install requests
   ```

   方法二：

   ```bash
   pip3 install -r <requirement.txt路径>
   ```

   其中，\<requirement.txt路径\>应当更改成程序所在的文件夹中的requirements.txt的路径



### 发现bug？

如果你发现了bug，欢迎在这里提交Pull Request或者Issues，或者联系[admin@vip.techzjc.com](mailto:admin@vip.techzjc.com)。对于每一条回应，都将会尽快回复！



## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fg497813927%2FBilibili_BV_Converter.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fg497813927%2FBilibili_BV_Converter?ref=badge_large)