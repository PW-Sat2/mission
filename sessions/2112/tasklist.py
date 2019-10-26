tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [3, 53, 103, 153, 203, 28, 78, 128, 178, 16, 66, 116, 166, 216, 40, 90, 140, 190, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [110, 160, 210, 22, 72, 122, 172, 222, 34, 84, 134, 184, 46, 96, 146, 196]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Download radfet data
    [tc.DownloadFile(100, '/radfet_24', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.ReadMemory(14, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing
    [tc.ReadMemory(3, 0x88018760, 3720), Send, WaitMode.Wait], # YAFFS_dev structure

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # The Satellite of the Rising Sun - wait for 23:25
    [tc.TakePhotoTelecommand(40, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(41, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(42, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(minutes=5), 't02w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(43, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(minutes=0), 't03w_240'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(204, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]