# Bilibili_BV2AV
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

[中文版](/README.md)

### Disclaimer

**This project is only for study purpose, DO NOT use this project to do any illegal behavior! This project is not responsible for any legal risks caused by its own misuse of this project!**

### TL;DR

Bilibili(a famous video website in China) Converter for BV number to AV number. User only need to input the video's BV number to get that video's AV number.

### Usage

1. With Parameters

Input following line in your terminal(Linux & macOS) or Command Prompt(Windows)

```bash
python main.py <lang> <BV number>
```

Change the \<lang\> into the language you want to, you need to input the number for the language(1- `Chinese Simplified` 2- `English`)

Change \<BV number\> into the BV number of the video

Press enter, you will get the AV number of that video

2. Without Parameters(Or Input Wrong Parameters)

Input following line in your terminal(Linux & macOS) or Command Prompt(Windows)

```bash
python main.py
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

### Compatible Solution for iOS & iPadOS devices

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

