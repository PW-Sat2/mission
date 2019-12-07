extract_file('suns_ps_16', also=[2386, 2387, 2390])

PHOTO_SESSIONS = [2391]

lr_photos = range(0, 29)

for p in lr_photos:
    extract_file('t01w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t01w_240_{}'.format(p), output_file_name='assembled/t01w_240_{}.jpg'.format(p))
