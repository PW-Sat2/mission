tasks = [
    # Generated on 2020-05-30 12:51:29.780000, contains telemetry from sessions 3527 to 3528.
    # The session starts on 2020-05-30 13:44:46+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [185, 235, 285, 335, 385, 210, 260, 310, 360, 198, 248, 298, 348, 398, 222, 272, 322, 372, 192, 242]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [292, 342, 392, 204, 254, 304, 354, 404, 216, 266, 316, 366, 228, 278, 328, 378]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(34, '/a1n_480_12_16_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a1n_480_12_16_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a1n_480_12_16_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a1n_480_12_16_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a1n_480_12_16_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a1n_480_12_16_0', [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a2n_480_12_17_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a2n_480_12_17_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a2n_480_12_17_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a2n_480_12_17_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a2n_480_12_17_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a2n_480_12_17_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a3n_480_12_18_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a3n_480_12_18_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a3n_480_12_18_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a3n_480_12_18_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a3n_480_12_18_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a3n_480_12_18_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a3n_480_12_18_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a3w_480_12_18_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a3w_480_12_18_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a3w_480_12_18_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a3w_480_12_18_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a3w_480_12_18_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a3w_480_12_18_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    # auto-generated file download end


    [tc.DownloadFile(60, '/a4w_480_12_19_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a4n_480_12_19_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a5w_480_12_20_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a5n_480_12_20_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a6w_480_12_21_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a6n_480_12_21_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/a7w_480_12_22_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/a7n_480_12_22_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/a8w_480_12_23_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/a8n_480_12_23_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/a9w_480_12_24_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/a9n_480_12_24_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/a10w_480_12_25_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/a10n_480_12_25_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(74, '/a4w_480_12_19_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/a4n_480_12_19_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/a5w_480_12_20_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/a5n_480_12_20_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/a6w_480_12_21_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/a6n_480_12_21_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/a7w_480_12_22_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/a7n_480_12_22_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/a8w_480_12_23_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/a8n_480_12_23_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/a9w_480_12_24_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/a9n_480_12_24_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/a10w_480_12_25_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/a10n_480_12_25_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(88, '/a4w_480_12_19_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/a4n_480_12_19_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/a5w_480_12_20_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/a5n_480_12_20_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/a6w_480_12_21_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/a6n_480_12_21_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/a7w_480_12_22_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/a7n_480_12_22_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/a8w_480_12_23_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/a8n_480_12_23_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/a9w_480_12_24_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/a9n_480_12_24_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/a10w_480_12_25_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/a10n_480_12_25_0', range(40, 60)), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]