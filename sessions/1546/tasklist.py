tasks = [
    # Generated on 2019-07-27 12:59:06.158015, contains telemetry from sessions 1544 to 1545.
    # The session starts on 2019-07-27 13:16:12+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # 18th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_18'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Europe
    [tc.TakePhotoTelecommand(210, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(211, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(212, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(213, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # North America
    [tc.TakePhotoTelecommand(214, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=17), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(215, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(216, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(217, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(218, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(219, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Alaska
    [tc.TakePhotoTelecommand(220, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=93), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(221, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(222, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(223, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(224, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(225, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968, 1018, 1068, 1118]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1168, 1218, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843, 893, 943, 993, 1043]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1093, 1143, 1193, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1031, 1081, 1131, 1181, 1231, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855, 905]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [955, 1005, 1055, 1105, 1155, 1205, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [875, 925, 975, 1025, 1075, 1125, 1175, 1225, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [749, 799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [711, 761, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # file download start
    [tc.DownloadFile(40, '/p_480_3', [32, 140, 26, 28, 31]), Send, WaitMode.Wait],

    [tc.DownloadFile(41, '/p_480_4', [116]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(42, '/p_480_6', [0, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 121, 124]), Send, WaitMode.Wait],

    [tc.DownloadFile(43, '/p_480_7', [0, 1, 3, 4, 5, 12]), Send, WaitMode.Wait],

    [tc.DownloadFile(44, '/p_480_8', [34, 66, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/p_480_9', [4, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p_480_9', [79, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p_480_9', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p_480_9', [131, 132, 133, 134, 135, 136]), Send, WaitMode.Wait],

    [tc.DownloadFile(49, '/p_480_10', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p_480_10', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p_480_10', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p_480_10', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p_480_10', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p_480_10', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p_480_10', [i for i in range(120, 124, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/p_480_11', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p_480_11', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p_480_11', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p_480_11', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p_480_11', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p_480_11', [i for i in range(100, 113, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p_480_12', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p_480_12', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p_480_12', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p_480_12', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p_480_12', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p_480_12', [i for i in range(100, 113, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(68, '/p_480_13', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p_480_13', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p_480_13', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p_480_13', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p_480_13', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p_480_13', [i for i in range(100, 116, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(74, '/p_480_14', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p_480_14', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p_480_14', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p_480_14', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/p_480_14', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/p_480_14', [i for i in range(100, 115, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/p_480_15', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p_480_15', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p_480_15', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p_480_15', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p_480_15', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p_480_15', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p_480_15', [i for i in range(120, 126, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(87, '/p_480_16', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/p_480_16', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/p_480_16', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/p_480_16', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/p_480_16', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/p_480_16', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/p_480_16', [i for i in range(120, 135, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(94, '/p_480_17', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/p_480_17', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/p_480_17', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/p_480_17', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/p_480_17', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/p_480_17', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/p_480_17', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p_480_17', [i for i in range(140, 149, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(102, '/p_480_18', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p_480_18', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p_480_18', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p_480_18', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p_480_18', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p_480_18', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p_480_18', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p_480_18', [i for i in range(140, 153, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p_480_19', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p_480_19', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/p_480_19', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p_480_19', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/p_480_19', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p_480_19', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/p_480_19', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/p_480_19', [i for i in range(140, 156, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(118, '/p_480_20', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/p_480_20', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/p_480_20', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/p_480_20', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/p_480_20', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/p_480_20', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/p_480_20', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/p_480_20', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/p_480_20', [i for i in range(160, 166, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(127, '/p_480_21', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/p_480_21', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/p_480_21', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(130, '/p_480_21', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/p_480_21', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/p_480_21', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/p_480_21', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/p_480_21', [i for i in range(140, 146, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(135, '/p_480_22', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/p_480_22', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/p_480_22', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/p_480_22', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(139, '/p_480_22', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(140, '/p_480_22', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/p_480_22', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/p_480_22', [i for i in range(140, 157, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(143, '/p_480_23', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(144, '/p_480_23', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(145, '/p_480_23', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(146, '/p_480_23', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(147, '/p_480_23', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(148, '/p_480_23', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(149, '/p_480_23', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(150, '/p_480_23', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/p_480_23', [i for i in range(160, 170, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(152, '/p_480_24', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/p_480_24', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/p_480_24', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(155, '/p_480_24', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(156, '/p_480_24', [i for i in range(80, 91, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(157, '/p_480_25', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(158, '/p_480_25', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(159, '/p_480_25', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(160, '/p_480_25', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(161, '/p_480_25', [i for i in range(80, 91, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(162, '/p_480_26', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(163, '/p_480_26', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(164, '/p_480_26', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(165, '/p_480_26', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(166, '/p_480_26', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(167, '/p_480_26', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(168, '/p_480_26', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(169, '/p_480_26', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(170, '/p_480_26', [i for i in range(160, 167, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(171, '/p_480_27', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(172, '/p_480_27', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(173, '/p_480_27', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(174, '/p_480_27', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(175, '/p_480_27', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(176, '/p_480_27', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(177, '/p_480_27', [i for i in range(120, 133, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(178, '/p_480_28', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(179, '/p_480_28', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(180, '/p_480_28', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(181, '/p_480_28', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/p_480_28', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(183, '/p_480_28', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(184, '/p_480_28', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(185, '/p_480_28', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/p_480_28', [i for i in range(160, 165, 1)]), Send, WaitMode.Wait],
    # file download end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]