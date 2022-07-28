import matplotlib.pyplot as plt
import numpy
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
from PIL import Image, ImageEnhance, ImageOps


X, y = datasets.load_digits(return_X_y=True)
# 重すぎて無理
# X, y = datasets.fetch_openml("mnist_784")
clf = LogisticRegression(random_state=0, solver="liblinear", multi_class="auto")
clf.fit(X, y)

X0 = X[0]
X0_square = X0.reshape(8, 8)
im = Image.open("IMG_E3159.JPG")
_, ax = pyplot.subplots()
# mydigit.jpgをEnhanceすることを宣言
enhancer = ImageEnhance.Brightness(im)
im_enhanced = enhancer.enhance(2.0)
# Gray化
im_gray = im_enhanced.convert(mode="L")
ax.imshow(im_gray, "gray")
plt.show()
# Resizeして縮小
im_8x8 = im_gray.resize((8, 8))
# 色の反転をする
im_invert = ImageOps.invert(im_8x8)
# ２次元の配列に変換
X_im2d = numpy.asarray(im_invert)
# １次元の配列に変換
X_im1d = X_im2d.reshape(-1)
X_multiplied = X_im1d * (8/255)
print(X_im2d)
# ここで画像判定する
print(clf.predict([X_multiplied])[0])

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
