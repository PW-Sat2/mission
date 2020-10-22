tasks = [
    [[tc.PingTelecommand(), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],    

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

    [tc.ReadMemory(120, 2282738188, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(121, 2282738419, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(122, 2282738650, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(123, 2282738881, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(124, 2282739112, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(125, 2282739343, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(126, 2282739574, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(127, 2282739805, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(128, 2282740036, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(129, 2282740267, 231), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
        
    [tc.ReadMemory(130, 2282740498, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(131, 2282740729, 231), Send, WaitMode.Wait],
    [tc.ReadMemory(132, 2282740960, 77), Send, WaitMode.Wait],   

    [tc.SendBeacon(), Send, WaitMode.Wait],     

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
