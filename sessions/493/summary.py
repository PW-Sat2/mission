PHOTO_SESSIONS_480 = [491, 492]

photos_480 = [1, 2, 3, 6, 7]

for p in photos_480:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS_480)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))