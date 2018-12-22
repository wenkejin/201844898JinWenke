from nltk.tokenize import word_tokenize
from sklearn import metrics
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.mixture import GaussianMixture
import re
import warnings


text = []
labels = []
cluster = []


def dataProcess():
    global text

    with open("./Tweets.txt", 'r') as data:
        data = data.readlines()
        for str in data:
            str = str.split("\"")
            text.append(str[3])
            labels.append(re.findall("\d+", str[6])[0])

    tfidfvectorizer = TfidfVectorizer(tokenizer = word_tokenize, stop_words = 'english')
    text = tfidfvectorizer.fit_transform(text)


def K_Means():#1
    global cluster
    global labels
    cluster = KMeans(n_clusters = 110).fit_predict(text)
    print("K-Means NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def Affinity_propagation():#2
    global cluster
    global labels
    clu = AffinityPropagation().fit(text)
    cluster = clu.labels_
    print("Affinity propagation NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def Mean_shift():#3
    global cluster
    global labels
    cluster = MeanShift().fit_predict(text.toarray())
    print("Mean-shift NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def Spectral_clustering():#4
    global cluster
    global labels
    cluster = SpectralClustering(n_clusters = 110).fit_predict(text)
    print("Spectral clustering NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def WardHierarchicalClustering():#5
    global cluster
    global labels
    cluster = AgglomerativeClustering(n_clusters = 110).fit_predict(text.toarray())
    print("Ward hierarchical clustering NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def Agglomerative_clustering():#6
    global cluster
    global labels
    cluster = AgglomerativeClustering(n_clusters = 110,linkage = "average").fit_predict(text.toarray())
    print("Agglomerative clustering NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def _DBSCAN():#7
    global cluster
    global labels
    cluster = DBSCAN(eps = 1.13,min_samples = 6).fit_predict(text)
    print("DBSCAN NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


def GaussianMixtures():#8
    global cluster
    global labels
    cluster = GaussianMixture(n_clusters = 110).fit_predict(text)
    print("GaussianMixtures NMI:%s" % (metrics.normalized_mutual_info_score(labels, cluster)))


if __name__=='__main__':
    # print("enter")

    warnings.filterwarnings("ignore")

    dataProcess()

    K_Means()
    Affinity_propagation()
    Mean_shift()
    Spectral_clustering()
    WardHierarchicalClustering()
    Agglomerative_clustering()
    _DBSCAN()
    GaussianMixtures()

    # print("end")