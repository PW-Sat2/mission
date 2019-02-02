PHOTO_SESSIONS = [389]
PHOTO_SESSIONS_480 = []

photos = [7, 9, 10]
photos_480 = [1, 2, 5, 8]

for p in photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in photos_480:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS_480)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))