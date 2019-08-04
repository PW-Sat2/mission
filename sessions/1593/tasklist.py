tasks = [
    # Generated on 2019-08-04 12:19:14.987000, contains telemetry from sessions 1592 to 1593.
    # The session starts on 2019-08-04 13:20:07+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_10_sec', [663]), Send, WaitMode.Wait],
    # missing from previous session end

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [528, 578, 628, 678, 728, 553, 603, 653, 703, 541, 591, 641, 691, 741, 565, 615, 665, 715, 535, 585]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [635, 685, 735, 547, 597, 647, 697, 747, 559, 609, 659, 709, 571, 621, 671, 721]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(100, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

]