PHOTO_SESSIONS = [1714]

extract_file('suns_ps_11')
extract_file('radfet_20')

extract_file('x2_128_0', also=PHOTO_SESSIONS)
decode_photo('assembled/x2_128_0', output_file_name='assembled/x2_128_0.jpg')

extract_file('x1_480_0', also=PHOTO_SESSIONS)
decode_photo('assembled/x1_480_0', output_file_name='assembled/x1_480_0.jpg')
