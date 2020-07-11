tasks = [
            # Generated on 2020-07-11 12:43:48.181000, contains telemetry from sessions 3796 to 3797.
            # The session starts on 2020-07-11 13:56:43+02:00.

            [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

            [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

            [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

            [tc.SendBeacon(), Send, WaitMode.Wait],

            # auto-generated telemetry start
            [tc.DownloadFile(31, '/telemetry.current', [1, 51, 101, 151, 201, 26, 76, 126, 176, 14, 64, 114, 164, 214, 38, 88, 138, 188, 8, 58]), Send, WaitMode.Wait],
            [tc.DownloadFile(32, '/telemetry.current', [108, 158, 208, 20, 70, 120, 170, 220, 32, 82, 132, 182, 44, 94, 144, 194]), Send, WaitMode.Wait],
        # auto-generated telemetry end


        # auto-generated file download start
        [tc.DownloadFile(33, '/a_w_12_28_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
        [tc.DownloadFile(34, '/a_w_12_28_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
        [tc.DownloadFile(35, '/a_w_12_28_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
        [tc.DownloadFile(36, '/a_w_12_28_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
        [tc.DownloadFile(37, '/a_w_12_28_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
        [tc.DownloadFile(38, '/a_w_12_28_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
        [tc.DownloadFile(39, '/a_n_12_28_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
        [tc.DownloadFile(40, '/a_n_12_28_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
        [tc.DownloadFile(41, '/a_n_12_28_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
        [tc.DownloadFile(42, '/a_n_12_28_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
        [tc.DownloadFile(43, '/a_n_12_28_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
        [tc.DownloadFile(44, '/a_w_12_29_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
        [tc.DownloadFile(45, '/a_w_12_29_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
        [tc.DownloadFile(46, '/a_w_12_29_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
        [tc.DownloadFile(47, '/a_w_12_29_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
        [tc.DownloadFile(48, '/a_w_12_29_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
        [tc.DownloadFile(49, '/a_w_12_29_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]), Send, WaitMode.Wait],
        [tc.DownloadFile(50, '/a_w_12_29_0', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133]), Send, WaitMode.Wait],
        [tc.DownloadFile(51, '/a_w_12_29_0', [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]), Send, WaitMode.Wait],
        [tc.DownloadFile(52, '/a_n_12_29_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
        [tc.DownloadFile(53, '/a_n_12_29_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
        [tc.DownloadFile(54, '/a_n_12_29_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
        [tc.DownloadFile(55, '/a_n_12_29_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
        [tc.DownloadFile(56, '/a_n_12_29_0', [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
        # auto-generated file download end

        [tc.DownloadFile(57, '/a_w_12_30_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(58, '/a_n_12_30_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(59, '/a_w_13_02_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(60, '/a_n_13_02_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(61, '/a_w_13_03_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(62, '/a_n_13_03_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(63, '/a_w_13_04_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(64, '/a_n_13_04_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(65, '/a_w_13_46_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(66, '/a_n_13_46_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(67, '/a_w_13_47_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(68, '/a_n_13_47_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(69, '/a_w_13_48_0', range(0, 20)), Send, WaitMode.Wait],
        [tc.DownloadFile(70, '/a_n_13_48_0', range(0, 20)), Send, WaitMode.Wait],


        [tc.DownloadFile(77, '/a_w_12_30_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(78, '/a_n_12_30_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(79, '/a_w_13_02_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(80, '/a_n_13_02_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(81, '/a_w_13_03_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(82, '/a_n_13_03_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(83, '/a_w_13_04_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(84, '/a_n_13_04_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(85, '/a_w_13_46_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(86, '/a_n_13_46_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(87, '/a_w_13_47_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(88, '/a_n_13_47_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(89, '/a_w_13_48_0', range(20, 40)), Send, WaitMode.Wait],
        [tc.DownloadFile(90, '/a_n_13_48_0', range(20, 40)), Send, WaitMode.Wait],



    [tc.DownloadFile(91, '/radfet_42', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],


        [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]