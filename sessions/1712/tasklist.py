tasks = [
    # Generated on 2019-08-23 17:38:33.895000, contains telemetry from sessions 1711 to 1712.
    # The session starts on 2019-08-24 11:47:11+02:00.

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
    [tc.DownloadFile(100, '/radfet_20', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # suns experiment
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_ps_11'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Wait for good uplink and downlink - photo queue.", Print, WaitMode.Wait],

    [tc.TakePhotoTelecommand(150, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(151, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p2_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(152, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(153, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p4_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(154, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(155, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p6_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(156, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(157, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p8_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(158, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(159, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p10_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(160, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p11_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(161, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p12_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(162, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p13_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(163, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p14_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(164, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p15_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(165, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p16_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(166, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p17_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(167, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p18_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(168, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p19_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(169, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p20_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(170, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p21_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(171, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p22_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(172, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p23_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(173, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p24_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(173, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p25_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(174, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p26_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(175, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p27_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(176, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p28_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(177, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p29_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(178, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p30_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(179, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p31_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(180, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p32_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(181, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p33_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(182, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p34_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(183, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p35_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(184, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p36_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(185, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p37_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(186, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p38_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(187, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p39_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(188, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p40_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(189, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p41_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(190, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p42_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(191, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2, seconds=30), 'p43_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(192, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p44_128'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]