# Bilibili_BV_Converter

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

[中文版](/README.md)

### Disclaimer

**This project is only for study purpose, DO NOT use this project to do any illegal behavior! This project is not responsible for any legal risks caused by its own misuse of this project!**

### TL;DR

Bilibili(a famous video website in China) Converter for BV number. Users only need to run the program to obtain the data they want.

### BV2CID

---

#### Usage

1. With Parameters

Input following line in your terminal(Linux & macOS) or Command Prompt(Windows)

```bash
python3 bv2cid.py <BV number> <p number>
```

Change \<BV number\> into the BV number of the video, and \<p number\> into the index of the part of the video

Press enter, you will get the CID of the part of the video you queried in your system's default language(Currently only support `Chinese Simplified` and `English`)

2. Without Parameters

Input following line in your terminal(Linux & macOS) or Command Prompt(Windows)

```bash
python3 bv2cid.py
```

Choose whether or not use system's default language(Currently only support `Chinese Simplified` and `English`) to run this program

```
你当前的系统语言不是简体中文，需要更改程序显示语言吗？
Your current language display is English, do you want to switch language?
(Y/N)
```

Select the language you want

```bash
1. 简体中文
2. English
请选择语言(Select language):
```

Then input BV number(use English as an example)

```bash
Please input BV number:
```

After that, input the index of the part of the video you want to(Number only, 0 stands for the first part, 1 stands for the second part, and so on)(use English as an example)

```bash
Please input the index of the part of the video you want to
(Number only, 0 stands for the first part, 1 stands for the second part, and so on):
```

After wait for a while, you will see the CID for the part of the video you queried

### BV2AV

---

#### Usage

1. With Parameters

Input following line in your terminal(Linux & macOS) or Command Prompt(Windows)

```bash
python3 bv2av.py <BV number>
```

Change \<BV number\> into the BV number of the video

Press enter, you will get the AV number of that video in your system's default language(Currently only support `Chinese Simplified` and `English`)

2. Without Parameters

Input following line in your terminal(Linux & macOS) or Command Prompt(Windows)

```bash
python3 bv2av.py
```
Choose whether or not use system's default language(Currently only support `Chinese Simplified` and `English`) to run this program
```
你当前的系统语言不是简体中文，需要更改程序显示语言吗？
Your current language display is English, do you want to switch language?
(Y/N)
```

Select the language you want

```bash
1. 简体中文
2. English
请选择语言(Select language):
```

Then input BV number(use English as an example)

```bash
Please input BV number:
```

After wait for a while, you will see the AV number for the video you queried

### Compatible Solution for iOS & iPadOS devices(BV Number to CID)

In progress, will be available in the future.

### Compatible Solution for iOS & iPadOS devices(BV Number to AV Number)

For iOS and iPadOS users, you can use the \'Shortcut\' APP to make the same effect, click [Here](https://www.icloud.com/shortcuts/6e58cd63e3da4e888879b2f7b5f97bd7), after you imported, you can directly use that to query

### FAQ

1. Q:

   Can I run this program if I do not have python?

   A:

   This program must require python, please download python [Here](https://www.python.org/downloads/)! If you are not familiar with python, please look this website: [Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp)

2. Q:

   The program throws this error: 

   `ModuleNotFoundError: No module named 'requests'`

   How to solve this

   A:

   You might not have installed the required dependency`requests`, please follow one of the following methods to install

   Method One:

   ```bash
   pip3 install requests
   ```

   Method Two:

   ```bash
   pip3 install -r <requirement.txt address>
   ```

   Please note that \<requirement.txt address> need to change into the address in this program's `requirements.txt` address



### Find a Bug?

If you find a bug, it is welcomed to submit your Pull Request or Issues here, or please email me at [admin@vip.techzjc.com](mailto:admin@vip.techzjc.com) I will reply these ASAP!

