#!/usr/bin/env python3
import requests
from exif import Image

LOCALHOST = "127.0.0.1"
#PORT = str(9050) # Edit if needed.
PORT = "9150"
proxies = {
'http': 'socks5h://' + LOCALHOST + ':' + PORT,
'https': 'socks5h://' + LOCALHOST + ':' + PORT
}

# Tiffs break that are out of official format.

# The market:
# 4jm77gv7h36xfnvnslizyavt2anheditededited.onion

# Order of operations:
# 1. Get user input.
# 2. Scrape the user market photo to local drive.
# 3. Process the local market photo on the local drive. (Save all file information to separate corresponding text files that accompany the photo name)

user = input('Input Market Photo: ')
name = user.split('/')[-1]
exifile = name.split('.')[0] + '.exif'

def write_image(url):
    r = requests.get(str(user), proxies=proxies)
    with open(name, 'wb') as image_file:
        image_file.write(r.content)
        image_file.flush()

def write_exif(data):
    with open(exifile, 'a+') as image_file:
        image_file.write(data + '\n')
        image_file.flush()

def main():
    write_image(user)

    my_image = Image(name)
    exifs = my_image.list_all()

    if len(exifs) > 0:
        print("This image has exif metadata.")

        if 'gps_longitude_ref' in exifs:
            print('gps longitude reference:', str(my_image.gps_longitude_ref))
            write_exif('gps longitude reference: ' + str(my_image.gps_longitude_ref))

        if 'gps_altitude' in exifs:
            print('gps altitude:', str(my_image.gps_altitude))
            write_exif('gps altitude: ' + str(my_image.gps_altitude))

        if 'gps_timestamp' in exifs:
            print('gps timestamp:', str(my_image.gps_timestamp))
            write_exif('gps timestamp: ' + str(my_image.gps_timestamp))

        if 'gps_datestamp' in exifs:
            print('gps datestamp:', str(my_image.gps_datestamp))
            write_exif('gps datestamp: ' + str(my_image.gps_datestamp))

        if 'gps_altitude_ref' in exifs:
            print('gps altitude reference:', str(my_image.gps_altitude_ref))
            write_exif('gps altitude reference: ' + str(my_image.gps_altitude_ref))

        if 'gps_latitude_ref' in exifs:
            print('gps latitude reference:', str(my_image.gps_latitude_ref))
            write_exif('gps latitude reference: ' + str(my_image.gps_latitude_ref))

        if 'gps_latitude' in exifs:
            print('gps latitude:', str(my_image.gps_latitude))
            write_exif('gps latitude: ' + str(my_image.gps_latitude))

        if 'gps_longitude' in exifs:
            print('gps longitude:', str(my_image.gps_longitude))
            write_exif('gps longitude: ' + str(my_image.gps_longitude))

        if 'model' in exifs:
            print('model:', str(my_image.model))
            write_exif('phone model: ' + str(my_image.model))

        if 'make' in exifs:
            print('make:', str(my_image.make))
            write_exif('phone make: ' + str(my_image.make))

        if 'software' in exifs:
            print('software:', str(my_image.software))
            write_exif('software: ' +  str(my_image.software))

        if 'datetime' in exifs:
            print('datetime:', str(my_image.datetime))
            write_exif('date and time: ' +  str(my_image.datetime))

        if 'gps_dop' in exifs:
            print('gps_dop:', str(my_image.gps_dop))
            write_exif('GPS DOP: ' +  str(my_image.gps_dop))

    elif len(exifs) < 1:
        print("This image has no exif metadata.")

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print('JPEG Bytes are Out Of Order.')
        print('This is not an actual JPEG.')
        print('You may need to manually check the image.')

