tasks = [
    # Generated on 2021-02-04 11:24:45.434000, contains telemetry from sessions 5098 to 5099.
    # The session starts on 2021-02-04 11:39:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(44, '/telemetry.current', [157, 207, 257, 307, 357, 182, 232, 282, 332, 170, 220, 270, 320, 194, 244, 294, 344, 164, 214, 264]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [314, 364, 176, 226, 276, 326, 188, 238, 288, 338, 200, 250, 300, 350]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [137, 149, 212, 262, 312, 319, 769, 881, 1042, 1049, 1055, 1061, 1067, 1073, 1079, 1085, 1092, 1099, 1105]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1111, 1117, 1123, 1129, 1135, 1142, 1149, 1155, 1161, 1167, 1173, 1179, 1185, 1192, 1199, 1211, 1217, 1223, 1224]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1229, 1235, 1236, 1248, 1249, 1274, 1286, 1298, 1312, 1324, 1336, 1348, 1362, 1374, 1386, 1398, 1412, 1424]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/wro_n_p480_21_45_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/wro_n_p480_21_45_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/wro_n_p480_21_45_0', [167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/wro_n_p480_22_24_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/wro_n_p480_22_24_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/wro_n_p480_22_24_0', [167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/wro_w_p480_21_45_0', [140, 144, 147, 150, 156, 157, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/wro_w_p480_21_45_0', [167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/wro_w_p480_22_24_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/wro_w_p480_22_24_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/wro_w_p480_22_24_0', [167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]