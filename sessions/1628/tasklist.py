tasks = [
    # Generated on 2019-08-03 10:48:57.006000, contains telemetry from sessions 1585 to 1586.
    # The session starts on 2019-08-03 11:44:03+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1, 51, 101, 151, 201, 26, 76, 126, 176, 14, 64, 114, 164, 214, 38, 88, 138, 188, 8, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [108, 158, 208, 20, 70, 120, 170, 220, 32, 82, 132, 182, 44, 94, 144, 194]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end
    
    [tc.TakePhotoTelecommand(50, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(51, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p1_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(52, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(53, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p2_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(54, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(55, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p3_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(56, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(57, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p4_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(58, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(59, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p5_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(60, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(61, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p6_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(62, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(63, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p7_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(64, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(65, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p8_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(66, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(67, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p9_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(68, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(69, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p10_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(70, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p11_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(71, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p11_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(72, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p12_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(73, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p12_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(74, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p13_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(75, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p13_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(76, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p14_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(77, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p14_480'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(78, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=5670), 'p15_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(79, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p15_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(80, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 'p16_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(81, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p16_480'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]