# vaccinecert-qa-similarity-test

## Install MeCab & dictionary (for Mac)

```sh:
brew install mecab
brew install mecab-ipadic
```

## Install MeCab & dictionary (for Ubuntu)

```sh:
sudo apt install mecab
sudo apt install libmecab-dev
sudo apt install mecab-ipadic-utf8
```

## Install Python library

```sh:
pip install numpy mecab-python3 sklearn
```

## Usage

```sh:
python3 qa-similarity.py data/faq/faq.json 3 > data/faq/faq-sim3.json
```

- `data/faq/faq.json`
  - input file
- `3`
  - count of similar questions
- `data/faq/faq-sim3.json`
  - output file

## Reference

- https://analysis-navi.com/?p=688
- https://qiita.com/Haruka-Ogawa/items/c2116f0eb5c859955d63
- https://naoyashiga.hatenablog.com/entry/2017/04/13/224339