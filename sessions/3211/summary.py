PHOTO_SESSIONS = [3207, 3208, 3210]

for p in range(1, 11):
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))



SUNS_SESSIONS = [3207, 3208, 3210]
extract_file('suns_ps_17', also=SUNS_SESSIONS)