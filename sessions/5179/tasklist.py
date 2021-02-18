tasks = [
    # Generated on 2021-02-18 14:00:15.929000, contains telemetry from sessions 5178 to 5179.
    # The session starts on 2021-02-18 14:16:21+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/p5174_1_w_p480_0', [149]), Send, WaitMode.Wait],
    # missing from previous session end

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1802, 1852, 1902, 1952, 2002, 1827, 1877, 1927, 1977, 1815, 1865, 1915, 1965, 2015, 1839, 1889, 1939, 1989, 1809, 1859]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1909, 1959, 2009, 1821, 1871, 1921, 1971, 1833, 1883, 1933, 1983, 1845, 1895, 1945, 1995]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]