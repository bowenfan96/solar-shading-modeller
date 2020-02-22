<!----- Conversion time: 34.718 seconds.


Using this Markdown file:

1. Cut and paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β18
* Sat Feb 22 2020 11:53:11 GMT-0800 (PST)
* Source doc: https://docs.google.com/open?id=1Qvrvg0cxA-faa5MeNDqeGnv68lyaTLtJLMmGh0x93zU
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server.

WARNING:
You have 8 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 35.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>
<a href="#gdcalert19">alert19</a>
<a href="#gdcalert20">alert20</a>
<a href="#gdcalert21">alert21</a>
<a href="#gdcalert22">alert22</a>
<a href="#gdcalert23">alert23</a>
<a href="#gdcalert24">alert24</a>
<a href="#gdcalert25">alert25</a>
<a href="#gdcalert26">alert26</a>
<a href="#gdcalert27">alert27</a>
<a href="#gdcalert28">alert28</a>
<a href="#gdcalert29">alert29</a>
<a href="#gdcalert30">alert30</a>
<a href="#gdcalert31">alert31</a>
<a href="#gdcalert32">alert32</a>
<a href="#gdcalert33">alert33</a>
<a href="#gdcalert34">alert34</a>
<a href="#gdcalert35">alert35</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# Smart Solar Optimizer


## A step-by-step user guide


# Introduction

The function of this tool is to calculate the impact of shading on the solar energy received at a location. It requires a 360° panorama (taken from Google StreetView) or a hemispherical fisheye image as input. It outputs a report which includes the percentage of energy lost to shading at the location analyzed, and the impact of shading for each month in the year.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar0.png "image_tooltip")



# Download and run



1. The .zip file (around 280 MB) containing the program can be downloaded from:

[https://github.com/bowenfan96/solar-shading-modeller/releases](https://github.com/bowenfan96/solar-shading-modeller/releases)

This page will be updated if there is a newer version of the program.



2. Unzip the file and click “ssm_v0.5.exe - Shortcut” to launch the program.


## Interface



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar1.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar1.png "image_tooltip")


When launched, a command window will pop up together with the program window - don’t close the command window or the program will also exit. The command window serves as a progress monitor during the calculation.


# Obtaining a 360° panorama or a hemispherical fisheye


## 360° panorama

The most convenient way to analyze the solar potential at a location is with a 360° panorama from Google Maps StreetView. To do this, the location of interest has to be on a road that’s covered by StreetView.



3. Download the tool that stitches together StreetView imagery to give a 360° panorama from this link: [https://svd360.istreetview.com/](https://svd360.istreetview.com/)  \
Credits to Thomas Orlita, who wrote this panorama downloader software.
4. Go to [https://www.google.com/maps](https://www.google.com/maps) and enter StreetView for a location of interest. Navigate as close as possible to a planned location for the solar panel.

As an example, I have navigated to an existing panel at 415 Bedok North Ave 2. With this method, the solar analysis will actually be giving results for the point on the road from which the StreetView was taken. This may be a couple of meters away from the real panel position. As such, it’s important to get as close as possible.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar2.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar2.png "image_tooltip")




5. Copy the URL from the address bar. Paste this URL into the solar program and click “Get Pano ID”. Copy the Pano ID generated:



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar3.png "image_tooltip")




6. Install and open the  “Street View Download 360” tool from Step 3. Specify a save folder and the file name. Paste the Pano ID into the program as such:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar4.png "image_tooltip")


A resolution of 1664×832 is sufficient. Higher resolutions are okay but the image tracing will take longer.



7. Click “Download Panorama” and open the downloaded .png or .jpg in Paint 3D (standard software on Windows 10), like this: \
_Should be able to just right click on the image file and select “Edit with Paint 3D”_



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar5.png "image_tooltip")


The solar analysis tool assumes that North is aligned to the leftmost pixel on the image. Hence it is necessary to edit the panorama such as the North is on the left.



