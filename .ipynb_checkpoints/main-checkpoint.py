from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import os
import pywt

plt.rcParams['figure.figsize'] = [16, 16]
plt.rcParams.update({ 'font.size': 18 })

A = imread( 'belanna.jpg')
B = np.mean(A, -1)

n = 2
w = 'db1'
coeficientes = pywt.wavedec2(B, wavelet=w, level=n)

coeficientes[0] /= np.abs(coeficientes[0]).max()
for detail_level in range(n):
  coeficientes[detail_level + 1] = [d/np.abs(d).max() for d in coeficientes[detail_level + 1]]

arr, coeff_slices = pywt.coeffs_to_array(coeficientes)

plt.imshow(arr, cmap='gray',vmin=-0.25,vmax=0.75)
plt.show()
