PHOTO_SESSIONS = [2476, 2478, 2479, 2480]

lr_photos = range(0, 29)
lr_photos2 = range(0, 7)

for p in lr_photos:
    extract_file('t01w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t01w_240_{}'.format(p), output_file_name='assembled/t01w_240_{}.jpg'.format(p))

    extract_file('t02w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t02w_240_{}'.format(p), output_file_name='assembled/t02w_240_{}.jpg'.format(p))
        
    extract_file('t03w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t03w_240_{}'.format(p), output_file_name='assembled/t03w_240_{}.jpg'.format(p))

for p in lr_photos2:
    extract_file('t04w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t04w_240_{}'.format(p), output_file_name='assembled/t04w_240_{}.jpg'.format(p))