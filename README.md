
<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"></head><body class="c15"><div><p class="c22"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 817.00px; height: 10.00px;"><img alt="" src="images/image2.png" style="width: 817.00px; height: 10.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="horizontal line"></span><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 817.00px; height: 10.00px;"><img alt="" src="images/image2.png" style="width: 817.00px; height: 10.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="horizontal line"></span></p><p class="c11"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 47.00px; height: 6.00px;"><img alt="" src="images/image12.png" style="width: 47.00px; height: 6.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="short line"></span></p></div><p class="c2 c21 title" id="h.dv7ifnntfcyn"><span class="c17">Solar Shading Modeller</span></p><p class="c2 c16 subtitle" id="h.dmb76m9m96l"><span class="c12">User guide</span></p><h1 class="c10 c2" id="h.ehx7q9uts426"><span class="c7">Introduction</span></h1><p class="c1"><span class="c0">The function of this tool is to calculate the impact of shading on the solar energy received at a location. It requires a 360&deg; panorama (taken from Google StreetView) or a hemispherical fisheye image as input. It outputs a report which includes the percentage of energy lost to shading at the location analyzed, and the impact of shading for each month in the year.</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 592.00px; height: 357.00px;"><img alt="" src="images/image9.png" style="width: 592.00px; height: 357.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><h1 class="c10 c2" id="h.qkdwp8skbuyn"><span class="c7">Download and run</span></h1><ol class="c4 lst-kix_wcy63pfyokw9-0 start" start="1"><li class="c1 c9"><span class="c0">The .zip file (around 280 MB) containing the program can be downloaded from:</span></li></ol><p class="c1"><span class="c14"><a class="c3" href="https://www.google.com/url?q=https://github.com/bowenfan96/solar-shading-modeller/releases&amp;sa=D&amp;ust=1582406735121000">https://github.com/bowenfan96/solar-shading-modeller/releases</a></span></p><p class="c1"><span class="c0">This page will be updated if there is a newer version of the program.</span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="2"><li class="c1 c9"><span class="c0">Unzip the file and click &ldquo;ssm_v0.5.exe - Shortcut&rdquo; to launch the program.</span></li></ol><h2 class="c1 c2" id="h.c1b5inzt7s0"><span class="c6">Interface</span></h2><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 385.33px;"><img alt="" src="images/image22.png" style="width: 602.00px; height: 385.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">When launched, a command window will pop up together with the program window - don&rsquo;t close the command window or the program will also exit. The command window serves as a progress monitor during the calculation.</span></p><h1 class="c10 c2" id="h.gv9wpnleonwv"><span class="c7">Obtaining a 360&deg; panorama or a hemispherical fisheye</span></h1><h2 class="c1 c2" id="h.ard3wsn896s4"><span class="c6">360&deg; panorama</span></h2><p class="c1"><span class="c0">The most convenient way to analyze the solar potential at a location is with a 360&deg; panorama from Google Maps StreetView. To do this, the location of interest has to be on a road that&rsquo;s covered by StreetView.</span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="3"><li class="c1 c9"><span>Download the tool that stitches together StreetView imagery to give a 360&deg; panorama from this link: </span><span class="c14"><a class="c3" href="https://www.google.com/url?q=https://svd360.istreetview.com/&amp;sa=D&amp;ust=1582406735124000">https://svd360.istreetview.com/</a></span><span class="c0">&nbsp;<br>Credits to Thomas Orlita, who wrote this panorama downloader software.</span></li><li class="c1 c9"><span>Go to </span><span class="c14"><a class="c3" href="https://www.google.com/url?q=https://www.google.com/maps&amp;sa=D&amp;ust=1582406735124000">https://www.google.com/maps</a></span><span class="c0">&nbsp;and enter StreetView for a location of interest. Navigate as close as possible to a planned location for the solar panel.</span></li></ol><p class="c1"><span class="c0">As an example, I have navigated to an existing panel at 415 Bedok North Ave 2. With this method, the solar analysis will actually be giving results for the point on the road from which the StreetView was taken. This may be a couple of meters away from the real panel position. As such, it&rsquo;s important to get as close as possible.</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image27.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="5"><li class="c1 c9"><span class="c0">Copy the URL from the address bar. Paste this URL into the solar program and click &ldquo;Get Pano ID&rdquo;. Copy the Pano ID generated:</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 592.00px; height: 357.00px;"><img alt="" src="images/image11.png" style="width: 592.00px; height: 357.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="6"><li class="c1 c9"><span class="c0">Install and open the &nbsp;&ldquo;Street View Download 360&rdquo; tool from Step 3. Specify a save folder and the file name. Paste the Pano ID into the program as such:</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 492.00px;"><img alt="" src="images/image5.png" style="width: 602.00px; height: 492.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">A resolution of 1664&times;832 is sufficient. Higher resolutions are okay but the image tracing will take longer.</span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="7"><li class="c1 c9"><span>Click &ldquo;Download Panorama&rdquo; and open the downloaded .png or .jpg in Paint 3D (standard software on Windows 10), like this:<br></span><span class="c8">Should be able to just right click on the image file and select &ldquo;Edit with Paint 3D&rdquo;</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image10.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">The solar analysis tool assumes that North is aligned to the leftmost pixel on the image. Hence it is necessary to edit the panorama such as the North is on the left.</span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="8"><li class="c1 c9"><span>Go back to Google Maps StreetView page. Click on the compass icon in the bottom-right corner so that the center of the picture aligns North (the red arrow should be pointing up). <br></span><span class="c8">It helps to zoom in first (scroll up), then align the compass - it&rsquo;s easier to find an object that&rsquo;s aligned to the North as they are bigger (see Step 9).</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image30.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image24.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="9"><li class="c1 c9"><span class="c0">Identify an object on the image that is directly along the North direction. This is any landmark or feature in the center of the view - the centerline is roughly in the middle of the 2nd &lsquo;o&rsquo; of the Google logo at the bottom.</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image34.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">Here, the centerline, which is the North, is slightly to the left of the lorry.</span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="10"><li class="c1 c9"><span class="c0">Now we&rsquo;ll have to edit the panorama image in Paint 3D and shift this lorry to the left.</span></li></ol><ol class="c4 lst-kix_wcy63pfyokw9-1 start" start="1"><li class="c1 c13"><span class="c0">Click &ldquo;Select&rdquo; from the top left corner. Draw a box to select the portion that contains the 0&deg; North line. Try to align it accurately.</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image21.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">To illustrate, this is the portion selected. Note that the lorry is on the the extreme left:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 393.50px; height: 420.95px;"><img alt="" src="images/image19.png" style="width: 393.50px; height: 420.95px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-1" start="2"><li class="c1 c13"><span class="c0">Cut the selection (Ctrl-X):</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image13.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-1" start="3"><li class="c1 c13"><span class="c0">Select the other half:</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image33.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-1" start="4"><li class="c1 c13"><span class="c0">Move this selection to the right by dragging it after it is selected. Then, paste the previous selection and drag it so that it is aligned to the left. Try not to leave a gap between the two portions:</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image32.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-1" start="5"><li class="c1 c13"><span class="c0">This is what the image should look like now, after being pieced together. The left of the image is now aligned to the geographic North (note where the lorry is).</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 301.33px;"><img alt="" src="images/image3.png" style="width: 602.00px; height: 301.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-1" start="6"><li class="c1 c13"><span class="c0">Crop the image into half. This is because this is a 360&deg;&times;180&deg; panorama. The lower half is actually below the panel height.</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image25.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">Click &ldquo;Crop&rdquo; from the top left corner. Crop the height to half of its original - the original height was 1024 px, so now it&rsquo;s cropped to 512 px.</span></p><ol class="c4 lst-kix_wcy63pfyokw9-1" start="7"><li class="c1 c13"><span class="c0">Save the image (Ctrl-S). This is what you should have now:</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 150.67px;"><img alt="" src="images/image28.png" style="width: 602.00px; height: 150.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><h1 class="c10 c2" id="h.fnkcz8w5m6kk"><span class="c7">Running the analysis</span></h1><ol class="c4 lst-kix_wcy63pfyokw9-0" start="11"><li class="c1 c9"><span class="c0">Go back to the solar analysis tool. Select the edited panorama in the &ldquo;Select image file&rdquo; row, using the &ldquo;browse&rdquo; button. Fill in the rest of the fields too.</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 592.00px; height: 357.00px;"><img alt="" src="images/image16.png" style="width: 592.00px; height: 357.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="12"><li class="c1 c9"><span>Click &ldquo;Test sensitivity&rdquo; to test whether the program is able to trace the obstacles accurately:<br>(</span><span class="c8">The higher the value, the less sensitive the program is. This may be confusing and I intend to fix this in a future release.)</span></li></ol><p class="c1"><span class="c0">The program will display the traced obstacles:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 571.50px; height: 142.66px;"><img alt="" src="images/image14.png" style="width: 571.50px; height: 142.66px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">In this case, the default value of 350 works well - the trees and the HDBs are traced quite accurately. </span></p><p class="c1"><span class="c0">However, the program may have trouble identifying the obstacles if the sky is cloudy or if the buildings are too similar to the colour of the sky. </span></p><p class="c1"><span class="c0">In this case, it will be more accurate if you manually trace the obstacles with a red line and erase the sky before feeding it into the program:</span></p><p class="c1"><span class="c0">In Paint 3D, use the red marker to draw over the trees and buildings, then use the eraser tool to erase the sky (don&rsquo;t erase the red marker line):</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 329.33px;"><img alt="" src="images/image20.png" style="width: 602.00px; height: 329.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">You should have an image like this:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 150.67px;"><img alt="" src="images/image7.png" style="width: 602.00px; height: 150.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="13"><li class="c1 c9"><span class="c0">You can test the sensitivity multiple times, until the program traces all the obstacles accurately. If you manually trace the sky with a red line and erase the sky like illustrated above, the default sensitivity value of 350 should be accurate.</span></li><li class="c1 c9"><span>Select a computation interval - the default value of 5 minutes means that the position of the sun is calculated and compared to the positions of the obstacles every 5 minutes. <br></span><span class="c8">Recommended to leave this as the default. A lower value (e.g. 1 minute) will take more time to compute, but does not increase accuracy because the accuracy bottleneck is with the image tracing.</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 592.00px; height: 357.00px;"><img alt="" src="images/image8.png" style="width: 592.00px; height: 357.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><ol class="c4 lst-kix_wcy63pfyokw9-0" start="15"><li class="c1 c9"><span class="c0">Click &ldquo;Compute&rdquo; to begin calculations:</span></li></ol><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 314.67px;"><img alt="" src="images/image1.png" style="width: 602.00px; height: 314.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c8">The program will say &ldquo;Not Responding&rdquo;, but it is actually making a lot of calculations in the background - see the console window. Don&rsquo;t click the window repeatedly.</span></p><p class="c1"><span class="c0">When it is done (about 1-2 minutes), the program will generate a report at the folder specified, and a window will pop up:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 388.00px; height: 95.00px;"><img alt="" src="images/image23.png" style="width: 388.00px; height: 95.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><h1 class="c10 c2" id="h.kq58ipajpbwv"><span class="c7">Solar Report</span></h1><h2 class="c1 c2" id="h.kc642uf39hld"><span>Summary</span></h2><p class="c1"><span class="c0">The first page of the solar report summarizes how bad the shading is, in terms of percentage energy loss:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 547.24px; height: 131.17px;"><img alt="" src="images/image4.png" style="width: 547.24px; height: 131.17px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><h2 class="c1 c2" id="h.626zj9349e8r"><span>Skyline and sun path chart</span></h2><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 519.50px; height: 395.56px;"><img alt="" src="images/image31.png" style="width: 519.50px; height: 395.56px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">The second page shows the path of the sun (red dots) over the course of a day, together with the position of the obstacles (blue line). Recall that this is our panorama:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 150.67px;"><img alt="" src="images/image28.png" style="width: 602.00px; height: 150.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">Looking at the skyline and sun path chart, you can see that the bunch of trees on the right is blocking a lot of the afternoon and evening sun - a lot of the sun (red dots) is covered by the trees (blue line) from around 180&deg; to 330&deg;.</span></p><p class="c1"><span class="c0">Obstacles without any red dots below them do not affect the sun, because they don&rsquo;t overlap with the sun&rsquo;s path. For example, the round tree on the extreme left is in the white region of the chart, and will not cause shading at any time of the day.</span></p><h2 class="c1 c2" id="h.xm2bpj7z11sa"><span class="c6">Monthly and quarterly analysis</span></h2><p class="c1"><span>The subsequent pages show how each month will be affected by the shading. The energy received at the location is plotted for Day 15 of each month - Day 15 is selected to give an indication for the whole month.</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 481.00px; height: 357.54px;"><img alt="" src="images/image15.png" style="width: 481.00px; height: 357.54px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">From the quarterly chart above, you can see that January (blue line) is the weakest month in this quarter. The location will only receive sunlight from around 10 am to around 1:05 pm. The peak intensity is also lower. The panel should be sized so that there&rsquo;s enough power even for the weakest month.</span></p><h1 class="c2 c10" id="h.o89tzo1nk0xn"><span class="c7">Clouds and rain</span></h1><p class="c1"><span class="c0">Referring to the report&rsquo;s summary:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 547.24px; height: 131.17px;"><img alt="" src="images/image4.png" style="width: 547.24px; height: 131.17px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">The overall solar potential of 1580 kWh/sqm/year is taken from the EMA website. This includes losses due to rain and cloud cover. The actual irradiance value calculated also includes losses due to rain and cloud cover, but the losses are averaged over the year. Not all months are equal because there&rsquo;s more rain in some months (e.g. December). Thus, dividing this value by 12 would not be indicative of the solar potential of each month.</span></p><p class="c1"><span class="c0">Referring to the monthly and quarterly analysis:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 439.50px; height: 328.13px;"><img alt="" src="images/image15.png" style="width: 439.50px; height: 328.13px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">The instantaneous irradiance values in these graphs assume a completely clear sky - the actual irradiance will almost always be lower. However, it wouldn&rsquo;t be possible to estimate the actual instantaneous irradiance, since that is subject to drifting clouds and rainfall.</span></p><h1 class="c2 c18" id="h.g8d1nixi39ga"><span class="c7">Using a hemispherical fisheye image instead</span></h1><p class="c1"><span class="c0">This is an example of a hemispherical lens used for solar analysis, taken from the NUS National Solar Repository:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 452.00px;"><img alt="" src="images/image29.png" style="width: 602.00px; height: 452.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c11"><span>Here&rsquo;s another image I found on the Internet (</span><span class="c14"><a class="c3" href="https://www.google.com/url?q=https://platypod.com/blog/tower-of-light-shooting-with-a-fisheye-lens&amp;sa=D&amp;ust=1582406735137000">https://platypod.com/blog/tower-of-light-shooting-with-a-fisheye-lens</a></span><span class="c0">), where there are more obstacles. There&rsquo;s no sun since it&rsquo;s taken at night, but it&rsquo;s just for illustration purposes.</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 429.50px; height: 429.50px;"><img alt="" src="images/image26.png" style="width: 429.50px; height: 429.50px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">Clip-on fisheye lenses are available for smartphones. They are a low-cost method to take images like these.</span></p><p class="c1"><span class="c0">If the potential panel location is not near a road (hence not covered by StreetView), it would be necessary to go to the location and take a hemispherical fisheye photo. Point the lens vertically upwards, at the height where the panel would be. Save it like a square image like the one above.</span></p><h2 class="c1 c2" id="h.bi3kihdqpwbk"><span class="c6">North alignment</span></h2><p class="c1"><span>Take note of where North is when you take the image. With a compass, rotate the lens until the North on the compass aligns with the vertical of the image (the red line shown above).</span></p><h2 class="c1 c2" id="h.n3l7vbapg5mk"><span class="c6">Unrolling and tracing a fisheye image</span></h2><p class="c1"><span class="c0">Input the image into the solar analysis program like before, but select the &ldquo;Hemispherical fisheye&rdquo; radio button instead:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 592.00px; height: 357.00px;"><img alt="" src="images/image18.png" style="width: 592.00px; height: 357.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">The program will unroll and trace the fisheye image for obstacles, just as it did for the 360&deg; panorama:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 602.00px; height: 301.33px;"><img alt="" src="images/image6.png" style="width: 602.00px; height: 301.33px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">If the obstacle tracing is unsatisfactory, you can manually trace the obstacles with a red marker and erase the sky in the middle portion like so:</span></p><p class="c5"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 440.00px; height: 440.00px;"><img alt="" src="images/image17.png" style="width: 440.00px; height: 440.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c1"><span class="c0">The rest of the steps in the analysis are the same - just remember to select the right image type.</span></p><h1 class="c18 c2" id="h.8uc43l3629jt"><span class="c7">Contact</span></h1><p class="c1"><span>Please email me at fan_b at meng.ucl.ac.uk</a></span><span class="c0">&nbsp;if there are errors in the program, or if you have a suggestion. Thanks! :)</span></p><div><p class="c20"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 817.00px; height: 43.00px;"><img alt="" src="images/image2.png" style="width: 817.00px; height: 43.00px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title="footer"></span></p></div></body></html>
