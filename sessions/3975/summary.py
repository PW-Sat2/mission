PHOTO_SESSIONS = []

files = [
    'a_w_11_30',
    'a_n_11_30',
    'a_w_11_31',
    'a_n_11_31',
    'a_w_11_32',
    'a_n_11_32',
    'a_w_11_40',
    'a_n_11_40',
    'a_w_11_41',
    'a_n_11_41',
    'a_w_11_42',
    'a_n_11_42',
    'a_w_11_57',
    'a_n_11_57',
    'a_w_11_58',
    'a_n_11_58',
    'a_w_11_59',
    'a_n_11_59',
    'a_w_12_59',
    'a_n_12_59',
    'a_w_13_00',
    'a_n_13_00',
    'a_w_13_01',
    'a_n_13_01',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')