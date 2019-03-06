tasks = [
    # Generated on 2019-03-06 08:24:36.032000, contains telemetry from sessions 597 to 600.
    # The session starts on 2019-03-06 10:02:26+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2109, 2159, 2209, 2259, 2134, 2184, 2234, 2122, 2172, 2222, 2272, 2146, 2196, 2246, 2116, 2166, 2216, 2266, 2128, 2178]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1029, 1079, 1129, 1179, 1229, 1279, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 604, 654]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 42, 92, 142, 192, 242, 292, 342]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1066, 1116, 1166, 1216, 1266, 1316, 36, 86, 136, 186, 236, 286, 336, 386, 436, 486, 536, 586, 636, 686]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286, 48, 98, 148, 198, 248, 298, 348, 398]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2228, 2278, 2140, 2190, 2240, 2152, 2202, 2252]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198, 1248, 1298, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1110, 1160, 1210, 1260, 1310, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]