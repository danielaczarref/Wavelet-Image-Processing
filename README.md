# Wavelet Transform

Wavelets are localized wave functions that are confined in finite domains and used to represent data or a function. Instead of infinitely oscillating, they drop to zero. The Wavelet Transform decomposes a function into a set of wavelets.

Two main aplications for Discrete Wavelet Transform are image denoise and image compression (since this is a work for Image Processing subject, but Wavelet Transform can also be used for 1D examples).

- Results for image denoise with MATLAB: orginal image vs noisy image vs denoised image


![alt text](https://github.com/danielaczarref/Wavelet-Image-Processing/blob/master/result1.png?raw=true)


To do so, I've added 0.0005 of Gaussian white noise.

1. `ddencmp` = MATLAB function used to find default values for denoising by using the universal threshold from donoh method;
2. `wdencmp` = MATLAB function used to denoise 1D and 2D

For this example, I've used sym4 (Wavelet Symlet-4), a single global threshold and 2 levels of decomposition.


- Results for image compression with Python

a) Original image:


![alt text](https://github.com/danielaczarref/Wavelet-Image-Processing/blob/master/tos.jpg?raw=true)


b) Results with the first 10% and 5% bigger wavelet coefficients:


![alt text](https://github.com/danielaczarref/Wavelet-Image-Processing/blob/master/result2.png?raw=true)


c) Results with the first 1% and 0.5% bigger wavelet coefficients:


![alt text](https://github.com/danielaczarref/Wavelet-Image-Processing/blob/master/result3.png?raw=true)



To do so, I've used 4 layers of decomposition in order to achieve better compression results.

The Wavelet used for image compression was Daubechies-1, recommended for better refinement.


- Main file results for analysis of image compression with Python:


![alt text](https://github.com/danielaczarref/Wavelet-Image-Processing/blob/master/result4.png?raw=true)

