PHOTO_SESSIONS = [901, 904, 905, 907]

photos_hr = [2, 7]

for p in photos_hr:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))

extract_file('suns_ps_4')
parse_experiment('assembled/suns_ps_4')
