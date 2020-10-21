tasks = [
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is SetBootSlots.", Print, WaitMode.Wait],
    [tc.SetBootSlots(76, 0b111000, 0b111), Send, WaitMode.Wait],

    ["The next step is Little Oryx Power Cycle", Print, WaitMode.Wait],
    [tc.little_oryx.Reboot(), Send, WaitMode.Wait],
    
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],    

    ["Take a few beacons before going to Read Logs step", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Read logs.", Print, WaitMode.Wait],
    [tc.ReadMemory(100, 2282733568, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(101, 2282733799, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(102, 2282734030, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(103, 2282734261, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(104, 2282734492, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(105, 2282734723, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(106, 2282734954, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(107, 2282735185, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(108, 2282735416, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(109, 2282735647, 231), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ReadMemory(110, 2282735878, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(111, 2282736109, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(112, 2282736340, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(113, 2282736571, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(114, 2282736802, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(115, 2282737033, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(116, 2282737264, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(117, 2282737495, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(118, 2282737726, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(119, 2282737957, 231), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Boot to normal software", Print, WaitMode.Wait],
    [tc.little_oryx.RebootToNormal(), Send, WaitMode.Wait],        
 
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],   

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
