# knsktzk-color_identification
教師あり学習（分類）を用いて、OT-2 でウェルプレートに分注した色水の吸光度データから色水の色を判別するモデルを作成

## 使用したもの
- [byonoy Absorbance 96](https://www.funakoshi.co.jp/contents/68832)
- [Opentrons 2](https://opentrons.com/ot-2/) 
  - [300 µl チップラック](https://labware.opentrons.com/opentrons_96_tiprack_300ul?_gl=1*1tlylb8*_ga*MjMxODQzNTc2LjE2NDQ3NjA2NDk.*_ga_GNSMNLW4RY*MTY0ODM1ODI0NS41LjEuMTY0ODM1ODM0Ni4w&_ga=2.5246907.948475537.1648358246-231843576.1644760649)
  - [96-wellマイクロプレート](https://labware.opentrons.com/corning_96_wellplate_360ul_flat?_gl=1*8i3lf1*_ga*MjMxODQzNTc2LjE2NDQ3NjA2NDk.*_ga_GNSMNLW4RY*MTY0ODM1ODI0NS41LjEuMTY0ODM1ODQxOC4w&_ga=2.77073181.948475537.1648358246-231843576.1644760649)
  - [6-wellマイクロプレート](https://labware.opentrons.com/corning_6_wellplate_16.8ml_flat?_gl=1*8i3lf1*_ga*MjMxODQzNTc2LjE2NDQ3NjA2NDk.*_ga_GNSMNLW4RY*MTY0ODM1ODI0NS41LjEuMTY0ODM1ODQxOC4w&_ga=2.77073181.948475537.1648358246-231843576.1644760649) 
- 色水
  - 赤（シクラメンピンク）
  - 緑（リーフグリーン）
  - 青（アクアブルー）
  - いずれの色水もインクを100倍希釈したもの

## 色の種類
- 黒
  - color_name：`black`
  - R：G：B＝１：１：１（40μL：40μL：40μL）
  - 作成スクリプト：`./ot2/three_colors.py`
- 緑
  - color_name：`green`
  - R：G：B＝０：１：０（0μL：120μL：0μL）
  - 作成スクリプト：`./ot2/a_color.py`
- 青
　- color_name：`blue`
  - R：G：B＝０：０：１（0μL：0μL：120μL）
  - 作成スクリプト：`./ot2/a_color.py`
- 赤
  - color_name：`red`
  - R：G：B＝１：０：０（120μL：0μL：0μL）
  - 作成スクリプト：`./ot2/a_color.py`
- 青緑
  - color_name：`blueen`
  - R：G：B＝０：１：１（0μL：60μL：60μL）
  - 作成スクリプト：`./ot2/two_colors.py`
- 紫
  - color_name：`purple`
  - R：G：B＝１：０：１（60μL：0μL：60μL）
  - 作成スクリプト：`./ot2/two_colors.py`

## データについて
- Absorbance で各色水の吸光度を測定
- 各色水に対して 96-wellマイクロプレートを1枚使用（つまり1色あたり96個のサンプルを獲得）
- 3種類の波長を測定
  - 405 nm `./test_data/{color_name}_405.csv`
  - 450 nm `./test_data/{color_name}_450.csv`
  - 620 nm `./test_data/{color_name}_620.csv`
 - 各色水の波長データを統合＆色のラベル（目的変数）を加えたデータセット `./test_dataset.csv`
  - 加工に使用したスクリプト `./data_shape.py`
  
  
  
