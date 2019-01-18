tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.RemoveFile(3, '/p3_480_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1938, 1988, 2038, 2088, 2138, 1963, 2013, 2063, 2113, 1951, 2001, 2051, 2101, 2151, 1975, 2025, 2075, 2125, 1945, 1995]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2045, 2095, 2145, 1957, 2007, 2057, 2107, 2157, 1969, 2019, 2069, 2119, 1981, 2031, 2081, 2131]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]