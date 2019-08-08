# ssm_v0.3 - solar shading modeller
# New in v0.3 - Added GUI

# This program calculates how much solar irradiation is reduced due to shading by surrounding obstructions,
# It requires the input of either 1. a hemispherical fisheye image taken upwards (true north aligned with image north,
# or 2. a 360 deg spherical panorama (true north aligned with the left of the image)
# Written by Bowen: fan_b@meng.ucl.ac.uk

import numpy as np
import easygui
import matplotlib.pyplot as plt
import csv
import subprocess
import PySimpleGUI as sg
import os
from math import *
from PIL import Image
from matplotlib.backends.backend_pdf import PdfPages
from resizeimage import resizeimage

# Begin image manipulation functions
# These functions trace the input image into an array of azimuth and elevation values


def squareImage(im):
    (width, height) = im.size
    box = ((width - height) / 2, 0, (width + height) / 2, height)
    return im.crop(box)


def despherifyImage(im):
    (width, height) = im.size
    half_width = int(im.size[0] / 2)
    half_height = int(im.size[1] / 2)
    inpix = im.load()
    out = Image.new("L", (width, half_height))
    outpix = out.load()
    full_circle = 1000.0 * 2 * pi
    for r in range(half_width):
        for theta in range(int(full_circle)):
            (inx, iny) = (round(r * cos(theta / 1000.0)) + half_width, round(r * sin(theta / 1000.0)) + half_width)
            (outx, outy) = (width - width * (theta / full_circle) - 1, r)
            outpix[outx, outy] = inpix[inx, iny]
    return out


def differentiateImageColumns(im):
    (width, height) = im.size
    pix = im.load()
    for x in range(width):
        for y in range(height - 1):
            pix[x, y] = min(10 * abs(pix[x, y] - pix[x, y + 1]), 255)
    return im


def redlineImage(im, threshold):
    (width, height) = im.size
    imgcsv_azimuth = []
    imgcsv_elevation = [0] * width
    pix = im.load()
    for x in range(width):
        for y in range(height - 1):
            (R, G, B) = pix[x, y]
            if R + G + B > threshold:
                pix[x, y] = (255, 0, 0)
                imgcsv_elevation[x] = ((height-y)/height) * 90
                break
        imgcsv_azimuth.append(x)
    return im, imgcsv_azimuth, imgcsv_elevation

# End image manipulation functions

# Begin geometry functions


def cylindrical_to_cartesian(distance, azimuth, height):
    azi_rad = np.deg2rad(azimuth)
    x_cart = distance * np.cos(azi_rad)
    y_cart = distance * np.sin(azi_rad)
    z_cart = height
    return x_cart,y_cart,z_cart


def cylindrical_to_horizontal(distance, height):
    elev_obj_rad = np.arctan((height/distance))
    elev_obj_deg = np.rad2deg(elev_obj_rad)
    return elev_obj_deg


def azimuth_to_elevation(azimuth_integer):
    elevation = linspace_elevations[azi_deg_rounded-1]
    print('Obstruction elevation: ', elevation, file=text_data)
    print('Obstruction elevation: ', elevation)
    return elevation

# End geometry functions

# Begin sun mapping and irradiation functions
# These functions calculate the position of the sun at any point in time through the year


