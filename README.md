# vaccinecert-qa-similarity-test

## Install MeCab & dictionary (for Mac)

```sh:
brew install mecab
brew install mecab-ipadic
```

## Install MeCab & dictionary (for Ubuntu)

```sh:
sudo apt-get install -y mecab libmecab-dev mecab-ipadic-utf8
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -y
echo dicdir = `mecab-config --dicdir`"/mecab-ipadic-neologd" > mecabrc 
sudo cp mecabrc /usr/local/etc
```

## Install Python library

```sh:
pip install numpy mecab-python3 sklearn
```

## Usage

```sh:
python3 tool/data-creator/qa-similarity.py data/faq/faq.json 3 > data/faq/similarity.json
```

- `data/faq/faq.json`
  - input file
- `3`
  - count of similar questions
- `data/faq/faq-similarity.json`
  - output file

## Reference

- https://analysis-navi.com/?p=688
- https://qiita.com/Haruka-Ogawa/items/c2116f0eb5c859955d63
- https://naoyashiga.hatenablog.com/entry/2017/04/13/224339