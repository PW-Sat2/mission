PHOTO_SESSIONS = []

photos = ['a_w_p480_11_22_0', 'a_n_p480_11_22_0', 'a_w_p480_11_26_0', 'a_n_p480_11_26_0', 'a_w_p480_11_32_0',
          'a_n_p480_11_32_0', 'a_w_p480_11_40_0', 'a_n_p480_11_40_0', 'a_w_p480_11_52_0', 'a_n_p480_11_52_0',
          'a_w_p480_11_56_0', 'a_n_p480_11_56_0', 'a_w_p480_12_00_0', 'a_n_p480_12_00_0', 'a_w_p480_12_04_0',
          'a_n_p480_12_04_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))