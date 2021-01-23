PHOTO_SESSIONS = []
SUNS_SESSIONS = []


extract_file('p0_n_p480_0', also=PHOTO_SESSIONS)
decode_photo('assembled/p0_n_p480_0', output_file_name='assembled/p0_n_p480_0.jpg')

extract_file('p1_w_p480_0', also=PHOTO_SESSIONS)
decode_photo('assembled/p1_w_p480_0', output_file_name='assembled/p1_w_p480_0.jpg')

extract_file('p2_n_p480_0', also=PHOTO_SESSIONS)
decode_photo('assembled/p2_n_p480_0', output_file_name='assembled/p2_n_p480_0.jpg')

extract_file('p3_w_p480_0', also=PHOTO_SESSIONS)
decode_photo('assembled/p3_w_p480_0', output_file_name='assembled/p3_w_p480_0.jpg')

extract_file('suns_ps_19', also=SUNS_SESSIONS)