tasks = [
    # Generated on 2019-02-09 20:57:03.118000, contains telemetry from sessions 438 to 439.
    # also missings from session 438
    # The session starts on 2019-02-09 22:13:33+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],


    [tc.DownloadFile(30, '/telemetry.previous', [184, 190, 202, 214, 234, 240, 252, 264, 284, 290, 302, 314, 334, 340, 352, 364, 384, 390, 402, 414]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1152, 1164, 1190, 1202, 1214, 1240, 1252, 1264, 1290, 1302, 1314, 1340, 1352, 1364, 1390, 1402, 1414, 1440, 1452]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(32, '/telemetry.previous', [434, 440, 452, 464, 484, 490, 502, 514, 534, 540, 552, 564, 584, 590, 602, 614, 634, 640, 652, 664]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1464, 1478, 1490, 1502, 1514, 1540, 1552, 1564, 1590, 1602, 1614, 1640, 1652, 1664, 1690, 1702, 1714, 1740, 1752]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(34, '/telemetry.previous', [684, 690, 702, 714, 728, 734, 740, 752, 764, 784, 790, 802, 814, 828, 834, 840, 852, 864, 884]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1764, 1790, 1802, 1814, 1828, 1840, 1852, 1864, 1890, 1902, 1914, 1928, 1940, 1952, 1964, 1990, 2002, 2014, 2040]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(36, '/telemetry.previous', [890, 902, 914, 940, 952, 964, 978, 990, 1002, 1014, 1040, 1052, 1064, 1078, 1090, 1102, 1114, 1128, 1140]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2046, 2052, 2064, 2090, 2096, 2102, 2114, 2140, 2146, 2152, 2164, 2190, 2196, 2202, 2214, 2240, 2246, 2252, 2264]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(38, '/telemetry.current', [528, 578, 628, 678, 728, 553, 603, 653, 703, 541, 591, 641, 691, 741, 565, 615, 665, 715, 535, 585]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [635, 685, 735, 547, 597, 647, 697, 747, 559, 609, 659, 709, 571, 621, 671, 721]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    [tc.DownloadFile(40, '/telemetry.current', [22, 34, 72, 84, 122, 134, 160, 172, 184, 210, 222, 234, 260, 272, 284, 310, 322]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [334, 354, 360, 372, 384, 410, 422, 434, 460, 472, 484, 504, 510, 522, 534, 560]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]