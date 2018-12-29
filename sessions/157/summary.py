sail_frames = only_type(frames, response_frames.SailExperimentFrame)
sail_frames = unique_seqs(sail_frames)
sail_frames = sorted(sail_frames, key=lambda f: f.seq())

with session.open_artifact('sail.exp', 'wb') as f:
    for frame in sail_frames:
        f.write(ensure_string(frame.response))


parse_experiment('sail.exp')