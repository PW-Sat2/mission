tasks = [
    # Generated on 2021-02-05 21:32:05.097000, contains telemetry from sessions 5107 to 5108.
    # The session starts on 2021-02-05 22:51:05+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # photos - aiming for terminator
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=14), 'p0_w_p480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p0_n_p480'), Send, WaitMode.Wait],
   
    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1732, 1782, 1832, 1882, 1932, 1757, 1807, 1857, 1907, 1745, 1795, 1845, 1895, 1945, 1769, 1819, 1869, 1919, 1739, 1789]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1839, 1889, 1939, 1751, 1801, 1851, 1901, 1763, 1813, 1863, 1913, 1775, 1825, 1875, 1925]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]