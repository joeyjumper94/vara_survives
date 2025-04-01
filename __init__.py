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
        return ("Vara Survives", "v0.2", "joeyjumper94")

    def mod_load(self):
        remygoodending=modast.find_label("remygoodending")
        filename=remygoodending.filename
        for node in renpy.game.script.all_stmts:
            if filename==node.filename and isinstance(node,ast.Say):

                if node.what=="Reza aimed a kick at her, only to lose his balance and fall when she bit and held onto his shin.":
                    print("Vara Survives mod link block1")
                    block1=node
                    connect(block1,modast.find_label("vara_survives_block1"))
                if node.what=="After he fought her off with a few kicks, his hand dove into his pocket to grab a few bullets, which he proceeded to load into his revolver.":
                    print("Vara Survives mod link nat")
                    nat=node
                    #player did not meet the requirements to save vara
                    connect(modast.find_label("vara_survives_fail"),nat)
                    #player selected vara in the remy hatchlings mod
                    connect(modast.find_label("vara_survives_remy_hatchlings_vara"),nat)
                if node.what=="Immediately, she was on him, throwing him to the ground before starting to pound his head with her fists. Together, they rolled down the slope of the small hill on which the portal stood.":
                    print("Vara Survives mod link success1")
                    success1=node
                    connect(modast.find_label("vara_survives_success1"),success1)

                if node.what=="Eventually, I arrived, only to be able to confirm that both of them were dead.":
                    print("Vara Survives mod link block2")
                    block2=node
                    connect(block2,modast.find_label("vara_survives_block2"))
                if node.what=="I went up to the portal and examined Vara for any signs of life. I found none.":
                    print("Vara Survives mod link fail2")
                    fail2=node
                    connect(modast.find_label("vara_survives_fail2"),fail2)
                if node.what=="Besides those we already knew to be dead, it was also too late for Maverick.":
                    print("Vara Survives mod link success2")
                    success2=node
                    connect(modast.find_label("vara_survives_success2"),success2)

                if node.what=="As soon as I could, I met with Remy, who told me about everything I had missed.":
                    print("Vara Survives mod link block3")
                    block3=node
                    connect(block3,modast.find_label("vara_survives_block3"))
                if node.what=="So, the comet has been diverted, and you've replaced the power source for the portal. I guess I must've been gone for a long time.":
                    print("Vara Survives mod link fail3")
                    fail3=node
                    connect(modast.find_label("vara_survives_fail3"),fail3)
                    print("Vara Survives mod link success3")
                    success3=node
                    connect(modast.find_label("vara_survives_success3"),success3)

                if node.what=="Don't let me stop you from going back if that's what you want to do, though. I'll be fine.":
                    print("Vara Survives mod link block4")
                    block4=node
                    connect(block4,modast.find_label("vara_survives_block4"))
                if node.what=="Yes. After all, I'm not alone anymore. In the last few weeks, I spent a lot of time with Adine, and I'd say we're pretty good friends now. As sad as it is what happened with Vara, there is another girl at the orphanage we've been taking care of pretty often.":
                    print("Vara Survives mod link fail4")
                    fail4=node
                    connect(modast.find_label("vara_survives_fail4"),fail4)
                if node.what=="Besides, if you really end up going back in time, I'll see you again.":
                    print("Vara Survives mod link fail4alt")
                    fail4alt=node
                    connect(modast.find_label("vara_survives_fail4alt"),fail4alt)
                if node.what=="Maybe you've seen her. Her name is Amely, and she's just the sweetest little girl.":
                    print("Vara Survives mod link success4")
                    success4=node
                    connect(modast.find_label("vara_survives_success4"),success4)
    def mod_complete(self):
        pass
