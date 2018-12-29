import base64

sail_frames = only_type(frames, response_frames.SailExperimentFrame)
sail_frames = unique_seqs(sail_frames)
sail_frames = sorted(sail_frames, key=lambda f: f.seq())

with session.open_artifact('sail.exp', 'wb') as f:
    for frame in sail_frames:
        f.write(ensure_string(frame.response))


parse_experiment('sail.exp')

with session.open_artifact('sail.frames', 'w') as f:
    PREFIX = ensure_byte_list('a' * 16)
    SUFFIX = ensure_byte_list('b' * 2)

    for frame in sail_frames:
        (b0, b1, b2, _) = struct.pack('<L', frame.seq())
        
        header = 0
        header |= (frame.apid() & 0b00111111) << 0
        header |= ord(b0) << 6
        header |= ord(b1) << 14
        header |= ord(b2) << 24

        header_bytes = struct.pack('<L', header)
        header_bytes = ensure_byte_list(header_bytes)
        header_bytes = header_bytes[:3]

        raw = PREFIX + header_bytes + frame.payload() + SUFFIX
        raw = ensure_string(raw)
        raw = base64.b64encode(raw)

        f.write(',D,')
        f.write(raw)
        f.write('\n')