def solar_position_calc(day, hr, min):
    # Singapore latitude = 1.3521 degrees North
    # Singapore longitude = 103.8198 degrees East
    # Singapore timezone is +8 hours from UTC

    latitude = 1.3521
    lat_rad = np.deg2rad(latitude)
    longitude = 103.8198
    lon_rad = np.deg2rad(longitude)
    timezone = 8

    # Refer to the NOAA paper "General Solar Position Calculations"
    # https://www.esrl.noaa.gov/gmd/grad/solcalc/solareqns.PDF

    y = (2 * 3.14159265/365) * (day - 1 + (hr-12)/24)
    eqtime = 229.18 * (0.000075 + 0.001868 * np.cos(y) - 0.032077 * np.sin(y) - 0.014615 * np.cos(2 * y)
                       - 0.040849 * np.sin(2 * y))
    declin = 0.006918 - 0.399912 * np.cos(y) + 0.070257 * np.sin(y) - 0.006758 * np.cos(2 * y) + 0.000907 \
             * np.sin(2 * y) - 0.002697 * np.cos(3 * y) + 0.00148 * np.sin(3 * y)

    time_offset = eqtime + 4 * longitude - 60 * timezone

    # Compute true solar time
    tst = hr * 60 + min + time_offset
    # Compute solar hour angle
    ha_deg = (tst/4) - 180
    ha_rad = np.deg2rad(ha_deg)

    # Compute solar zenith
    cos_zen = np.sin(lat_rad) * np.sin(declin) + np.cos(lat_rad) * np.cos(declin) * np.cos(ha_rad)
    zen_rad = np.arccos(cos_zen)
    zen_deg = np.rad2deg(zen_rad)

    # Compute solar azimuth
    if ha_deg > 0:
        cos_pi_minus_azi = ((np.sin(lat_rad) * np.cos(zen_rad) - np.sin(declin)) / (np.cos(lat_rad) * np.sin(zen_rad)))
        pi_minus_azi = np.arccos(cos_pi_minus_azi)
        azi_deg = (180 + np.rad2deg(pi_minus_azi)) % 360

    else:
        cos_pi_minus_azi = ((np.sin(lat_rad) * np.cos(zen_rad) - np.sin(declin)) / (np.cos(lat_rad) * np.sin(zen_rad)))
        pi_minus_azi = np.arccos(cos_pi_minus_azi)
        azi_deg = (540 - np.rad2deg(pi_minus_azi)) % 360

    # Compute solar elevation to tell whether it is night or day
    elev_deg = 90 - zen_deg
    if elev_deg >= 0:
        night_or_day = 'Day'
    else:
        night_or_day = 'Night'

    zen_deg_rounded = int(round(zen_deg))
    azi_deg_rounded = int(round(azi_deg))
    elev_deg_rounded = int(round(elev_deg))

    print('Zenith: ',zen_deg_rounded, '\nAzimuth: ',azi_deg_rounded,'\nElevation: ',elev_deg_rounded,'\n',night_or_day, file=text_data)
    print('Zenith: ',zen_deg_rounded, '\nAzimuth: ',azi_deg_rounded,'\nElevation: ',elev_deg_rounded,'\n',night_or_day)

    return zen_deg_rounded, azi_deg_rounded, elev_deg_rounded, night_or_day


def insolation(sun_zenith):
    sun_zenith_radians = np.deg2rad(sun_zenith)
    solar_constant = 1362 #watts per square meter
    insolation = solar_constant * np.cos(sun_zenith_radians)

    return insolation

# End sun mapping and irradiation functions

# Begin program operation

# Begin experimental GUI code


layout = [[sg.Text('Location name:'), sg.Input()],
          [sg.Text('Image type:'),
          sg.Radio('Hemispherical fisheye', "RADIO1", default=True), sg.Radio('360 deg panorama', "RADIO1")],
          [sg.Text('Select image file:'), sg.Input(), sg.FileBrowse()],
          [sg.Text('Set sky sensitivity threshold:'),
          sg.Slider(range=(1,700), default_value=200, size=(20,15), orientation='horizontal')],
          [sg.Text('Output Folder:'), sg.Input(), sg.FolderBrowse()],
          [sg.Button('Test')],
          [sg.Text('Set computation interval:'),
          sg.Slider(range=(1,60), default_value=15, size=(20,15), orientation='horizontal')],
          [sg.Button('Compute')]
          ]

window = sg.Window('Solar Shading Modeller - PUB', layout)

