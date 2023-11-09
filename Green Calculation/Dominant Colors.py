import cv2, numpy as np
from sklearn.cluster import KMeans

def visualize_Dominant_colors(cluster, C_centroids):
    C_labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (C_hist, _) = np.histogram(cluster.labels_, bins = C_labels)
    C_hist = C_hist.astype("float")
    C_hist /= C_hist.sum()

    rect_color = np.zeros((50, 300, 3), dtype=np.uint8)
    img_colors = sorted([(percent, color) for (percent, color) in zip(C_hist, C_centroids)])
    start = 0
    for (percent, color) in img_colors:
        print(color, "{:0.2f}%".format(percent * 100))
        end = start + (percent * 300)
        cv2.rectangle(rect_color, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
    return rect_color
s = "Excess CuSO4 "
# Load image
for i in range(5):

    src_image = cv2.imread(s + "" + str(i+1) + ".jpeg")
    src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
    reshape_img = src_image.reshape((src_image.shape[0] * src_image.shape[1], 3))

    # Display dominant colors Present in the image
    KM_cluster = KMeans(n_clusters=5).fit(reshape_img)
    visualize_color = visualize_Dominant_colors(KM_cluster, KM_cluster.cluster_centers_)
    visualize_color = cv2.cvtColor(visualize_color, cv2.COLOR_RGB2BGR)
    cv2.imshow('visualize_Color', visualize_color)
    cv2.waitKey()
    