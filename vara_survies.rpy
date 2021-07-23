#requirements:
#1, see Remy's bad ending
#2, see Vara die to Reza
#3, you must follow Vara during the 3rd investigation


#for any developers that want this mod to speak to yours
#if renpy.python.store_dicts["store"].get("vara_survives_varahere",false):
#use this if you need to see if Vara should be shown alongside Remy

#if not renpy.python.store_dicts["store"].get("vara_survives_varadead",true):
#this will be false if Vara survived somehow

#if persistent.vara_survives_persistant:
#this will be true if you have gotten the good ending to this mod

#the first block is where the bulk of the logic is done, deciding how and if Vara survived or not
label vara_survives_block1:
    $ vara_survives_varadead=True
    $ vara_survives_varahere=False
    show reza at Position(xpos=0.4, xanchor='center') with ease
    play sound "fx/bite.ogg"
    $ renpy.pause (0.5)
    show reza at Position(xpos=0.4, xanchor='center', ypos=1.0, yanchor='top')
    show vara at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='center')
    with ease
    if renpy.python.store_dicts["store"].get("hatchling","")=="Vara":#player selected Vara in the remy hatchlings mod, she survives anyway
        $ vara_survives_varadead=False
        label vara_survives_remy_hatchlings_vara:
            pass
    elif not persistent.remygoodending or not persistent.remybadending or not varasaved:#did not see both of Remy's endings or our MC wasn't the one who saved Vara this run
        if persistent.vara_survives_persistant:#player has already seen this mods good ending
            pass
        else:
            label vara_survives_fail:
                pass
    $ vara_survives_varadead=False
    m "when he fell Vara immediately jumped on him and started bitting him."
    m "I went as fast as I could, but with my injuries I knew i had little chance to get there in time."
    play sound "fx/hit2.ogg"
    show vara at Position(xpos=-0.10, xanchor='left', ypos=0.90, yanchor='center')
    with ease
    play sound "fx/hit2.ogg"
    m "after struggling for a bit, reza finally pushed her off."
    show reza annoyed b at Position(xpos=0.4, xanchor='center', ypos=1.0, yanchor='bottom') with easeinbottom
    m "as he got up, his hand dove into his pocket to grab a few bullets, which he proceeded to load into his revolver."
    show vara at Position(xpos=-0.10, xanchor='left', ypos=0.90, yanchor='center') with ease
    play sound "fx/reload.ogg"
    queue sound "fx/rev.ogg"
    $ renpy.pause (0.3)
    #show reza gunpoint b at Position(xpos=0.45, xanchor='center', ypos=1.0, yanchor='bottom') with dissolve
    show vara at Position(xpos=-0.20, xanchor='left', ypos=0.90, yanchor='center') with ease
    m "as he pointed his gun at her, Izumi appeared behind him."
    if persistent.annabadending==True:
        show izumi normal 4 d at center behind reza with easeinright
    else:
        show izumi normal 4 c at center behind reza with easeinright
    #show izumi at Position(xpos=0.3, xanchor='center') with move6
    play sound "fx/impact3.ogg"
    play sound2 "fx/silence.ogg"
    queue sound2 "fx/rolldownhill.ogg"
    show izumi at Position(xpos=0.4, xanchor='center', ypos=1.0, yanchor="top")
    show reza at Position(xpos=0.3, xanchor='center', ypos=1.0, yanchor="top")
    with move8
    label vara_survives_success:
        pass

#if Vara survived some of the vanilla text no longer makes sense so we need to change it
label vara_survives_block2:
    if renpy.python.store_dicts["store"].get("hatchling","")!="Vara":#player didn't select Vara in the remy hatchlings mod.
        if persistent.vara_survives_persistant or persistent.remygoodending and persistent.remybadending and varasaved:#has seen both of Remy's endings and our MC rescued Vara themself
            show remy shy behind vara at Position(xpos=0.6, xanchor='left', ypos=1.0, yanchor='bottom') with easeinright
            m "When I looked up again, I could see Remy looking at Vara with a pained expression."
            Ry "Were you looking for me? Did you sneak out again?"
            show vara sad flip at Position(xpos=0.35, xanchor='left', ypos=0.90, yanchor='center') with move8
            m "He enveloped her as his tears started raining down."
            $ renpy.pause (6.0)
            stop music fadeout 3.0
            $ renpy.pause (0.5)
            scene black with dissolveslow
            $ renpy.pause (2.0)
            window show
            n "Soon, more help arrived. Remy, Vara, and I got all the medical attention we needed."
            label vara_survives_success2:
                pass
        else:
            pass
    else:
        pass
    label vara_survives_fail2:
        pass

#show Vara alongside Remy unless she is dead or we chose to adopt Amely
label vara_survives_block3:
    if vara_survives_varadead or renpy.python.store_dicts["store"].get("hatchling","Amely")=="Amely":#Vara dead or the player selected Amely in Remy Hatchlings mod
        window hide
        nvl clear
        $ renpy.pause (2.0)
        scene park2 with dissolveslow
        show remy normal with dissolve
        play music "mx/library.ogg" fadein 2.0
        label vara_survives_fail3:
            pass
    else:
        $ vara_survives_varahere=True
        window hide
        nvl clear
        $ renpy.pause (2.0)
        scene park2 with dissolveslow
        #given that Remy nearly lost his daughter to a serial killer, he probably won't let her out of his sight for a while
        
        show vara normal flip at Position(xpos=0.30, xanchor='center', ypos=0.8, yanchor="center")
        show remy normal behind vara at Position(xpos=0.70, xanchor='center', ypos=1.0, yanchor="bottom")
        with dissolve
        play music "mx/library.ogg" fadein 2.0
        label vara_survives_success3:
            pass
#again more dialog that no longer makes sense if Vara survived
label vara_survives_block4:
    c "are you sure you will be fine?"
    if vara_survives_varadead:#Vara is dead
        if renpy.python.store_dicts["store"].get("hatchling","Vara")=="Amely":#dialog from Remy Hatchlings that apears when you select Amely
            Ry "Yes. After all, I'm not alone anymore. I have Amely to care for and I'm sure Adine will be up for helping if it came down to that."
            Ry look "Though if I'd adopted Vara, things might have been different. I might have been quicker. She might have lived."
            c "Don't worry about it. There's nothing you can do now. Just look to the future, will you?"
            Ry normal "I'll try."
            label vara_survives_fail4alt:
                pass
        else:
            label vara_survives_fail4:#continue with the cannon dialog
                pass
    else:
        if varasaved and not persistent.vara_survives_persistant:#player has met all requirements but not already seen this mods good ending
            $ persistent.vara_survives_persistant=True
            call syscheck from vara_suvives_syscheck
            play sound "fx/system.wav"
            if system=="normal":
                s "Vara survived! Congratulations [player_name]\nshe somehow remembered Reza was bad."
            else:
                s "Vara survived! Congratulations [player_name]\nshe knows Reza is dangerous."
        elif varasaved:
            pass
        #it does not make sense for remy to say "As sad as it is what happened with Vara" if she is alive and well
        Ry "Yes. After all, I'm not alone anymore. In the last few weeks, I spent a lot of time with Adine, and I'd say we're pretty good friends now."
        if vara_survives_varahere:
            Vr "..."
        else:
            pass
        Ry "In addition to Vara, another hatchling has caught my eye."
        label vara_survives_success4:
            pass
#
