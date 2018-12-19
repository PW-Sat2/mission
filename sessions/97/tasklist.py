tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between sessions 96 and 97
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1890, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1902, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1896, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1908, 2090, 25)]), Send, WaitMode.Wait],

    # Remove downloaded files
    [tc.RemoveFile(20, '/radfet_4'), Send, WaitMode.Wait],
    [tc.RemoveFile(21, '/suns_5'), Send, WaitMode.Wait],
    [tc.RemoveFile(22, '/suns_5_sec'), Send, WaitMode.Wait],

    # More telemetry between sessions 96 and 97
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1893, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(1899, 2090, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1905, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(1911, 2090, 25)]), Send, WaitMode.Wait],

    # Much more telemetry between sessions 96 and 97
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1891, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1892, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1894, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1895, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1897, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1898, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1900, 2090, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1901, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(1903, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(1904, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(1906, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(1907, 2090, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(1909, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(1910, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(1912, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(1913, 2090, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(1914, 2090, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
