PHOTO_SESSIONS = [1082]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for p in photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))
