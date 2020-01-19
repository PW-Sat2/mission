tasks = [
    # Generated on 2020-01-19 20:56:37.002171, contains telemetry from sessions 2670 to 2671.
    # The session starts on 2020-01-19 22:12:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1371, 1421, 1471, 1521, 1571, 1396, 1446, 1496, 1546, 1384, 1434, 1484, 1534, 1584, 1408, 1458, 1508, 1558, 1378, 1428]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1478, 1528, 1578, 1390, 1440, 1490, 1540, 1590, 1402, 1452, 1502, 1552, 1414, 1464, 1514, 1564]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]