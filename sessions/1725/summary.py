PHOTO_SESSIONS = [1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39]

for p in photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

photosLR = [12, 13, 14, 15, 16, 17, 18, 19, 20]
photosHR = [12, 13, 14, 15, 17, 19, 20]

for p in photosLR:
    extract_file('t{}w_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}w_128_0'.format(p), output_file_name='assembled/t{}w_128_0.jpg'.format(p))

    extract_file('t{}n_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}n_128_0'.format(p), output_file_name='assembled/t{}n_128_0.jpg'.format(p))

for p in photosHR:
    extract_file('t{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}w_480_0'.format(p), output_file_name='assembled/t{}w_480_0.jpg'.format(p))

    extract_file('t{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}n_480_0'.format(p), output_file_name='assembled/t{}n_480_0.jpg'.format(p))