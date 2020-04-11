tasks = [
     # Get beacons from deep-sleep
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    # Wake-up from deep-sleep
    [[tc.PingTelecommand(), 15], SendLoop, WaitMode.NoWait],

    # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Get few beacons from nominal OBC
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_36'), Send, WaitMode.Wait],

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(17, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(26, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],
    
    # =========================================

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # =========================================

    [tc.ListFiles(80, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p1_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_128_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p1_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p1_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p1_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p1_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p1_480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p1_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p1_480_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait],    


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]