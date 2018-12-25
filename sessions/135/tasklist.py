tasks = [
    # ============================================================================
    # SESSION 135
    # ============================================================================

    ["SESSION 135", Print, WaitMode.NoWait],

    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # ReadMemory, weird telecommand
    #["ReadMemory, weird telecommand", Print, WaitMode.NoWait],
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    ["List files - 7 items expected", Print, WaitMode.NoWait],
    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # Wait until good uplink
    ["Beacons - Wait until good uplink - next one is POWER CYCLE", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # EPS A - Power cycle - send three times (no answer expected!)
    ["EPS A - Power cycle - send three times (no answer expected!)", Print, WaitMode.NoWait],
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    # Ping - start pinging about 30 s after reboot
    #["Ping - start pinging about 30 s after reboot", Print, WaitMode.NoWait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Wait for non-zero beacon
    #["Request till non-zero beacon decoded", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],


    # Set 9600
    #["Set 9600", Print, WaitMode.NoWait],
    [tc.SetBitrate(10, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Beacon loop at 9600 - time to adjust GRC
    ["Beacon loop at 9600", Print, WaitMode.NoWait],

    [[tc.SendBeacon(), 5], SendLoop, WaitMode.NoWait],

    # Telemetry.current between session 134 and 135
    #["Telemetry current between sessions  134 and 135", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(0, 380, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(14, 380, 25)]), Send, WaitMode.Wait],

    # Telemetry previous from 1760 to 2280 chunks
    #["Telemetry previous from 1760 to 2280 chunks", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/telemetry.previous', [i for i in range(1760, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [i for i in range(1764, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [i for i in range(1769, 2280, 25)]), Send, WaitMode.Wait],


    # More telemetry.current between session 134 and 135
    #["More telemetry current between sessions  134 and 135", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(4, 380, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(9, 380, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(19, 380, 25)]), Send, WaitMode.Wait],

    # More telemetry previous from 1760 to 2280 chunks
    #["More telemetry previous from 1760 to 2280 chunks", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1774, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1779, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(1784, 2280, 25)]), Send, WaitMode.Wait],


    # Remove radfet file
    #["Remove file", Print, WaitMode.Wait],
    [tc.RemoveFile(60, '/radfet_7'), Send, WaitMode.Wait],
    [tc.ListFiles(61, '/'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]