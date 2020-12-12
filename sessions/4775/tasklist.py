tasks = [
    # Generated on 2020-12-12 12:22:13.534000, contains telemetry from sessions 4774 to 4775.
    # The session starts on 2020-12-12 13:34:04+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [168, 218, 268, 318, 368, 193, 243, 293, 343, 181, 231, 281, 331, 381, 205, 255, 305, 355, 175, 225]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [275, 325, 375, 187, 237, 287, 337, 387, 199, 249, 299, 349, 211, 261, 311, 361]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.TakePhotoTelecommand(33, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'b_n_p480_3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(34, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'b_w_p480_3'), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/b_n_p480_0_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/b_n_p480_0_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/b_n_p480_0_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],

    [tc.ListFiles(48, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(37, '/b_w_p480_0_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/b_w_p480_0_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/b_w_p480_0_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/b_w_p480_0_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/b_w_p480_1_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/b_w_p480_1_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/b_w_p480_1_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/b_w_p480_1_0', [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/b_w_p480_1_0', [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],


    [tc.DownloadFile(61, '/b_n_p480_1_0', [80]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/b_w_p480_2_0', [80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],

    [tc.DownloadFile(71, '/b_n_p480_2_0', [80, 81, 82, 83]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]