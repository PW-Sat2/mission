PHOTO_SESSIONS = []


extract_file('p0_n_p480_0'.format(p), also=PHOTO_SESSIONS)
decode_photo('assembled/p0_n_p480_0'.format(p), output_file_name='assembled/p0_n_p480_0.jpg'.format(p))

extract_file('p1_w_p480_0'.format(p), also=PHOTO_SESSIONS)
decode_photo('assembled/p1_w_p480_0'.format(p), output_file_name='assembled/p1_w_p480_0.jpg'.format(p))

extract_file('p2_n_p480_0'.format(p), also=PHOTO_SESSIONS)
decode_photo('assembled/p2_n_p480_0'.format(p), output_file_name='assembled/p2_n_p480_0.jpg'.format(p))

extract_file('p3_w_p480_0'.format(p), also=PHOTO_SESSIONS)
decode_photo('assembled/p3_w_p480_0'.format(p), output_file_name='assembled/p3_w_p480_0.jpg'.format(p))

