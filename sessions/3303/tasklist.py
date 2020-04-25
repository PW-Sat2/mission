tasks = [
    # Generated on 2020-04-25 20:54:29.844000, contains telemetry from sessions 3302 to 3303.
    # The session starts on 2020-04-25 22:06:41+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(75, '/telemetry.current', [1024, 1074, 1124, 1174, 1224, 1049, 1099, 1149, 1199, 1037, 1087, 1137, 1187, 1237, 1061, 1111, 1161, 1211, 1031, 1081]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [1131, 1181, 1231, 1043, 1093, 1143, 1193, 1055, 1105, 1155, 1205, 1067, 1117, 1167, 1217]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(77, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=17), 'a1w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(78, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a1n_480'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/t1n_480_0', [30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t1n_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t1n_480_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t1n_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t1n_480_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t1n_480_0', [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t2n_480_0', [20, 21, 22, 24, 26, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t2n_480_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t2n_480_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t2n_480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t2n_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t2n_480_0', [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t2n_480_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t3n_480_0', [1, 27, 28, 29, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t3n_480_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t3n_480_0', [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t3n_480_0', [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t3n_480_0', [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t3w_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t3w_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t3w_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t4n_480_0', [20, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t4n_480_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t4n_480_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t4n_480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t4n_480_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t4n_480_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t4n_480_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t4w_480_0', [20, 32, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t4w_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t4w_480_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t4w_480_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t4w_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t5n_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t5n_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t5n_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t5n_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t5n_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t5w_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t5w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t5w_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t5w_480_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t5w_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t5w_480_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t5w_480_0', [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]