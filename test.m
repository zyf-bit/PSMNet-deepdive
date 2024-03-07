imgPath = 'F:\PSMNet\result_gray\';
imgPath2 = 'F:\PSMNet\result_rgb\';
imgDir  = dir([imgPath '*.png']);
for i = 1:length(imgDir) 
    D_test = disp_read([imgPath imgDir(i).name]);
    D_test_color=disp_to_color(D_test,192);
    imwrite (D_test_color, [imgPath2 imgDir(i).name])
end