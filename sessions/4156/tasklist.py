tasks = [
    # Generated on 2020-09-05 14:56:10.471000, contains telemetry from sessions 4155 to 4156.
    # The session starts on 2020-09-05 20:33:56+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(80, '/telemetry.current', [510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 535, 585, 635, 685, 735]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 523, 573, 623, 673, 723, 773, 823, 873, 923, 973, 1023]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.current', [1073, 1123, 1173, 1223, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 517, 567]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.current', [617, 667, 717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 529, 579, 629, 679, 729, 779, 829]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [879, 929, 979, 1029, 1079, 1129, 1179, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [1191, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/m_n_11_28_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/m_n_11_29_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/m_n_11_29_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/m_n_11_38_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/m_n_11_38_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/m_n_11_38_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/m_n_11_41_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/m_n_11_41_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/m_n_11_41_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/m_n_12_36_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/m_n_12_36_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/m_n_12_36_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/m_n_12_37_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/m_n_12_37_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/m_n_12_37_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/m_n_12_38_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/m_n_12_38_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/m_n_12_38_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/m_n_12_39_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/m_n_12_39_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/m_n_12_39_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/m_w_11_23_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/m_w_11_23_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/m_w_11_24_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/m_w_11_24_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/m_w_11_26_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/m_w_11_26_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/m_w_11_27_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/m_w_11_27_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/m_w_11_28_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/m_w_11_28_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/m_w_11_29_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/m_w_11_29_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/m_w_11_38_0', [38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/m_w_11_38_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/m_w_11_41_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/m_w_11_41_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/m_w_11_41_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/m_w_12_36_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/m_w_12_36_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/m_w_12_36_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/m_w_12_37_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/m_w_12_37_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/m_w_12_37_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/m_w_12_38_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/m_w_12_38_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/m_w_12_38_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/m_w_12_39_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/m_w_12_39_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/m_w_12_39_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]