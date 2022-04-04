# Computer Vision Course Tasks
In this Repository we present a variety of Image Processing Techniques implemented from scratch using Python with help of some helpful packages.

## Team members
| Name  | Section| BN |
| ------------- | ------------- |------------- |
|Marwa Abdel Aal| 02| 23|
|Nada Ezzat |02 |38  |
|Noura Mahmoud |02 |39|
|Youssef Mohamed |02 |50|
|Yousof Mahmoud |02 |51|  

#Task 1
## 1.1 Add additive noise to the image
### 1.1.1 Uniform Noise  &#x2611;
![Uniform Noise](/images/Figure_1.png)
### 1.1.2 Gaussian Noise   &#x2611;
![Gaussian Noise](/images/Figure_2.png)
### 1.1.3 Salt and Pepper Noise  &#x2611;
![Salt and Pepper Noise](/images/Figure_3.png)

## 1.2 Filter the noisy image using the following low pass filters
#### PS: openCV is only used for comparing output 
#### average & Gaussian images are normalized to be dispalyed in the desired range (0:255)
### 1.2.1 Median Filtering output &#x2611;
![](/images/median.png)
### 1.2.2 Average Filtering output &#x2611;
![](/images/Average_with_openCV.png)
### 1.2.3Gaussian Filtering output &#x2611;
![](/images/Gaussian_Filtering.png)


## 1.3 Detect edges in the image using the following masks  
### Original photo
![](/images/apple_gray.png)
### 1.3.1 Sobel  &#x2611;
####  Sobel X
![](/images/apple_sobel_x.png)
####  Sobel Y
![](/images/apple_sobel_y.png)
####  Sobel XY
![](/images/apple_sobel_xy.png)
### 1.3.2 Roberts   &#x2611;
![](/images/robert_img.jpg)
### 1.3.3 Prewitt   &#x2611;
![](/images/prewitt_img.jpg)
### 1.3.4 Canny edge detectors.  &#x2611;
####  with Lena photo
![](/images/canny_lena.jpg)
####  with high threshold 
![](/images/canny_high_threshold.jpg)


## 1.4.1 Draw histogram &#x2611; 
![Histogram](/images/Histogram.jpeg)
## 1.4.2 Distribution curve &#x2611;
![Distribution curve](/images/Curve.jpeg)

## 1.5 Equalize the image &#x2611;
<!-- ![Equalization](/images/Equalization.jpeg) -->
<!-- ![Equalization](/images/equalization.png) -->
![Equalization](/images/equalized_image.png)

## 1.6 Normalize the image &#x2611;
![normalized_image](/images/normalized.jpeg)

## 1.7 Local and global thresholding
![original](/images/original.png)
### Local thresholding  &#x2611;
![Local thresholding](/images/local.png)
### Global thresholding   &#x2611;
![Global thresholding](/images/global.png)

## 1.8 Transformation from color image to gray scale image and plot of R, G and B histograms with its distribution curve (cumulative curve) &#x2611;

### 1.8.1- Transformation from color image to gray scale image
![rgb2gray](/images/point8/rgb2gray.png)

### 1.8.2- Color image Histogram
![Color_Histogram](/images/point8/Color_Histogram.jpg)

### 1.8.2.1- Red Histogram
![Red_Histogram](/images/point8/Red_Histogram.jpg)

### 1.8.2.2- Green Histogram
![Green_Histogram](/images/point8/Green_Histogram.jpg)

### 1.8.2.3- Blue Histogram
![Blue_Histogram](/images/point8/Blue_Histogram.jpg)

### 1.8.3- RGB Cumulative Curve
![Cumulative Curve](/images/point8/cumulative_curve.jpg)

### 1.8.3.1- Red Cumulative Curve
![Red Cumulative Curve](/images/point8/red_cumulative_curve.jpg)

### 1.8.3.2- Green Cumulative Curve
![Green Cumulative Curve](/images/point8/green_cumulative_curve.jpg)

### 1.8.3.3- Blue Cumulative Curve
![Blue_Cumulative Curve](/images/point8/blue_cumulative_curve.jpg)


## 1.9- Filter in frequancy domain 
#### Before applying filtering images are converted to frequency domain using FFT and then Shifted to make Low frequency component in the center 
![](/images/FFT_Shifting.png)
#### PS Low & High pass filters  are applied with customized filter size to control images' bluring and Sharpening
### 1- Ideal Low Pass Filter  &#x2611;
![](/images/lowpass_output1.png)
### 2- Ideal High Pass Filter  &#x2611;
![](/images/highpass_output.png)


## 1.10 Hybrid Images  &#x2611;
![](/images/h1.png)
![](/images/h2.png)
### the result  still in progress
![](/images/hybrid_image.png)

# Task 2
## 2.1 Hough Transform
### 2.1.1 Line detection and drawing  &#x2611;
![png](/Hough/output_9_1.png)
![png](/Hough/output_10_1.png)

#### another example 
![png](/Hough/output_11_1.png)
![png](/Hough/output_12_1.png)

### 2.1.2 Circle detection and drawing  &#x2611;
![png](/Hough/output_15_1.png)
![png](/Hough/output_16_1.png)