while True:  # Event Loop
    event, values = window.Read()
    print(event, values)

    if event is None:
        break

    if event == 'Test':
        try:
            # Create target Directory
            os.mkdir(values[5] + '/' + values[0])
            print("Directory ", values[5] + '/' + values[0], " Created ")
        except FileExistsError:
            print("Directory ", values[5] + '/' + values[0], " already exists")

        path_Image = values[3]
        threshold = values[4]
        if values[1]:
            im = Image.open(path_Image).convert("L")
            im = squareImage(im)
            lin = despherifyImage(im)
            d = differentiateImageColumns(lin).convert("RGB")
        elif values[2]:
            im = Image.open(path_Image).convert("L")
            d = differentiateImageColumns(im).convert("RGB")

        img_resized = resizeimage.resize_width(d, 360)
        img_resized.save(values[5] + '/' + values[0] + '/' + 'ResizedImage.bmp', img_resized.format)

        r, imgcsv_azimuth, imgcsv_elevation = redlineImage(img_resized, threshold)

        # Write to csv
        with open(values[5] + '/' + values[0] + '/' + 'ImageVectorData.csv', 'w', newline='') as img_csv_file:
            writer = csv.writer(img_csv_file)
            writer.writerow(['azimuth', 'elevation'])
            writer.writerows(zip(imgcsv_azimuth, imgcsv_elevation))

        r.show()
        r.save(values[5] + '/' + values[0] + '/' + 'TracedImage.bmp')

        linspace_azimuths = imgcsv_azimuth
        linspace_elevations = imgcsv_elevation

    elif event == 'Compute':
        try:
            # Create target Directory
            os.mkdir(values[5] + '/' + values[0])
            print("Directory ", values[5] + '/' + values[0], " Created ")
        except FileExistsError:
            print("Directory ", values[5] + '/' + values[0], " already exists")

        window.Close()
        path_Image = values[3]
        threshold = values[4]

        if values[1]:
            im = Image.open(path_Image).convert("L")
            im = squareImage(im)
            lin = despherifyImage(im)
            d = differentiateImageColumns(lin).convert("RGB")
        elif values[2]:
            im = Image.open(path_Image).convert("L")
            d = differentiateImageColumns(im).convert("RGB")

        img_resized = resizeimage.resize_width(d, 360)
        img_resized.save(values[5] + '/' + values[0] + '/' + 'ResizedImage.bmp', img_resized.format)

        r, imgcsv_azimuth, imgcsv_elevation = redlineImage(img_resized, threshold)

        # Write to csv
        with open(values[5] + '/' + values[0] + '/' + 'ImageVectorData.csv', 'w', newline='') as img_csv_file:
            writer = csv.writer(img_csv_file)
            writer.writerow(['azimuth', 'elevation'])
            writer.writerows(zip(imgcsv_azimuth, imgcsv_elevation))

        r.show()
        r.save(values[5] + '/' + values[0] + '/' + 'TracedImage.bmp')

        linspace_azimuths = imgcsv_azimuth
        linspace_elevations = imgcsv_elevation

        # Draw plotting axes

        plt.figure(1)
        plt.xlim(right=360, left=0)
        plt.xticks(np.arange(0, 361, 30))
        plt.ylim(top=90, bottom=0)
        plt.yticks(np.arange(0, 91, 10))
        plt.xlabel('Azimuth from 0 to 360 degrees')
        plt.ylabel('Elevation from 0 to 90 degrees')
        plt.title('Skyline & sun path chart')

        # Program will iteratively compute at the user-defined interval
        # Not recommended to compute at intervals below 5 minutes on computers with less than 8GB RAM
        # 5 minutes is sufficient for fairly accurate results; 15 minutes for quick results

        frequency = int(values[6])
        time_intervals = np.linspace(0, 525600, num=525600 // frequency, dtype=int)
        shade_counter = 0

        potential_insolation_counter = 0
        actual_insolation_counter = 0
        instant_potential_insolation = 0
        instant_actual_insolation = 0

        jan_min, feb_min, mar_min, apr_min, may_min, jun_min, jul_min, aug_min, sep_min, oct_min, nov_min, dec_min \
            = [], [], [], [], [], [], [], [], [], [], [], []

        jan_insolation, feb_insolation, mar_insolation, apr_insolation, may_insolation, jun_insolation, jul_insolation, \
        aug_insolation, sep_insolation, oct_insolation, nov_insolation, dec_insolation \
            = [], [], [], [], [], [], [], [], [], [], [], []

        text_data = open(values[5] + '/' + values[0] + '/' + r"RawData.txt", "w")

        # Begin iterative computing

        for time_min in time_intervals:
            sg.OneLineProgressMeter('Computing solar obstructions', time_min+1, 525600, 'key')

            day = time_min // 1440
            hr = (time_min - day * 1440) // 60
            min = (time_min - day * 1440 - hr * 60)

            print('\n', day, hr, min, file=text_data)
            print('\n', day, hr, min)

            zen_deg_rounded, azi_deg_rounded, elev_deg_rounded, night_or_day = solar_position_calc(day, hr, min)

            if night_or_day == 'Night':
                instant_actual_insolation = 0

            else:
                instant_potential_insolation = insolation(zen_deg_rounded)
                potential_insolation_counter = potential_insolation_counter + instant_potential_insolation

                if elev_deg_rounded < azimuth_to_elevation(azi_deg_rounded):
                    instant_actual_insolation = 0
                    print('Is shaded', file=text_data)
                    print('Is shaded')

                else:
                    instant_actual_insolation = insolation(zen_deg_rounded)
                    actual_insolation_counter = actual_insolation_counter + instant_actual_insolation
                    print('Is not shaded', file=text_data)
                    print('Is not shaded')

                year_chart = plt.plot(azi_deg_rounded, elev_deg_rounded, 'r,')

            if day == 14:  # 15 Jan is day 14, starting from day 0
                jan_min.append((time_min - day * 1440) / 60)
                jan_insolation.append(instant_actual_insolation)

            if day == 45:  # 15 Feb is day 45, from day 0
                feb_min.append((time_min - day * 1440) / 60)
                feb_insolation.append(instant_actual_insolation)

            if day == 73:  # 15 Mar is day 73, from day 0
                mar_min.append((time_min - day * 1440) / 60)
                mar_insolation.append(instant_actual_insolation)

            if day == 104:
                apr_min.append((time_min - day * 1440) / 60)
                apr_insolation.append(instant_actual_insolation)

            if day == 134:
                may_min.append((time_min - day * 1440) / 60)
                may_insolation.append(instant_actual_insolation)

            if day == 165:
                jun_min.append((time_min - day * 1440) / 60)
                jun_insolation.append(instant_actual_insolation)

            if day == 195:
                jul_min.append((time_min - day * 1440) / 60)
                jul_insolation.append(instant_actual_insolation)

            if day == 226:
                aug_min.append((time_min - day * 1440) / 60)

                aug_insolation.append(instant_actual_insolation)
            if day == 257:
                sep_min.append((time_min - day * 1440) / 60)
                sep_insolation.append(instant_actual_insolation)

            if day == 287:
                oct_min.append((time_min - day * 1440) / 60)
                oct_insolation.append(instant_actual_insolation)

            if day == 318:
                nov_min.append((time_min - day * 1440) / 60)
                nov_insolation.append(instant_actual_insolation)

            if day == 348:
                dec_min.append((time_min - day * 1440) / 60)
                dec_insolation.append(instant_actual_insolation)

        total_potential_insolation = potential_insolation_counter / len(time_intervals)
        total_actual_insolation = actual_insolation_counter / len(time_intervals)

        print('\nTotal solar potential if the location is unshaded =', total_potential_insolation,
              'watts per square meter', file=text_data)
        print('\nActual solar energy accounting for shading =', total_actual_insolation, 'watts per square meter',
              file=text_data)
        print('\nGenerating PDF report - SolarReport.pdf - file can be found in active program folder', file=text_data)

        print('\nTotal solar potential if the location is unshaded =', total_potential_insolation,
              'watts per square meter')
        print('\nActual solar energy accounting for shading =', total_actual_insolation, 'watts per square meter')
        print('\nGenerating PDF report - SolarReport.pdf - file can be found in active program folder')
        print('\nSaving raw data text output - RawData.txt - file can be found in active program folder')

        text_data.close()

        # Begin plotting functions
        # These functions are responsible for generating the final PDF report

        plt.figure(1)
        year_chart = plt.plot(linspace_azimuths, linspace_elevations)

        plt.figure(2)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 January')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        jan_chart = plt.plot(jan_min, jan_insolation)

        plt.figure(3)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 February')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        feb_chart = plt.plot(feb_min, feb_insolation)

        plt.figure(4)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 March')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        mar_chart = plt.plot(mar_min, mar_insolation)

        plt.figure(5)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 April')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        apr_chart = plt.plot(apr_min, apr_insolation)

        plt.figure(6)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 May')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        may_chart = plt.plot(may_min, may_insolation)

        plt.figure(7)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 June')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        jun_chart = plt.plot(jun_min, jun_insolation)

        plt.figure(8)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 July')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        jul_chart = plt.plot(jul_min, jul_insolation)

        plt.figure(9)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 August')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        aug_chart = plt.plot(aug_min, aug_insolation)

        plt.figure(10)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 September')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        sep_chart = plt.plot(sep_min, sep_insolation)

        plt.figure(11)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 October')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        oct_chart = plt.plot(oct_min, oct_insolation)

        plt.figure(12)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 November')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        nov_chart = plt.plot(nov_min, nov_insolation)

        plt.figure(13)
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15 December')
        plt.ylabel('Instantaneous irradiance in watts per sqm')
        dec_chart = plt.plot(dec_min, dec_insolation)

        plt.figure(14)
        plt.plot(jan_min, jan_insolation, label='Jan')
        plt.plot(feb_min, feb_insolation, label='Feb')
        plt.plot(mar_min, mar_insolation, label='Mar')
        plt.plot(apr_min, apr_insolation, label='Apr')
        plt.plot(may_min, may_insolation, label='May')
        plt.plot(jun_min, jun_insolation, label='Jun')
        plt.plot(jul_min, jul_insolation, label='Jul')
        plt.plot(aug_min, aug_insolation, label='Aug')
        plt.plot(sep_min, sep_insolation, label='Sep')
        plt.plot(oct_min, oct_insolation, label='Oct')
        plt.plot(nov_min, nov_insolation, label='Nov')
        plt.plot(dec_min, dec_insolation, label='Dec')
        plt.legend(loc='upper right')
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15th of each month (whole year)')
        plt.ylabel('Instantaneous irradiance in watts per sqm')

        plt.figure(15)
        plt.plot(jan_min, jan_insolation, label='Jan')
        plt.plot(feb_min, feb_insolation, label='Feb')
        plt.plot(mar_min, mar_insolation, label='Mar')
        plt.legend(loc='upper right')
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15th of each month (1st quarter)')
        plt.ylabel('Instantaneous irradiance in watts per sqm')

        plt.figure(16)
        plt.plot(apr_min, apr_insolation, label='Apr')
        plt.plot(may_min, may_insolation, label='May')
        plt.plot(jun_min, jun_insolation, label='Jun')
        plt.legend(loc='upper right')
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15th of each month (2nd quarter)')
        plt.ylabel('Instantaneous irradiance in watts per sqm')

        plt.figure(17)
        plt.plot(jul_min, jul_insolation, label='Jul')
        plt.plot(aug_min, aug_insolation, label='Aug')
        plt.plot(sep_min, sep_insolation, label='Sep')
        plt.legend(loc='upper right')
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15th of each month (3rd quarter)')
        plt.ylabel('Instantaneous irradiance in watts per sqm')

        plt.figure(18)
        plt.plot(oct_min, oct_insolation, label='Oct')
        plt.plot(nov_min, nov_insolation, label='Nov')
        plt.plot(dec_min, dec_insolation, label='Dec')
        plt.legend(loc='upper right')
        plt.xlim(right=22, left=5)
        plt.xticks(np.arange(5, 22, step=1))
        plt.xlabel('Time through 15th of each month (4th quarter)')
        plt.ylabel('Instantaneous irradiance in watts per sqm')

        with PdfPages(values[5] + '/' + values[0] + '/' + 'SolarReport.pdf') as pdf:
            firstPage = plt.figure()
            firstPage.clf()
            txt0 = 'Solar shading report for location: ' + values[0]
            txt1 = 'Total solar potential if the location is unshaded = ' + str(
                round(total_potential_insolation)) + ' watts per square meter'
            txt2 = 'Actual irradiance accounting for shading = ' + str(
                round(total_actual_insolation)) + ' watts per square meter'
            firstPage.text(0.5, 0.58, txt0, transform=firstPage.transFigure, size=9, ha="center")
            firstPage.text(0.5, 0.48, txt1, transform=firstPage.transFigure, size=8, ha="center")
            firstPage.text(0.5, 0.52, txt2, transform=firstPage.transFigure, size=8, ha="center")
            pdf.savefig(firstPage)

            for fig in range(1, plt.gcf().number):
                pdf.savefig(fig)

        break

    window.Close()

if event is not None:
#    sg.Popup('Solar report generated at selected folder - SolarReport.pdf')

    layout2 = [[sg.Text('Solar report generated at selected folder - SolarReport.pdf')],
               [sg.Button('Open'), sg.Button('Cancel')]]

    window2 = sg.Window('Solar shading report generated', layout2)
    event2, values2 = window2.Read()

    while True:
        if event2 is None or event2 == 'Cancel':
            break
        if event2 == 'Open':
            os.startfile(values[5] + '/' + values[0] + '/' + 'SolarReport.pdf')
            break
    window2.Close()

# End of program, report generated as SolarReport.pdf in the running directory

# End experimental GUI code
