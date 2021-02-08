tasks = [
    # Generated on 2021-02-08 13:23:54.282000, contains telemetry from sessions 5123 to 5124.
    # The session starts on 2021-02-08 21:53:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=17), 'l01w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'l01n'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'l02w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'l02n'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1870, 1920, 1970]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 2, 52, 102, 152, 202, 252, 302, 352]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [402, 452, 502, 552, 602, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 14, 64, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2020, 2070, 2120, 2170, 2220, 2270, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1864, 1914, 1964, 2014, 2064, 2114]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [164, 214, 264, 314, 364, 414, 464, 514, 564, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2164, 2214, 2264, 1876, 1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [584, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 8, 58, 108, 158, 208, 258, 308]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [358, 408, 458, 508, 558, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]