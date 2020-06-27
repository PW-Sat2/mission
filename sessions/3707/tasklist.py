tasks = [
    # Generated on 2020-06-27 14:12:03.469000, contains telemetry from sessions 3706 to 3707.
    # The session starts on 2020-06-27 21:07:55+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [2, 52, 102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 27, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877, 15, 65, 115, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815, 865, 39, 89, 139, 189, 239, 289]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 9, 59, 109, 159, 209, 259, 309, 359, 409]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [459, 509, 559, 609, 659, 709, 759, 809, 859, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [571, 621, 671, 721, 771, 821, 871, 33, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [683, 733, 783, 833, 883, 45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [795, 845]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.DownloadFile(60, '/dummy_14_33_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/dummy_15_33_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/dummy_16_33_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a_w_17_00_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a_n_17_00_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a_w_17_01_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/a_n_17_01_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/a_w_17_02_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/a_n_17_02_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/a_w_17_03_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/a_n_17_03_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/a_w_17_04_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/a_n_17_04_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/dummy_18_04_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/dummy_19_04_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/a_w_20_02_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/a_n_20_02_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/a_w_20_03_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/a_n_20_03_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/dummy_14_33_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/dummy_15_33_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/dummy_16_33_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/a_w_17_00_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/a_n_17_00_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/a_w_17_01_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/a_n_17_01_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/a_w_17_02_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/a_n_17_02_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/a_w_17_03_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/a_n_17_03_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/a_w_17_04_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/a_n_17_04_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/dummy_18_04_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/dummy_19_04_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/a_w_20_02_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/a_n_20_02_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/a_w_20_03_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/a_n_20_03_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/dummy_14_33_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/dummy_15_33_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/dummy_16_33_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/a_w_17_00_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/a_n_17_00_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/a_w_17_01_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/a_n_17_01_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/a_w_17_02_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/a_n_17_02_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/a_w_17_03_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/a_n_17_03_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/a_w_17_04_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/a_n_17_04_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/dummy_18_04_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/dummy_19_04_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/a_w_20_02_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/a_n_20_02_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/a_w_20_03_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/a_n_20_03_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(119, '/radfet_41', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]