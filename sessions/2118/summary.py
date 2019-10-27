PHOTO_SESSIONS = [2114, 2115, 2116, 2117]

lr_photos = range(0, 29)

hr_photos = ['t01n_480_0', 't01w_480_0']

for p in lr_photos:
    extract_file('t02w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t02w_240_{}'.format(p), output_file_name='assembled/t02w_240_{}.jpg'.format(p))

for p in hr_photos:
    extract_file(p, also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))

