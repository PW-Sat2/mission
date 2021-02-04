tasks = [
    # Generated on 2021-02-04 22:43:10.002946, contains telemetry from sessions 5102 to 5103.
    # The session starts on 2021-02-04 23:42:12+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1466, 1516, 1566, 1616, 1666, 1491, 1541, 1591, 1641, 1479, 1529, 1579, 1629, 1679, 1503, 1553, 1603, 1653, 1473, 1523]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1573, 1623, 1673, 1485, 1535, 1585, 1635, 1497, 1547, 1597, 1647, 1509, 1559, 1609, 1659]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
