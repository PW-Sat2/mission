tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1207, 1257, 1307, 1357, 1407, 1232, 1282, 1332, 1382, 1220, 1270, 1320, 1370, 1420, 1244, 1294, 1344, 1394, 1214, 1264]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1314, 1364, 1414, 1226, 1276, 1326, 1376, 1426, 1238, 1288, 1338, 1388, 1250, 1300, 1350, 1400]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]