8. Go back to Google Maps StreetView page. Click on the compass icon in the bottom-right corner so that the center of the picture aligns North (the red arrow should be pointing up).  \
_It helps to zoom in first (scroll up), then align the compass - it’s easier to find an object that’s aligned to the North as they are bigger (see Step 9)._



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar6.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar6.png "image_tooltip")




<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar7.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar7.png "image_tooltip")




9. Identify an object on the image that is directly along the North direction. This is any landmark or feature in the center of the view - the centerline is roughly in the middle of the 2nd ‘o’ of the Google logo at the bottom.



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar8.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar8.png "image_tooltip")


Here, the centerline, which is the North, is slightly to the left of the lorry.



10. Now we’ll have to edit the panorama image in Paint 3D and shift this lorry to the left.
    1. Click “Select” from the top left corner. Draw a box to select the portion that contains the 0° North line. Try to align it accurately.



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar9.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar9.png "image_tooltip")


To illustrate, this is the portion selected. Note that the lorry is on the the extreme left:



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar10.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar10.png "image_tooltip")




    2. Cut the selection (Ctrl-X):



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar11.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar11.png "image_tooltip")




    3. Select the other half:



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar12.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar12.png "image_tooltip")




    4. Move this selection to the right by dragging it after it is selected. Then, paste the previous selection and drag it so that it is aligned to the left. Try not to leave a gap between the two portions:



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar13.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar13.png "image_tooltip")




    5. This is what the image should look like now, after being pieced together. The left of the image is now aligned to the geographic North (note where the lorry is).



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar14.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar14.png "image_tooltip")




    6. Crop the image into half. This is because this is a 360°×180° panorama. The lower half is actually below the panel height.



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar15.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar15.png "image_tooltip")


Click “Crop” from the top left corner. Crop the height to half of its original - the original height was 1024 px, so now it’s cropped to 512 px.



    7. Save the image (Ctrl-S). This is what you should have now:



<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar16.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar16.png "image_tooltip")



# Running the analysis



11. Go back to the solar analysis tool. Select the edited panorama in the “Select image file” row, using the “browse” button. Fill in the rest of the fields too.



<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar17.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar17.png "image_tooltip")




12. Click “Test sensitivity” to test whether the program is able to trace the obstacles accurately: \
(_The higher the value, the less sensitive the program is. This may be confusing and I intend to fix this in a future release.)_

The program will display the traced obstacles:



<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar18.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar18.png "image_tooltip")


In this case, the default value of 350 works well - the trees and the HDBs are traced quite accurately. 

However, the program may have trouble identifying the obstacles if the sky is cloudy or if the buildings are too similar to the colour of the sky. 

In this case, it will be more accurate if you manually trace the obstacles with a red line and erase the sky before feeding it into the program:

In Paint 3D, use the red marker to draw over the trees and buildings, then use the eraser tool to erase the sky (don’t erase the red marker line):



<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar19.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar19.png "image_tooltip")


You should have an image like this:



<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar20.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar20.png "image_tooltip")




13. You can test the sensitivity multiple times, until the program traces all the obstacles accurately. If you manually trace the sky with a red line and erase the sky like illustrated above, the default sensitivity value of 350 should be accurate.
14. Select a computation interval - the default value of 5 minutes means that the position of the sun is calculated and compared to the positions of the obstacles every 5 minutes.  \
_Recommended to leave this as the default. A lower value (e.g. 1 minute) will take more time to compute, but does not increase accuracy because the accuracy bottleneck is with the image tracing._



<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar21.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar21.png "image_tooltip")




15. Click “Compute” to begin calculations:



<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar22.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar22.png "image_tooltip")


_The program will say “Not Responding”, but it is actually making a lot of calculations in the background - see the console window. Don’t click the window repeatedly._

When it is done (about 1-2 minutes), the program will generate a report at the folder specified, and a window will pop up:



