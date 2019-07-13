PHOTO_SESSIONS = [1460, 1461, 1462, 1463]

photos_queue = range(1, 51)
photos_series = range(0, 29)

for p in photos_queue:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in photos_series:
    extract_file('p52_128_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p52_128_{}'.format(p), output_file_name='assembled/p52_128_{}.jpg'.format(p))

for p in ['p0n_480_0', 'p0w_480_0']:
    extract_file(p, also=PHOTO_SESSIONS)
    decode_photo(p, output_file_name='assembled/{}.jpg'.format(p))
