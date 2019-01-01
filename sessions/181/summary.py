PHOTO_SESSIONS = [180]

low_photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
high_photos = [1, 2, 3, 4, 5, 6, 7, 9]

for p in low_photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in high_photos:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))
