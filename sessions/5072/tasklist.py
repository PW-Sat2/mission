tasks = [
    # Generated on 2021-01-30 22:13:04.454613, contains telemetry from sessions 5071 to 5072.
    # The session starts on 2021-01-30 22:58:31+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # radfet_58
    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_58'), Send, WaitMode.Wait],

    # foteczki (11:04), zakladamy wyslanie o 11:00
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=17), 'p480_w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p480_n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'p480_w_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p480_n_2'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [448, 498, 548, 598, 648, 473, 523, 573, 623, 461, 511, 561, 611, 661, 485, 535, 585, 635, 455, 505]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [555, 605, 655, 467, 517, 567, 617, 479, 529, 579, 629, 491, 541, 591, 641]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [14, 314]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [294, 644, 2044, 2094, 2144, 2194, 2244]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
