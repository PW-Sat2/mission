tasks = [
    # Generated on 2021-02-07 12:31:54.127000, contains telemetry from sessions 5117 to 5118.
    # The session starts on 2021-02-07 13:47:37+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1432, 1482, 1532, 1582, 1632, 1457, 1507, 1557, 1607, 1445, 1495, 1545, 1595, 1645, 1469, 1519, 1569, 1619, 1439, 1489]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1539, 1589, 1639, 1451, 1501, 1551, 1601, 1463, 1513, 1563, 1613, 1475, 1525, 1575, 1625]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]