<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar23.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar23.png "image_tooltip")



# Solar Report


## Summary

The first page of the solar report summarizes how bad the shading is, in terms of percentage energy loss:



<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar24.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar24.png "image_tooltip")



## Skyline and sun path chart



<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar25.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar25.png "image_tooltip")


The second page shows the path of the sun (red dots) over the course of a day, together with the position of the obstacles (blue line). Recall that this is our panorama:



<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar26.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar26.png "image_tooltip")


Looking at the skyline and sun path chart, you can see that the bunch of trees on the right is blocking a lot of the afternoon and evening sun - a lot of the sun (red dots) is covered by the trees (blue line) from around 180° to 330°.

Obstacles without any red dots below them do not affect the sun, because they don’t overlap with the sun’s path. For example, the round tree on the extreme left is in the white region of the chart, and will not cause shading at any time of the day.


## Monthly and quarterly analysis

The subsequent pages show how each month will be affected by the shading. The energy received at the location is plotted for Day 15 of each month - Day 15 is selected to give an indication for the whole month.



<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar27.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar27.png "image_tooltip")


From the quarterly chart above, you can see that January (blue line) is the weakest month in this quarter. The location will only receive sunlight from around 10 am to around 1:05 pm. The peak intensity is also lower. The panel should be sized so that there’s enough power even for the weakest month.


# Clouds and rain

Referring to the report’s summary:



<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar28.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar28.png "image_tooltip")


The overall solar potential of 1580 kWh/sqm/year is taken from the EMA website. This includes losses due to rain and cloud cover. The actual irradiance value calculated also includes losses due to rain and cloud cover, but the losses are averaged over the year. Not all months are equal because there’s more rain in some months (e.g. December). Thus, dividing this value by 12 would not be indicative of the solar potential of each month.

Referring to the monthly and quarterly analysis:



<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar29.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar29.png "image_tooltip")


The instantaneous irradiance values in these graphs assume a completely clear sky - the actual irradiance will almost always be lower. However, it wouldn’t be possible to estimate the actual instantaneous irradiance, since that is subject to drifting clouds and rainfall.


# Using a hemispherical fisheye image instead

This is an example of a hemispherical lens used for solar analysis, taken from the NUS National Solar Repository:



<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar30.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar30.png "image_tooltip")


Here’s another image I found on the Internet ([https://platypod.com/blog/tower-of-light-shooting-with-a-fisheye-lens](https://platypod.com/blog/tower-of-light-shooting-with-a-fisheye-lens)), where there are more obstacles. There’s no sun since it’s taken at night, but it’s just for illustration purposes.



<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar31.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar31.png "image_tooltip")


Clip-on fisheye lenses are available for smartphones. They are a low-cost method to take images like these.

If the potential panel location is not near a road (hence not covered by StreetView), it would be necessary to go to the location and take a hemispherical fisheye photo. Point the lens vertically upwards, at the height where the panel would be. Save it like a square image like the one above.


## North alignment

Take note of where North is when you take the image. With a compass, rotate the lens until the North on the compass aligns with the vertical of the image (the red line shown above).


## Unrolling and tracing a fisheye image

Input the image into the solar analysis program like before, but select the “Hemispherical fisheye” radio button instead:



<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar32.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar32.png "image_tooltip")


The program will unroll and trace the fisheye image for obstacles, just as it did for the 360° panorama:



<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar33.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar33.png "image_tooltip")


If the obstacle tracing is unsatisfactory, you can manually trace the obstacles with a red marker and erase the sky in the middle portion like so:



<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Smart-Solar34.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Smart-Solar34.png "image_tooltip")


The rest of the steps in the analysis are the same - just remember to select the right image type.


# Contact

Please email me at [fan_b@meng.ucl.ac.uk](mailto:fan_b@meng.ucl.ac.uk) if there are errors in the program, or if you have a suggestion. Thanks! :)


<!-- Docs to Markdown version 1.0β18 -->
