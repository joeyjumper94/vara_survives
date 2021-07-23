import sys

import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

def connect(node,next):
    hook=modast.hook_opcode(node,None)
    hook.chain(next)
    #node.next=next
    #thanks 4onen for explaining this
    """
    node_i_want_to_hook=modast.find_say("Ooh, I do hope what I'm saying now is unique across all time, or I might link the wrong spot!")
    my_hook=modast.hook_opcode(node_i_want_to_hook,None) # makes my_hook the next node, but preserves the old next as an old_next on the my_hook object, as well as making my_hook.next equal to the old next.
    my_hook.chain(modast.find_label('my_unique_mod_label')) # replaces my_hook.next, but leaves my_hook.old_next intact
    """

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Vara Survives", "v0.1", "joeyjumper94")

    def mod_load(self):
        block1=modast.find_say("Reza aimed a kick at her, only to lose his balance and fall when she bit and held onto his shin.")
        connect(block1,modast.find_label("vara_survives_block1"))
        nat=modast.find_say("After he fought her off with a few kicks, his hand dove into his pocket to grab a few bullets, which he proceeded to load into his revolver.")
        fail=modast.find_label("vara_survives_fail")#player did not meet the requirements to save vara
        connect(fail,nat)
        alt=modast.find_label("vara_survives_remy_hatchlings_vara")#player selected vara in the remy hatchlings mod
        connect(alt,nat)
        success=modast.find_label("vara_survives_success")
        connect(success,modast.find_say("Immediately, she was on him, throwing him to the ground before starting to pound his head with her fists. Together, they rolled down the slope of the small hill on which the portal stood."))

        block2=modast.find_say("Eventually, I arrived, only to be able to confirm that both of them were dead.")
        connect(block2,modast.find_label("vara_survives_block2"))
        fail2=modast.find_label("vara_survives_fail2")
        connect(fail2,modast.find_say("I went up to the portal and examined Vara for any signs of life. I found none."))
        success2=modast.find_label("vara_survives_success2")
        connect(success2,modast.find_say("Besides those we already knew to be dead, it was also too late for Maverick."))

        block3=modast.find_say("As soon as I could, I met with Remy, who told me about everything I had missed.")
        connect(block3,modast.find_label("vara_survives_block3"))
        fail3=modast.find_label("vara_survives_fail3")
        connect(fail3,modast.find_say("So, the comet has been diverted, and you've replaced the power source for the portal. I guess I must've been gone for a long time."))
        success3=modast.find_label("vara_survives_success3")
        connect(success3,modast.find_say("So, the comet has been diverted, and you've replaced the power source for the portal. I guess I must've been gone for a long time."))

        block4=modast.find_say("Don't let me stop you from going back if that's what you want to do, though. I'll be fine.")
        connect(block4,modast.find_label("vara_survives_block4"))
        fail4=modast.find_label("vara_survives_fail4")
        fail4alt=modast.find_label("vara_survives_fail4alt")
        connect(fail4,modast.find_say("Yes. After all, I'm not alone anymore. In the last few weeks, I spent a lot of time with Adine, and I'd say we're pretty good friends now. As sad as it is what happened with Vara, there is another girl at the orphanage we've been taking care of pretty often."))
        connect(fail4alt,modast.find_say("Besides, if you really end up going back in time, I'll see you again."))
        success4=modast.find_label("vara_survives_success4")
        connect(success4,modast.find_say("Maybe you've seen her. Her name is Amely, and she's just the sweetest little girl."))
    def mod_complete(self):
        pass
