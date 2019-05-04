tasks = [
    # Generated on 2019-05-04 22:36:42.424000, contains telemetry from sessions 1001 to 1002.
    # The session starts on 2019-05-04 23:44:28+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1208, 1258, 1308, 1358, 1408, 1233, 1283, 1333, 1383, 1221, 1271, 1321, 1371, 1421, 1245, 1295, 1345, 1395, 1215, 1265]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1315, 1365, 1415, 1227, 1277, 1327, 1377, 1427, 1239, 1289, 1339, 1389, 1251, 1301, 1351, 1401]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Radfet download
    [tc.DownloadFile(40, '/radfet_12', range(0, 8)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/radfet_12', range(8, 16)), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(50, '/p5_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/p8_128_0', [24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/p9_128_0', [25]), Send, WaitMode.Wait],
    # missing from previous session end

    #big photo
    [tc.DownloadFile(60, '/p9_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p9_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p9_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p9_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p9_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],

    # this one does't have chances to be downloaded, but...
    [tc.DownloadFile(65, '/p3_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p3_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p3_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p3_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p3_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p3_480_0', [90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]