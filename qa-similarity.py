import numpy
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# 形態素解析 Tokenizer
def tokenizer(text):
    t = MeCab.Tagger()
    return t.parse(text).split()

# 文書ベクトル化
def vector_array(documents):
    docs = numpy.array(documents)
    vectorizer = TfidfVectorizer(analyzer=tokenizer,binary=True,use_idf=False)
    vecs = vectorizer.fit_transform(docs)
    return vecs.toarray()

# JSON ファイルからデータを読み込み
def data_load(file_name):
    with open(file_name) as file:
        data = json.load(file)
    docs = []
    for faq in data:
        docs.append(faq["質問"] + faq["回答"])
    return docs

if __name__ == '__main__':
    # データ読み込み
    qa_array = data_load("data/faq/faq.json")
    # 類似度計算
    cos_array = cosine_similarity(vector_array(qa_array), vector_array(qa_array))
    # 上位 3 つを表示
    i = 0
    for qa in qa_array:
        print("Q[%d] %s" % (i, qa))
        cos = cos_array[i]
        max4_indices = numpy.argpartition(-cos, 4)[:4]
        y = cos[max4_indices]
        indices = numpy.argsort(-y)
        max4_indices_sorted = max4_indices[indices]
        for idx in max4_indices_sorted:
            if idx != i:
                print("%f %s" % (cos[idx], qa_array[idx]))
        print("---")
        i += 1