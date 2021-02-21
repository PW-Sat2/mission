PHOTO_SESSIONS = list(range(5190, session.session_number))

for p in range(0, 25):
    extract_file('pw_p{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/pw_p{}_0'.format(p), output_file_name='assembled/pw_p{}_0.jpg'.format(p))