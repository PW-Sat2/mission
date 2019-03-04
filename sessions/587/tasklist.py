tasks = [
    # Generated on 2019-03-04 10:23:31.281000, contains telemetry from sessions 586 to 587.
    # The session starts on 2019-03-04 11:29:17+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(10, '/telemetry.current', [562, 612, 662, 712, 762, 587, 637, 687, 737, 575, 625, 675, 725, 775, 599, 649, 699, 749, 569, 619]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [669, 719, 769, 581, 631, 681, 731, 781, 593, 643, 693, 743, 605, 655, 705, 755]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # SunS suns_ps_2 experiment file download
    [tc.DownloadFile(21, '/suns_ps_2', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/suns_ps_2', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/suns_ps_2', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/suns_ps_2', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/suns_ps_2', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_ps_2', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/suns_ps_2', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_ps_2', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_ps_2', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/suns_ps_2', [i for i in range(180, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_2', [i for i in range(200, 220, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_2', [i for i in range(220, 240, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_2', [i for i in range(240, 250, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]