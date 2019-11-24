PHOTO_SESSIONS = [2288, 2289, 2290, 2291, 2293, 2294, 2295]

lr_photos = range(0, 29)

for p in lr_photos:
    extract_file('t01w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t01w_240_{}'.format(p), output_file_name='assembled/t01w_240_{}.jpg'.format(p))

    extract_file('t02w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t02w_240_{}'.format(p), output_file_name='assembled/t02w_240_{}.jpg'.format(p))
