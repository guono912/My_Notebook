% 神奇的函数系列，可以用于将手拍图像处理的和扫描一样的骚操作、
%% demo
I = imread('printedtext.png');
figure
imshow(I)
title('Original Image')         %以上输入原始图像并展示（实际操作只需前两句）
BW = imbinarize(I,'adaptive','ForegroundPolarity','dark','Sensitivity',0.4);   %暂时没搞懂的最核心的一句，先放着
figure
imshow(BW)
title('Binary Version of Image')     %嗯结果，被阴影挡的看不起的地方也可以扫的非常清楚哈哈哈哈
