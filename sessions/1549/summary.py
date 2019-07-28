PHOTO_SESSIONS = [1544, 1546, 1547]

photos = range(0, 29)

for p in photos:
    extract_file('p_480_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p_480_{}'.format(p), output_file_name='assembled/p_480_{}.jpg'.format(p))
