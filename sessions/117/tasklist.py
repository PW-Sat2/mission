tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # ReadMemory, weird telecommand
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # Telemetry between session 116 and 117
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(650, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(675, 1650, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(662, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(687, 1650, 50)]), Send, WaitMode.Wait],

    # =========================================
    # TakePhoto queue over USA - start at 19:33
    # Group 1
    [tc.TakePhotoTelecommand(40, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=27), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(41, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(42, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(43, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(44, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(45, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(46, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(47, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(48, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(49, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(50, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(51, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(52, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(53, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(54, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(55, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(56, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(57, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(58, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(59, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],
    # =========================================
    
    # suns_7 missings download
    [tc.DownloadFile(60, '/suns_7', [45, 48, 64, 65, 67, 137, 159, 178, 179, 250, 496, 500, 513, 522, 559, 560, 563, 564]), Send, WaitMode.Wait],

    # More telemetry between session 116 and 117
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(656, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(668, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(681, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(693, 1650, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(653, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(659, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(665, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(671, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(678, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(684, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(690, 1650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(696, 1650, 50)]), Send, WaitMode.Wait],

    # suns_7_sec missings download
    [tc.DownloadFile(91, '/suns_7_sec', [0, 1, 4, 5, 29, 40, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/suns_7_sec', [57, 58, 60, 61, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81]), Send, WaitMode.Wait], 
    [tc.DownloadFile(93, '/suns_7_sec', [84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 97, 98, 99, 100, 103, 104, 105]), Send, WaitMode.Wait], 
    [tc.DownloadFile(94, '/suns_7_sec', [106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]), Send, WaitMode.Wait], 
    [tc.DownloadFile(95, '/suns_7_sec', [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait], 
    [tc.DownloadFile(96, '/suns_7_sec', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait], 
    [tc.DownloadFile(97, '/suns_7_sec', [151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait], 
    [tc.DownloadFile(98, '/suns_7_sec', [166, 167, 168, 169, 170, 171, 174, 177, 178, 179, 180, 181, 182, 183, 184]), Send, WaitMode.Wait], 
    [tc.DownloadFile(99, '/suns_7_sec', [185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]), Send, WaitMode.Wait], 
    [tc.DownloadFile(100, '/suns_7_sec', [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214]), Send, WaitMode.Wait], 
    [tc.DownloadFile(101, '/suns_7_sec', [215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/suns_7_sec', [230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244]), Send, WaitMode.Wait], 
    [tc.DownloadFile(103, '/suns_7_sec', [245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259]), Send, WaitMode.Wait], 
    [tc.DownloadFile(104, '/suns_7_sec', [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/suns_7_sec', [275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/suns_7_sec', [290, 291, 292, 293, 294, 295, 296]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]