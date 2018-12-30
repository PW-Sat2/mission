tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 163 and 164
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(920, 1120, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(926, 1120, 12)]), Send, WaitMode.Wait],

    # Low-res photos just before and after sail deployment
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/sail.photo_73', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/sail.photo_75', [i for i in range(0, 21, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/sail.photo_77', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/sail.photo_77', [i for i in range(15, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/sail.photo_79', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/sail.photo_79', [i for i in range(15, 27, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/sail.photo_81', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/sail.photo_81', [i for i in range(15, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/sail.photo_83', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/sail.photo_83', [i for i in range(16, 33, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/sail.photo_85', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/sail.photo_85', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 161 and 163
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(6, 920, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(18, 920, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(31, 920, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(43, 920, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(106, '/telemetry.previous', [i for i in range(1936, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [i for i in range(1948, 2280, 25)]), Send, WaitMode.Wait],

    # Missing telemetry
    [tc.DownloadFile(200, '/telemetry.previous', [i for i in range(1949, 2189, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.previous', [i for i in range(1961, 2189, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.previous', [i for i in range(1973, 2189, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.previous', [i for i in range(1985, 2189, 48)]), Send, WaitMode.Wait],

    # Remove donwloaded photos
    [tc.RemoveFile(31, '/sail.photo_31'), Send, WaitMode.NoWait],
    [tc.RemoveFile(33, '/sail.photo_33'), Send, WaitMode.NoWait],
    [tc.RemoveFile(37, '/sail.photo_37'), Send, WaitMode.NoWait],
    [tc.RemoveFile(39, '/sail.photo_39'), Send, WaitMode.NoWait],
    [tc.RemoveFile(41, '/sail.photo_41'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, '/sail.photo_43'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(59, '/sail.photo_59'), Send, WaitMode.NoWait],
    [tc.RemoveFile(61, '/sail.photo_61'), Send, WaitMode.NoWait],
    [tc.RemoveFile(63, '/sail.photo_63'), Send, WaitMode.NoWait],
    [tc.RemoveFile(65, '/sail.photo_65'), Send, WaitMode.NoWait],
    [tc.RemoveFile(69, '/sail.photo_69'), Send, WaitMode.NoWait],
    [tc.RemoveFile(71, '/sail.photo_71'), Send, WaitMode.NoWait],
    [tc.RemoveFile(87, '/sail.photo_87'), Send, WaitMode.NoWait],

    # Low-res photos before sail deployment
    [tc.DownloadFile(1, '/sail.photo_1', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(3, '/sail.photo_3', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/sail.photo_5', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(7, '/sail.photo_7', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(9, '/sail.photo_9', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]