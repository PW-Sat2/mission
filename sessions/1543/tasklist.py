tasks = [
    # Generated on 2019-06-28 22:47:34.288000.
    # The session starts on 2019-06-29 11:17:49+02:00.


    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    # auto-generated telemetry end

    ["The next step is Take Photo queue.", Print, WaitMode.Wait],

    # Photo queue
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 29, datetime.timedelta(minutes=0), 'p_480'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]