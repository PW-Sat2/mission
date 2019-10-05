tasks = [
    # Generated on 2019-10-05 20:58:14.667000, contains telemetry from sessions 1968 to 1969.
    # The session starts on 2019-10-05 22:15:52+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(46, '/telemetry.current', [1031, 1081, 1131, 1181, 1231, 1056, 1106, 1156, 1206, 1044, 1094, 1144, 1194, 1244, 1068, 1118, 1168, 1218, 1038, 1088]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1138, 1188, 1238, 1050, 1100, 1150, 1200, 1062, 1112, 1162, 1212, 1074, 1124, 1174, 1224]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [190, 202, 214, 240, 252, 264, 290, 302, 314, 340, 352, 364, 390, 402, 414, 440]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [452, 464, 490, 502, 514, 540, 552, 564, 578, 590, 602, 614, 628, 640, 652, 664]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [678, 690, 702, 714, 728, 740, 752, 764, 778, 790, 802, 814, 828, 840, 852, 864]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [878, 890, 902, 914, 928, 940, 952, 964, 978, 990, 1002, 1014, 1028, 1040, 1052]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=3), 5, datetime.timedelta(seconds=10), 'suns_ps_15'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=80), 't02w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(104, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't02n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=80), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(107, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=7), 't04w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(108, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't04n_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(34, '/p2_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(35, '/p2_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p2_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p2_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p2_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p1_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p1_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p1_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p1_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p1_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],
    # missing from previous session end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]