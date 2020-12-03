# Detecting Lane Lines in Python with OpenCV
As follow is a [lane detection tool](), the first project of the [Self Driving Car Nano Degree](https://www.udacity.com/drive) program from Udacity.
The goal of this project is to detect lane lines in images and video footages taken from an overhead camera on the car while driving.

[//]: # (Image References)
[whole pipeline]: ./writeup/pipeline.png
[gray]: ./writeup/grayscale.jpg 
[region of interest]: ./writeup/edges_roi.jpg 
[roi]: ./writeup/roi.png
[blurred]: ./writeup/blurred.jpg
[canny]: ./writeup/edges.jpg
[all_lines]: ./writeup/lines.jpg
[lines]: ./writeup/lines_extrapolate.jpg
[final]: ./writeup/result.jpg

The result of this project is represented as below:

![Compare](./writeup/compare.gif)

In this post, the logic behind the pipeline is illustrated by steps.

### Generating Candidate Lines and Excluding False-detections.
The pipeline has two major phases: the first is prepping for and detecting potential lines in the image/video,
and the second is heuristically removing lines that don't seem like sensible candidates to represent lanes.

![whole pipeline]

* [Generate Candidate Lines](#generate-candidate-lines)
  * [Convert Image to Grayscale](#convert-image-to-grayscale)
  * [Apply Gaussian Blur](#apply-gaussian-blut)
  * [Apply the Canny Transform](#canny-transform)
  * [Choose a Region of Interest](#choose-a-region-of-interest)
  * [Detect Lines by Converting Image to Hough Space](#detect-lines)
* [Heuristically Process Lines](#heuristically-process-lines)

### Generate Candidate Lines

#### 1. Convert Image to Grayscale
In order to detect the brightness intensity contrast, the image should be converted into gray scales. 

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


![Look at all those gray scales][gray]


#### 2. Apply Gaussian Blur
By doing this, the noise in the image will be reduced. The kernel size for Gaussian smoothing should be any odd number. A larger kernel size implies averaging, or smoothing, over a larger area. Here the kernel size has been set to 5.

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
![Just a little blur][blurred]

#### 3. Canny Transform
The algorithm will first detect strong edge (strong gradient) pixels above the high_threshold, and reject pixels below the low_threshold. Next, pixels with values between the low_threshold and high_threshold will be included as long as they are connected to strong edges. The output edges is a binary image with white pixels tracing out the detected edges and black everywhere else.

After Canny Transform, the blurred image has been converted into outlines.

    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

![After we apply the canny transform][canny]


#### 4. Choose a Region of Interest
Since the front facing camera that took the image is mounted in a fixed position on the car, such that the lane lines will always appear in the same general region of the image. We'll take advantage of this by adding a criterion to only consider pixels in the region where we expect to find the lane lines.

First, we specify a trapezoid from the two bottom corners to the two centers of the image by assign four vertices as follows.

    roi_vertices = np.array([(x * image.shape[1],y * image.shape[0]) for (x,y) in \
        [[0.0,1], [0.45, 0.6], [0.55, 0.6], [1, 1]]], np.int32)

![This is all we're interested in][roi]

Masking the canny image for a certain region looks like this:

    mask = np.zeros_like(edges)   
    if len(edges.shape) > 2:
        channel_count = edges.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    cv2.fillPoly(mask, [roi_vertices], ignore_mask_color)
    edges_roi = cv2.bitwise_and(edges, mask)


![This is all we're interested in][region of interest]
#### 5. Detect Lines
We used the Hough Transform to find lines from canny edges:
    
    rho = 1
    theta = 1 * np.pi/180
    threshold = 5
    min_line_len = 2
    max_line_gap = 20

    lines = cv2.HoughLinesP(edges_roi, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)

    line_img = np.zeros((edges_roi.shape[0], edges_roi.shape[1], 3), dtype=np.uint8)

    for line in lines:
        cv2.line(line_img, (line.x1, line.y1), (line.x2, line.y2), color=[255, 0, 0], thickness=5)

![All the lines][all_lines]

#### Heuristically Process Lines (`reduce_to_lanes`)
So far the candidate lines from the image have been detected as below, however not all of them should be considered as the lane lines. 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by:
  * Separate line segments by their slope to decide which segments are part of the left line vs. the right line.


        def line_angle_checked(img, x1, y1, x2, y2):
            # check the line slope is in the range of 25-40 degree
            min_angle = 25
            max_angle = 40

            x_mid = np.uint32(img.shape[1] * 0.5)

            min_angle_tan = np.tan(min_angle*np.pi/180)
            max_angle_tan = np.tan(max_angle*np.pi/180)
            slope = (y2-y1)/(x2-x1)

            if x1 >= x_mid and x2 >= x_mid:
                if slope > min_angle_tan and slope < max_angle_tan: 
                    return True
            else:
                if slope < -min_angle_tan and slope > -max_angle_tan:
                    return True

  * Average the position of each of the lines
  * Extrapolate to the top and bottom of the lane.

        if x1 >= x_mid and x2 >= x_mid:
            W = np.linalg.norm(np.array((x2,y2))-np.array((x1,y1)))
            fitW = np.polyfit((x1,x2), (y1,y2), 1) * W
            rA,rB = (rA,rB) + fitW
            rW = rW + W
            rX_max = min(rX_max,x1,x2)
        else:
            W = np.linalg.norm(np.array((x2,y2))-np.array((x1,y1)))
            fitW = np.polyfit((x1,x2), (y1,y2), 1) * W
            lA,lB = (lA,lB) + fitW
            lW = lW + W
            lX_max = max(lX_max, x1, x2)

        if rW != 0 and lW != 0:
            rA,rB = (rA,rB) / rW
            lA,lB = (lA,lB) / lW

            # left line left vertice
            l_x1, l_y1 = (0, int(lB))
            # left line right vertice
            l_x2, l_y2 = (int(lX_max), int(lX_max*lA + lB))

            # right line left vertice
            r_x1, r_y1 = (int(rX_max), int(rX_max*rA + rB))
            # right line right vertice
            r_x2, r_y2 = (int(full_x), int(full_x*rA + rB))
            
            cv2.line(img, (l_x1, l_y1), (l_x2,l_y2), color, thickness)
            cv2.line(img, (r_x1, r_y1), (r_x2,r_y2), color, thickness)
![Final Result Lines][lines]

Now we can make an image to represent our lines and glue it to our copy of the original image:


    result = cv2.addWeighted(image, α, lines_extrapolate, β, λ)


![final][final]

#### Shortcomings

Potential shortcomings would be what would happen when
* The lane lines on the road are more than short
* Overexposed image 
* The car has drifted out of the lane lines


#### Possible Improvements

* Try curve detection with polynomial fit
* Improve parameter tuning for region of interest regarding situation when the car has drifted out of the lane lines.
