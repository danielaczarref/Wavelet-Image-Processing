[filename, pathname] = uigetfile('*.*', 'Selecione uma imagem');

filewithpath=strcat(pathname, filename);

img = imread(filewithpath);
i = rgb2gray(img);

imgn = imnoise(i, 'gaussian', 0, 0.0005); 

dwtmode('per'); 

[thr, sorh, keepapp] = ddencmp('den', 'wv', imgn);

imgden = wdencmp('gbl', double(imgn), 'sym4', 2, thr, sorh, keepapp);

subplot(131), imshow(img), title('Imagem original');
subplot(132), imshow(imgn), title('Imagem com ruído');
subplot(133), imshow(uint8(imgden), []), title('Imagem sem ruído');
