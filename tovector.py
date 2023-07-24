#文本向量化
import pandas as pd
import sentence_transformers
df = pd.read_csv("ready.txt", sep="#",header=None, names=["sentence"])
from sentence_transformers import SentenceTransformer,util
import scipy

model = SentenceTransformer('D:\\PCProjects\\model\\m3e-base')

# 保存预训练模型的文件夹
#save_path = "../model"
#model.save(save_path)

sentences = df['sentence'].tolist()
sentence_embeddings = model.encode(sentences)

print(sentence_embeddings.shape)  # (100,768)

#for sentence,embedding in zip(sentences,sentence_embeddings):
#    print("Sentence:",sentence)
#    print("Embedding:",embedding)
#    print("")

sentence1='玩家喜欢'
sentence1s = [sentence1]
embedding1s = model.encode(sentence1s)
number_top_matches = 1
for query,query_embedding  in zip(sentence1s,embedding1s):
    #consine_score1 = util.pytorch_cos_sim(embedding1,embedding)[0]
    distances = scipy.spatial.distance.cdist([query_embedding],sentence_embeddings,"cosine")[0]
    results = zip(range(len(distances)),distances)
    results = sorted(results,key=lambda x:x[1])
    print("Query",query)
    print("\nTop {} most similar sentences in corpus:".format(number_top_matches))

    '''
    distance表示两个句子的余弦距离，1-distance可以理解为两个句子的余弦分数，分数越大表示两个句子的语义越相近
    '''
    for idx, distance in results[0:number_top_matches]:
        print(sentences[idx].strip(), "(Cosine Score: %.4f)" % (1 - distance))
