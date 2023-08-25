"""
 Ways to determine chance of winning

    Team Comps
        Synergies(steal from U.gg)
        AD/AP
        Tank/Mage/Assassin/Adc/Engage/Enchanter
        Range vs engage

    Player's mastery of champ
        WR
        Games played

    The team
        Team's standings
        their winstreak/lose streak
        Player experience

        

    What points to assign
        a single champ strength-
            (ban % across all games) + (WR% * 100)^2 * games played
            (pickban * WR)
        a players strength - 
            Sqrt graph of experience
        a comps strength -
            Synergies - if champs are picked together often then good synergy(USE INTERSECTION DATA TABLE)

            
 """
