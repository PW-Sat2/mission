tasks = [
    # Generated on 2021-02-11 22:36:25.067000, contains telemetry from sessions 5142 to 5143.
    # The session starts on 2021-02-11 23:49:11+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(38, '/telemetry.current', [1644, 1694, 1744, 1794, 1844, 1669, 1719, 1769, 1819, 1657, 1707, 1757, 1807, 1857, 1681, 1731, 1781, 1831, 1651, 1701]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1751, 1801, 1851, 1663, 1713, 1763, 1813, 1675, 1725, 1775, 1825, 1687, 1737, 1787, 1837]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t02n_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t02n_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t02n_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t02n_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t02n_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    # missing from previous session end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated file download start
    # auto-generated file download end

    [tc.RemoveFile(104, '/photo01n_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(105, '/photo01w_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(106, '/photo02n_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(107, '/photo02w_0'), Send, WaitMode.NoWait],
    # auto-generated file remove start
        
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated file download start
    [tc.RemoveFile(100, '/t01w_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/t01n_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(102, '/t02w_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/t02n_0'), Send, WaitMode.NoWait],
    # auto-generated file remove end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]