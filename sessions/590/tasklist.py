tasks = [
    # Generated on 2019-03-04 13:14:34.721915, contains telemetry from sessions 587 to 590.
    # The session starts on 2019-03-04 20:47:41+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1732, 1782, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1657, 1707, 1757, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 1445, 1495, 1545]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1595, 1645, 1695, 1745, 1795, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1519, 1569, 1619, 1669, 1719, 1769, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 1189, 1239, 1289, 1339, 1389]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1439, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # SunS missings from session 587
    [tc.DownloadFile(30, '/suns_ps_2', [0, 17, 33, 34, 36, 67, 94, 108, 136, 145, 146, 147, 149, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_2', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_2', [178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_2', [196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_2', [214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_2', [232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
