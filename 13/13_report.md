---
attachments: [Clipboard_2022-07-12-12-21-59.png]
tags: [Python応用]
title: 13_report.md
created: '2022-07-12T03:05:26.949Z'
modified: '2022-07-12T03:46:20.747Z'
---

# 13_report.md
## 1.相関関係の強い教科名を答えてください
- 国語と英語
- 数学と理科

## 2.subplots()を使用してグラフを作成する手順

1. FigureとAxesの生成

```python
fig, ax = plt.subplots(5,5)
```
上記のコードは5*5個のサブプロットを生成するコードである
Figureは描画領域全体
Axesは個別の座標軸を扱う

![](@attachment/Clipboard_2022-07-12-12-21-59.png)
> https://www.yutaka-note.com/entry/matplotlib_subplots#%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%83%83%E3%83%88%E3%82%92%E4%B8%80%E3%81%A4%E7%94%9F%E6%88%90fig-ax--pltsubplots

2. ラベルの設定

```python
ax[0,0].set_xlabel("X軸", fontname="MS Gothic",fontsize="5")
ax[0,0].set_ylabel("Y軸", fontname="MS Gothic",fontsize="5")
```
上記のコードは左上のサブプロットについて、x軸とy軸のラベルを設定するコードである
- subplotsは`ax[0,0]`のように2次元配列の形で指定できる
- ラベル名に日本語を使用する場合はフォントを指定しないと文字化けを起こす
- `fontsize`で文字の大きさを変更できる

3. グラフの設定
```python
ax[0,0].grid(True)
ax[0,0].plot(x,y)
```
- `grid(True)`を指定することでグリッドを表示
- 描画するグラフはaxに直接指定する

