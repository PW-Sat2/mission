tasks = [
    # Generated on 2020-05-31 23:08:53.307000, contains telemetry from sessions 3536 to 3537.
    # The session starts on 2020-06-01 00:22:40+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(63, '/telemetry.current', [1705, 1755, 1805, 1855, 1905, 1730, 1780, 1830, 1880, 1718, 1768, 1818, 1868, 1918, 1742, 1792, 1842, 1892, 1712, 1762]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [1812, 1862, 1912, 1724, 1774, 1824, 1874, 1924, 1736, 1786, 1836, 1886, 1748, 1798, 1848, 1898]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/a6w_480_12_21_0', [100, 101, 102, 103, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/a6w_480_12_21_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a6w_480_12_21_0', [138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # When everything is downloaded, switch to deep-sleep
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(6), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]