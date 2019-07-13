PHOTO_SESSIONS = []

photos = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for p in photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

