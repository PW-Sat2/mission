tasks = [
    # Generated on 2021-01-30 00:07:08.467000, contains telemetry from sessions 5067 to 5068.
    # The session starts on 2021-01-30 10:55:39+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # radfet_58

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_58'), Send, WaitMode.Wait],

    # foteczki (11:04), zakładamy wysłanie o 11:00
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=4), 'wro_w_p480_11_04'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'wro_n_p480_11_04'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=8), 'wro_w_p480_11_12'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'wro_n_p480_11_12'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1332, 1382, 1432, 1482, 1532, 1582, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807, 857, 907, 957, 1007]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 345, 395, 445, 495, 545, 595, 645, 695, 745]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 1445, 1495, 1545, 1595, 369, 419, 469]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469]), Send, WaitMode.Wait],


    [tc.ListFiles(41, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(35, '/telemetry.current', [1519, 1569, 339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 1189]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1239, 1289, 1339, 1389, 1439, 1489, 1539, 1589, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [951, 1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 363, 413, 463, 513, 563, 613]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 375]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1425, 1475, 1525, 1575]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]