tasks = [
    # Generated on 2020-12-16 11:54:42.356535, contains telemetry from sessions 4799 to 4800.
    # The session starts on 2020-12-16 13:12:34+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(35, '/telemetry.current', [604, 654, 704, 754, 804, 629, 679, 729, 779, 617, 667, 717, 767, 817, 641, 691, 741, 791, 611, 661]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [711, 761, 811, 623, 673, 723, 773, 823, 635, 685, 735, 785, 647, 697, 747, 797]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [163, 451, 503]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/w_17_46_0', [103, 124, 150, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/w_17_46_0', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/x_14_42_0', [6, 7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/x_17_11_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
