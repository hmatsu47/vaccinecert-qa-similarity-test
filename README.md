# vaccinecert-qa-similarity-test

- Install MeCab & dictionary (for Mac)

```sh:
brew install mecab
brew install mecab-ipadic
```

- Install MeCab & dictionary (for Ubuntu)

```sh:
sudo apt install mecab
sudo apt install libmecab-dev
sudo apt install mecab-ipadic-utf8
```

- Install Python library

```sh:
pip install numpy mecab-python3 sklearn
```

- Usage

```sh:
python3 qa-similarity.py data/faq/faq.json > data/faq/faq-sim3.json
```

- Reference
  - https://analysis-navi.com/?p=688