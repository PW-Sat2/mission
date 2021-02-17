tasks = [
    # Generated on 2021-02-17 12:41:26.517090, contains telemetry from sessions 5172 to 5173.
    # The session starts on 2021-02-17 13:46:53+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [1395, 1445, 1495, 1545, 1595, 1420, 1470, 1520, 1570, 1408, 1458, 1508, 1558, 1608, 1432, 1482, 1532, 1582, 1402, 1452]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1502, 1552, 1602, 1414, 1464, 1514, 1564, 1426, 1476, 1526, 1576, 1438, 1488, 1538, 1588]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [78, 84, 240, 360, 703, 716, 928, 990, 1134, 1140, 1146, 1178, 1184, 1190, 1196, 1237, 1261]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p1_w_p480_0', [22, 53, 54, 58, 59]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]