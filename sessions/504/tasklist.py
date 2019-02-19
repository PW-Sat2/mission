tasks = [
    # Generated on 2019-02-19 20:06:19.466000, contains telemetry from sessions 503 to 504.
    # The session starts on 2019-02-19 21:24:41+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1666, 1716, 1766, 1816, 1866, 1691, 1741, 1791, 1841, 1679, 1729, 1779, 1829, 1879, 1703, 1753, 1803, 1853, 1673, 1723]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1773, 1823, 1873, 1685, 1735, 1785, 1835, 1885, 1697, 1747, 1797, 1847, 1709, 1759, 1809, 1859]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(41, '/telemetry.previous', [1605, 1705, 1955, 2105, 2205]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [49, 99, 149, 199, 249, 275, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1463, 1499, 1513, 1549, 1563, 1599, 1649, 1699]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]