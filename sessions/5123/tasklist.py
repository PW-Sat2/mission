tasks = [
    # Generated on 2021-02-08 11:40:00.343495, contains telemetry from sessions 5122 to 5123.
    # The session starts on 2021-02-08 12:56:25+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1690, 1740, 1790, 1840, 1890, 1715, 1765, 1815, 1865, 1703, 1753, 1803, 1853, 1903, 1727, 1777, 1827, 1877, 1697, 1747]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1797, 1847, 1897, 1709, 1759, 1809, 1859, 1721, 1771, 1821, 1871, 1733, 1783, 1833, 1883]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [803, 1003, 1053, 1103, 1153, 1203]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]