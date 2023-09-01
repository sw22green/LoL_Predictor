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
        single champ strength-
            (pickban * WR)
        players strength - 
            Sqrt graph of experience
        # comps strength -
        #     Synergies - if champs are picked together often then good synergy(USE INTERSECTION DATA TABLE)
        team's strength-
            WL ratio
        
    
    What matters most - Team Strength> comp strength > single champ strength > player strength
            
    
    Machine Learning
    Might need columns on player experience, team record, comp synergy, champ strength idk
 """
