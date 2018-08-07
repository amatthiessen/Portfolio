import math

def SSE_Fit(kmeans, X):
    SSE = []
    i = 0
    c = 0
    summ = 0
    cluster_group = []
    for cc in kmeans.cluster_centers_:
        for label in kmeans.labels_:
            if label == i:
                cluster_group.append(c)
            c = c+1    
        for index in cluster_group:
            summ +=(math.hypot(cc[0] - X[index][0], cc[1] - X[index][1]))**2
        SSE.append(summ)
        i += 1
        c = 0
        summ = 0
        cluster_group = []

    for element in SSE:
        summ += element
    return summ