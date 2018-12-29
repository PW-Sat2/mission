def extract_sail():
    import base64

    file_frames = only_type(frames, response_frames.FileSendSuccessFrame)
    file_frames = filter(lambda f: f.correlation_id == 199, file_frames)

    sail_frames = only_type(store.get_session(157).frames(['all']), response_frames.SailExperimentFrame)
    sail_frames += file_frames
    sail_frames = unique_seqs(sail_frames)
    sail_frames = sorted(sail_frames, key=lambda f: f.seq())

    print(sail_frames)

    with session.open_artifact('assembled/sail.exp', 'wb') as f:
        for frame in sail_frames:
            f.write(ensure_string(frame.response))

extract_sail()

parse_experiment('assembled/sail.exp')

photos = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,  57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87]

for p in photos:
    extract_file('sail.photo_{}'.format(p), also=[158])
    decode_photo('assembled/sail.photo_{}'.format(p), output_file_name='assembled/sail_photo_{}.jpg'.format(p))
