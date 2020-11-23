tasks = [
    # Generated on 2020-11-23 10:56:00.753000, contains telemetry from sessions 4655 to 4656.
    # The session starts on 2020-11-23 12:12:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(37, '/telemetry.current', [631, 681, 731, 781, 831, 656, 706, 756, 806, 644, 694, 744, 794, 844, 668, 718, 768, 818, 638, 688]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [738, 788, 838, 650, 700, 750, 800, 850, 662, 712, 762, 812, 674, 724, 774, 824]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(32, '/n_w_7_0', [33, 35, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/n_w_7_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/n_w_8_0', [19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/n_w_8_0', [66, 67, 70, 106, 117, 118, 126, 127, 132, 133, 137, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/n_w_8_0', [147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    ["Set bootslots for deep_sleep.", Print, WaitMode.Wait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]