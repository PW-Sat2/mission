tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 83 and 84
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(1170, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(1182, 1370, 25)]), Send, WaitMode.Wait],

    # Delete photos
    [tc.RemoveFile(5, '/p7_480_0'), Send, WaitMode.NoWait],
    # Remove old RadFET exp
    [tc.RemoveFile(6, '/radfet_2'), Send, WaitMode.NoWait],
    [tc.RemoveFile(7, '/radfet_3'), Send, WaitMode.NoWait],
    # Remove downloaded suns exp data
    [tc.RemoveFile(8, '/suns_4'), Send, WaitMode.NoWait],

    [tc.ListFiles(9, '/'), Send, WaitMode.Wait],

    # Missing Suns exp secondary file download
    [tc.DownloadFile(10, '/suns_4_sec', [16]), Send, WaitMode.Wait],

    # More telemetry between session 83 and 84
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(1176, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(1188, 1370, 25)]), Send, WaitMode.Wait],

    # Much more telemetry between session 83 and 84
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1171, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1172, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1173, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1174, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1175, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1177, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1178, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1179, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1180, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1181, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(1183, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1184, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1185, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1186, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1187, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1189, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1190, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1191, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1192, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1193, 1370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(1194, 1370, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
