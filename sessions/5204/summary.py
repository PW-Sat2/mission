PHOTO_SESSIONS = list(range(5190, session.session_number))

for p in range(0, 25):
    extract_file('pw_p{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/pw_p{}_0'.format(p), output_file_name='assembled/pw_p{}_0.jpg'.format(p))


photos = ['o1_w_128_0', 'o1_n_480_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))