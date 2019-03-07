tasks = [
    # Generated on 2019-03-07 21:18:23.656000, contains telemetry from sessions 611 to 612.
    # The session starts on 2019-03-07 22:36:45+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missings from session 611
    [tc.DownloadFile(30, '/telemetry.previous', [221, 233, 283, 321, 333, 371, 383,
                                                 433, 471, 483, 521, 533, 571, 583, 633, 683, 733]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [783, 833, 883, 933, 983, 1033, 1083,
                                                 1133, 1183, 1233, 1259, 1271, 1283, 1333, 1383, 1433]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1483, 1533, 1583, 1621, 1633, 1659,
                                                 1671, 1683, 1721, 1733, 1759, 1771, 1783, 1821, 1833, 1871]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1883, 1921, 1933, 1971, 1983, 2021,
                                                 2033, 2071, 2083, 2121, 2133, 2171, 2183, 2221, 2233, 2271]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [3, 41, 53, 79, 91, 103, 129,
                                                141, 153, 179, 191, 203, 229, 241, 253, 279, 291]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [303, 329, 341, 353, 379, 391, 403,
                                                429, 441, 453, 479, 491, 503, 529, 541, 553, 579]), Send, WaitMode.Wait],


    # auto-generated telemetry start
    [tc.DownloadFile(40, '/telemetry.current', [550, 600, 650, 700, 750, 575, 625, 675,
                                                725, 563, 613, 663, 713, 763, 587, 637, 687, 737, 557, 607]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [657, 707, 757, 569, 619, 669,
                                                719, 769, 581, 631, 681, 731, 593, 643, 693, 743]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
