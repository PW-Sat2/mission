tasks = [
    # Generated on 2019-11-22 21:33:26.168000, contains telemetry from sessions 2287 to 2288.
    # The session starts on 2019-11-22 22:48:22+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [6, 56, 106, 156, 206, 31, 81, 131, 181, 19, 69, 119, 169, 219, 43, 93, 143, 193, 13, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [113, 163, 213, 25, 75, 125, 175, 225, 37, 87, 137, 187, 49, 99, 149, 199]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(41, '/radfet_26', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/t01w_240_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t01w_240_1', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t01w_240_2', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t01w_240_3', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t01w_240_4', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t01w_240_5', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t01w_240_6', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t01w_240_7', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t01w_240_8', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t01w_240_9', range(0, 20)), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Wait for 22:52
    [tc.TakePhotoTelecommand(42, CameraLocation.Nadir, PhotoResolution.p240, 29, datetime.timedelta(minutes=10), 't03n_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(43, CameraLocation.Nadir, PhotoResolution.p240, 29, datetime.timedelta(minutes=0), 't04n_240'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/t01w_240_10', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t01w_240_11', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t01w_240_12', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t01w_240_13', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t01w_240_14', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t01w_240_15', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t01w_240_16', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t01w_240_17', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t01w_240_18', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t01w_240_19', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t01w_240_20', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t01w_240_21', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t01w_240_22', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t01w_240_23', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t01w_240_24', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t01w_240_25', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t01w_240_26', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t01w_240_27', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t01w_240_28', range(0, 20)), Send, WaitMode.Wait],

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]