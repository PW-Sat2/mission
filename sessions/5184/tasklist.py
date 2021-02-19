tasks = [
    # Generated on 2021-02-19 12:56:33.801000, contains telemetry from sessions 5183 to 5184.
    # The session starts on 2021-02-19 13:10:26+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(42, '/telemetry.current', [2033, 2083, 2133, 2183, 2233, 2058, 2108, 2158, 2208, 2046, 2096, 2146, 2196, 2246, 2070, 2120, 2170, 2220, 2040, 2090]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [2140, 2190, 2240, 2052, 2102, 2152, 2202, 2064, 2114, 2164, 2214, 2076, 2126, 2176, 2226]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [832, 875, 882, 900, 932, 950, 1050, 1138, 1275, 1294, 1325, 1344, 1362, 1375, 1388, 1394]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1412, 1425, 1438, 1462, 1475, 1488, 1506, 1512, 1525, 1538, 1556, 1562, 1575, 1588, 1606, 1625]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1638, 1650, 1656, 1675, 1688, 1738, 1788, 1800, 1825, 1832, 1850, 1900, 1906, 1982, 2000]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/n02w_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/n01w_0', [62, 63, 64, 81, 82, 83, 84, 97, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/n02n_0', [76, 80, 81, 100, 102, 104, 105, 110, 111, 112, 113, 129, 130, 131, 132, 133]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/n02n_0', [134, 135, 137, 138, 139, 140, 141, 144, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/n02n_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/n02w_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/n02w_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/n02w_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/n02w_0', [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]