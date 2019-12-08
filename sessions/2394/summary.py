PHOTO_SESSIONS = [2391, 2392, 2393]

lr_photos = range(0, 29)

for p in lr_photos:
    extract_file('t01w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t01w_240_{}'.format(p), output_file_name='assembled/t01w_240_{}.jpg'.format(p))
