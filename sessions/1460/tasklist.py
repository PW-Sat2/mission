tasks = [
    # Generated on 2019-06-28 22:47:34.288000.
    # The session starts on 2019-06-29 11:17:49+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is Purge Photo.", Print, WaitMode.Wait],
    [tc.PurgePhotoTelecommand(11), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [12, 62, 112, 162, 212, 37, 87, 137, 187, 25, 75, 125, 175, 225, 49, 99, 149, 199, 19, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [119, 169, 219, 31, 81, 131, 181, 231, 43, 93, 143, 193, 55, 105, 155, 205]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1
    [tc.TakePhotoTelecommand(81, CameraLocation.Wing, PhotoResolution.p128, 29, datetime.timedelta(minutes=0), 'p52_128'), Send, WaitMode.Wait],

    # =========================================

    # Low and mid res photos download

    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p15_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p20_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p25_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p30_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p35_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p40_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p45_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p50_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(201, '/p52_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/p52_128_5', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/p52_128_10', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/p52_128_15', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/p52_128_20', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(206, '/p52_128_25', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]