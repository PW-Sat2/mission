tasks = [
    # Generated on 2021-02-18 22:04:14.357621, contains telemetry from sessions 5180 to 5181.
    # The session starts on 2021-02-18 23:05:49+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.current', [496, 546, 596, 646, 696, 521, 571, 621, 671, 509, 559, 609, 659, 533, 583, 633, 683, 503, 553, 603]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [653, 703, 515, 565, 615, 665, 527, 577, 627, 677, 539, 589, 639, 689]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [22, 41, 47, 72, 91, 97, 122, 141, 147, 172, 191, 197, 222, 241, 247]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [253, 259, 272, 297, 303, 322, 347, 353, 372, 397, 409, 422, 447, 472, 522]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1809, 1821, 1827, 1877, 1883, 1889, 1927, 1939, 1989, 2009, 2039, 2059, 2089, 2095]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2102, 2109, 2139, 2145, 2152, 2159, 2189, 2195, 2202, 2209, 2239, 2245, 2252, 2259]), Send, WaitMode.Wait],
    # missing from previous session end

    [tc.DownloadFile(100, '/n01w', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/n01w', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/n01w', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/n01w', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/n01w', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/n01w', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/n01w', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/n01w', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/n01w', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],


    [tc.DownloadFile(110, '/n01n', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/n01n', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/n01n', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/n01n', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/n01n', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/n01n', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/n01n', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/n01n', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/n01n', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],


    [tc.DownloadFile(120, '/n02w', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/n02w', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/n02w', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/n02w', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/n02w', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/n02w', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/n02w', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/n02w', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/n02w', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],


    [tc.DownloadFile(130, '/n02n', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/n02n', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/n02n', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/n02n', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/n02n', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/n02n', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/n02n', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/n02n', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/n02n', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
