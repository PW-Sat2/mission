tasks = [
    # Generated on 2019-10-12 11:53:51.638000, contains telemetry from sessions 2014 to 2015.
    # The session starts on 2019-10-12 12:50:00+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1454, 1504, 1554, 1604, 1654, 1479, 1529, 1579, 1629, 1467, 1517, 1567, 1617, 1667, 1491, 1541, 1591, 1641, 1461, 1511]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1561, 1611, 1661, 1473, 1523, 1573, 1623, 1673, 1485, 1535, 1585, 1635, 1497, 1547, 1597, 1647]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [396]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]