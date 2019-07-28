PHOTO_SESSIONS = [1544, 1546, 1547, 1549, 1550, 1551]

photos = range(0, 29)

photos_single_low_res = range(1, 7)
photos_single_high_res = [1, 2]

for p in photos:
    extract_file('p_480_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p_480_{}'.format(p), output_file_name='assembled/p_480_{}.jpg'.format(p))

for p in photos_single_low_res:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in photos_single_high_res:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))