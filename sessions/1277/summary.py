PHOTO_SESSIONS = [1275]

photos_lr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
photos_hr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for p in photos_lr:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))


for p in photos_hr:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))
