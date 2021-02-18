tasks = [
    # Generated on 2021-02-18 21:23:43.780000, contains telemetry from sessions 5178 to 5180.
    # The session starts on 2021-02-18 21:36:24+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p5174_1_w_p480_0', [149]), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=25), 'n01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n02n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=25), 'n01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n02n'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 47, 97, 147, 197, 247, 297, 347, 397, 447]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [497, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 9, 59, 109, 159, 209, 259, 309, 359]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1809]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [409, 459, 509, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 41, 91, 141, 191, 241, 291]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1833]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [341, 391, 441, 491, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 15, 65, 115, 165, 215]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [265, 315, 365, 415, 465, 515]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
