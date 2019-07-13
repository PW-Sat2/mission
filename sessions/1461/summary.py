PHOTO_SESSIONS = []

photos_queue = [1, 5, 10, 15, 20, 25, 29]
photos_series = [0, 5, 10, 15, 20, 25]

for p in photos_queue:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in photos_series:
    extract_file('p52_128_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p52_128_{}'.format(p), output_file_name='assembled/p52_128_{}.jpg'.format(p))

