tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(30, '/telemetry.previous', [1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1197, 1247, 1297, 1347, 1397]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1447, 1497, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1203, 1253, 1303, 1353]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1403, 1453, 1503, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1227, 1277, 1327, 1377, 1427, 1477, 1527]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [96, 146, 196, 246, 296, 121, 171, 221, 271, 109, 159, 209, 259, 309, 133, 183, 233, 283, 103, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [203, 253, 303, 115, 165, 215, 265, 315, 127, 177, 227, 277, 139, 189, 239, 289]), Send, WaitMode.Wait],
    
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
