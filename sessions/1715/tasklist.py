tasks = [
     [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(85, '/telemetry.current', [1207, 1257, 1307, 1357, 1407, 1232, 1282, 1332, 1382, 1220, 1270, 1320, 1370, 1420, 1244, 1294, 1344, 1394, 1214, 1264]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [1314, 1364, 1414, 1226, 1276, 1326, 1376, 1426, 1238, 1288, 1338, 1388, 1250, 1300, 1350, 1400]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [211, 224, 261, 424, 481, 1099]), Send, WaitMode.Wait],    
    # auto-generated telemetry end

    # missing from previous session start part 1
    [tc.DownloadFile(33, '/suns_ps_11', [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_11', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_11', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_11', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_11', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    # missing from previous session end

    [tc.SendBeacon(), Send, WaitMode.Wait],
    # Super Long Photos Part 1 - aim into 22:43

    # Orbit 1, 23:02, 60 N, Alaska
    [tc.TakePhotoTelecommand(200, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=19), 't01w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(201, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(202, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't01n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(203, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.NoWait],

    # Orbit 1, 23:09, 40 N, ocean
    [tc.TakePhotoTelecommand(204, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't02w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(205, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't02n_128'), Send, WaitMode.NoWait], 
 
    # Orbit 1, time extender
    [tc.TakePhotoTelecommand(206, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_1'), Send, WaitMode.Wait],
 
    # Orbit 2, 00:38, 60 N, more Alaska
    [tc.TakePhotoTelecommand(207, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=29), 't03w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(208, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(209, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't03n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(210, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.NoWait],

    # Orbit 2, 00:45, 40 N, ocean
    [tc.TakePhotoTelecommand(211, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't04w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(212, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't04n_128'), Send, WaitMode.NoWait], 
 
    # Orbit 2, time extender
    [tc.TakePhotoTelecommand(213, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_2'), Send, WaitMode.Wait],
 
    # Orbit 3, 02:14, 60 N, Siberia
    [tc.TakePhotoTelecommand(214, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=29), 't05w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(215, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(216, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't05n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(217, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05n_480'), Send, WaitMode.NoWait],

    # Orbit 3, 02:21, 40 N, ocean
    [tc.TakePhotoTelecommand(218, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't06w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(219, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't06n_128'), Send, WaitMode.NoWait], 
 
    # Orbit 3, time extender
    [tc.TakePhotoTelecommand(220, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_3'), Send, WaitMode.Wait],
 
    # Orbit 4, 03:57, 40 N, Japan
    [tc.TakePhotoTelecommand(221, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't07w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(222, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(223, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't07n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(224, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07n_480'), Send, WaitMode.Wait],

    # Orbit 4, time extender
    [tc.TakePhotoTelecommand(225, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_4'), Send, WaitMode.Wait],
 
    # Orbit 5, 05:33, 40 N, China
    [tc.TakePhotoTelecommand(226, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't08w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(227, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(228, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't08n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(229, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08n_480'), Send, WaitMode.Wait],

    # Orbit 5, time extender
    [tc.TakePhotoTelecommand(230, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_5'), Send, WaitMode.Wait],
 
    # Orbit 6, 07:09, 40 N, Tibet
    [tc.TakePhotoTelecommand(231, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't09w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(232, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(233, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't09n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(234, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09n_480'), Send, WaitMode.Wait],

    # Orbit 6, 07:11, Himalayas
    [tc.TakePhotoTelecommand(235, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 't10w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(236, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(237, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't10n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(238, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10n_480'), Send, WaitMode.Wait],

    # Orbit 6, time extender
    [tc.TakePhotoTelecommand(239, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_6'), Send, WaitMode.Wait],
 
    # Orbit 7, 08:45, 40 N, Pakistan or somewhere there
    [tc.TakePhotoTelecommand(240, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=34), 't11w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(241, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11w_480'), Send, WaitMode.NoWait],
    [tc.TakePhotoTelecommand(242, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't11n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(243, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11n_480'), Send, WaitMode.NoWait],


    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start part 2
    [tc.DownloadFile(38, '/p1_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p1_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p5_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p5_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p3_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p2_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p2_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/p4_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p6_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p8_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],

    [tc.DownloadFile(82, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p9_128_0', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(53, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p11_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p11_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p14_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p26_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p26_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p15_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p12_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p19_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/p22_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p16_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p16_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/p18_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p18_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p21_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],

    [tc.DownloadFile(76, '/p17_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],

    [tc.DownloadFile(84, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],

    [tc.DownloadFile(72, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],     
    [tc.DownloadFile(61, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],     
    [tc.DownloadFile(48, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
     
     
     
    # missing from previous session end








    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]