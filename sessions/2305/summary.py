PHOTO_SESSIONS = [2288, 2289, 2290, 2291, 2293, 2294, 2295, 2296, 2297, 2298, 2300, 2301, 2302, 2303, 2304]

lr_photos = range(0, 29)

for p in lr_photos:
    extract_file('t01w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t01w_240_{}'.format(p), output_file_name='assembled/t01w_240_{}.jpg'.format(p))

    extract_file('t02w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t02w_240_{}'.format(p), output_file_name='assembled/t02w_240_{}.jpg'.format(p))

    extract_file('t03n_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t03n_240_{}'.format(p), output_file_name='assembled/t03n_240_{}.jpg'.format(p))

    extract_file('t04n_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t04n_240_{}'.format(p), output_file_name='assembled/t04n_240_{}.jpg'.format(p))
