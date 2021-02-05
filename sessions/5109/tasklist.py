tasks = [
    # Generated on 2021-02-05 23:08:10.628000, contains telemetry from sessions 5108 to 5109.
    # The session starts on 2021-02-06 00:25:06+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1893, 1943, 1993, 2043, 2093, 1918, 1968, 2018, 2068, 1906, 1956, 2006, 2056, 2106, 1930, 1980, 2030, 2080, 1900, 1950]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2000, 2050, 2100, 1912, 1962, 2012, 2062, 2112, 1924, 1974, 2024, 2074, 1936, 1986, 2036, 2086]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Try to download the photos without knowing sizes
    [tc.DownloadFile(42, '/p0_w_p480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p0_w_p480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p0_w_p480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p0_w_p480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p0_w_p480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p0_w_p480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p0_w_p480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p0_w_p480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p0_w_p480_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p0_w_p480_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(47, '/p0_n_p480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p0_n_p480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p0_n_p480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p0_n_p480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p0_n_p480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p0_n_p480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p0_n_p480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p0_n_p480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p0_n_p480_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p0_n_p480_0', range(180, 200)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]