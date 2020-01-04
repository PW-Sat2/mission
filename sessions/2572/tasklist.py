tasks = [
    # Generated on 2020-01-04 20:28:04.633000, contains telemetry from sessions 2571 to 2572.
    # The session starts on 2020-01-04 21:45:24+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [6, 56, 106, 156, 206, 31, 81, 131, 181, 19, 69, 119, 169, 219, 43, 93, 143, 193, 13, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [113, 163, 213, 25, 75, 125, 175, 37, 87, 137, 187, 49, 99, 149, 199]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(7, '/radfet_29', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],


    [tc.DownloadFile(40, '/p01w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p01n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p02w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p02n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p03w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p03n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p04w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p04n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p05w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p05n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p06w_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p06n_480_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/p01w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p01n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p02w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p02n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p03w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p03n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p04w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p04n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p05w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p05n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p06w_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p06n_480_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/p01w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p01n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p02w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p02n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p03w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p03n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p04w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p04n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p05w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p05n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p06w_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p06n_480_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(76, '/p01w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p01n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/p02w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/p02n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/p03w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p03n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p04w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p04n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p05w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p05n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p06w_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/p06n_480_0', range(60, 80)), Send, WaitMode.Wait],

    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]