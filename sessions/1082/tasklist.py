tasks = [
    # Generated on 2019-05-18 10:39:05.043000, contains telemetry from sessions 1081 to 1082.
    # The session starts on 2019-05-18 11:47:48+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [5, 55, 105, 155, 205, 30, 80, 130, 180, 18, 68, 118, 168, 218, 42, 92, 142, 192, 12, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [112, 162, 212, 24, 74, 124, 174, 224, 36, 86, 136, 186, 48, 98, 148, 198]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # RadFET download
    [tc.DownloadFile(40, '/radfet_13', range(0, 8)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/radfet_13', range(8, 16)), Send, WaitMode.Wait],


    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(17, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=16), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=16), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=48), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(26, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],

    # =========================================

    [tc.ListFiles(99, '/'), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.ListFiles(103, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]