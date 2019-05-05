tasks = [
    # Generated on 2019-05-05 23:27:53.276763, contains telemetry from sessions 1007 to 1008.
    # The session starts on 2019-05-05 23:47:09+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(48, '/telemetry.current', [1571, 1621, 1671, 1721, 1771, 1596, 1646, 1696, 1746, 1584, 1634, 1684, 1734, 1784, 1608, 1658, 1708, 1758, 1578, 1628]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1678, 1728, 1778, 1590, 1640, 1690, 1740, 1790, 1602, 1652, 1702, 1752, 1614, 1664, 1714, 1764]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(36, '/p5_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p4_480_0', [1, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p4_480_0', [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p4_480_0', [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p4_480_0', [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 86, 107, 113, 114, 115]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p4_480_0', [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p4_480_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p7_480_0', [48, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p7_480_0', [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p7_480_0', [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p7_480_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p7_480_0', [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
