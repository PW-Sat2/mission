PHOTO_SESSIONS = []

photos = [1, 2, 3, 4]

for p in photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

    extract_file('p{}_240_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_240_0'.format(p), output_file_name='assembled/p{}_240_0.jpg'.format(p))
