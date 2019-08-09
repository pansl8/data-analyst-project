from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def cm_plot(yt, yp):
    cm = confusion_matrix(yt, yp)
    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()
    for x in range(len(cm)):
        for yt in range(len(cm)):
            plt.annotate(cm[x, yt], xy=[x, yt], horizontalalignment='center',
                         verticalalignment='center')
    plt.xlabel('Preticted label')
    plt.ylabel('True label')
    return plt


if __name__ == '__main__':
    yt = [1, 1, 0, 0, 0, 0, 1]
    yp = [1, 1, 0, 0, 0, 1, 1]
    cm_plot(yt, yp).show()
