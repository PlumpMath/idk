from direct.distributed.DistributedSmoothNode import DistributedSmoothNode
from direct.actor import Actor
from direct.task.Task import cont
from direct.stdpy.threading import Timer
from pandac.PandaModules import *
from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.directutil import Mopath
from direct.gui import DirectGuiGlobals as DGG
import random

from panda3d.core import TextNode


class DistributedToon(DistributedSmoothNode):
    def __init__(self, cr):
        self.legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}
         
        self.torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgl_shorts_torso_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_left.bam'}
        DistributedSmoothNode.__init__(self,cr)
        NodePath.__init__(self, 'avatar')
        
        self.ToonSpeedFactor = 1.25
        self.ToonForwardSpeed = 16.0 * self.ToonSpeedFactor
        self.ToonJumpForce = 24.0
        self.ToonReverseSpeed = 8.0 * self.ToonSpeedFactor
        self.ToonRotateSpeed = 80.0 * self.ToonSpeedFactor
        
        self.moveKeyList = [
            'arrow_left', 'arrow_right', 'arrow_up', 'arrow_down'
            ]

        self.moveKeys = {}
        for key in self.moveKeyList:
            self.moveKeys[key] = False
            self.accept(key, self.moveKeyStateChanged, extraArgs = [key, True])
            self.accept(key + '-up', self.moveKeyStateChanged, extraArgs = [key, False])



        
        self.access = 0

        self.avColor = (1, 1, 1)
        
        self.legs = loader.loadModel('phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam')
        otherParts = self.legs.findAllMatches('**/boots*')+self.legs.findAllMatches('**/shoes')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        self.torso = loader.loadModel('phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam')
        self.headList = ['cat', 'duck', 'monkey', 'horse', 'rabbit', 'bear']
        self.bear = loader.loadModel('phase_3/models/char/bear-heads-1000.bam')
        otherParts = self.bear.findAllMatches('**/*long*')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        ntrlMuzzle = self.bear.find('**/*muzzle*neutral')
        otherParts = self.bear.findAllMatches('**/*muzzle*')
        for partNum in range(0, otherParts.getNumPaths()):
            part = otherParts.getPath(partNum)
            if part != ntrlMuzzle:
                otherParts.getPath(partNum).removeNode()
        self.rabbit = loader.loadModel('phase_3/models/char/rabbit-heads-1000.bam')
        otherParts = self.rabbit.findAllMatches('**/*long*')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        ntrlMuzzle = self.rabbit.find('**/*muzzle*neutral')
        otherParts = self.rabbit.findAllMatches('**/*muzzle*')
        for partNum in range(0, otherParts.getNumPaths()):
            part = otherParts.getPath(partNum)
            if part != ntrlMuzzle:
                otherParts.getPath(partNum).removeNode()
        self.monkey = loader.loadModel('phase_3/models/char/monkey-heads-1000.bam')
        otherParts = self.monkey.findAllMatches('**/*long*')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        ntrlMuzzle = self.monkey.find('**/*muzzle*neutral')
        otherParts = self.monkey.findAllMatches('**/*muzzle*')
        for partNum in range(0, otherParts.getNumPaths()):
            part = otherParts.getPath(partNum)
            if part != ntrlMuzzle:
                otherParts.getPath(partNum).removeNode()
        self.duck = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
        otherParts = self.duck.findAllMatches('**/*long*')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        ntrlMuzzle = self.duck.find('**/*muzzle*neutral')
        otherParts = self.duck.findAllMatches('**/*muzzle*')
        for partNum in range(0, otherParts.getNumPaths()):
            part = otherParts.getPath(partNum)
            if part != ntrlMuzzle:
                otherParts.getPath(partNum).removeNode()
        self.cat = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
        otherParts = self.cat.findAllMatches('**/*long*')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        ntrlMuzzle = self.cat.find('**/*muzzle*neutral')
        otherParts = self.cat.findAllMatches('**/*muzzle*')
        for partNum in range(0, otherParts.getNumPaths()):
            part = otherParts.getPath(partNum)
            if part != ntrlMuzzle:
                otherParts.getPath(partNum).removeNode()
        self.horse = loader.loadModel('phase_3/models/char/horse-heads-1000.bam')
        otherParts = self.horse.findAllMatches('**/*long*')
        for partNum in range(0, otherParts.getNumPaths()):
            otherParts.getPath(partNum).removeNode()
        ntrlMuzzle = self.horse.find('**/*muzzle*neutral')
        otherParts = self.horse.findAllMatches('**/*muzzle*')
        for partNum in range(0, otherParts.getNumPaths()):
            part = otherParts.getPath(partNum)
            if part != ntrlMuzzle:
                otherParts.getPath(partNum).removeNode()
        self.model = Actor({'torso':self.torso, 'legs':self.legs},
                {'torso':self.torsoAnimDict, 'legs':self.legsAnimDict})
        self.head_np = self.model.find('**/def_head')
        self.bear.reparentTo(self.head_np)
        self.rabbit.reparentTo(self.head_np)
        self.monkey.reparentTo(self.head_np)
        self.duck.reparentTo(self.head_np)
        self.cat.reparentTo(self.head_np)
        self.horse.reparentTo(self.head_np)
        self.cat.hide()
        self.bear.hide()
        self.rabbit.hide()
        self.monkey.hide()
        self.duck.hide()
        self.horse.hide()
        self.model.attach('torso', 'legs', 'joint_hips')
        self.model.reparentTo(self)

        cs = CollisionSphere(0, 0, 0, 1)
        cnode = CollisionNode('cnode')
        cnode.addSolid(cs)
        self.cnp = self.attachNewNode(cnode)

        self.still = True
        self.isMoving = False
        self.standing = 1
        self.standTime = 0
        self.previousPos = 0
        self.previousHpr = 0

        self.tag = OnscreenText(scale=.30,font=loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'),pos=(0,3.25),text='Toon',bg=(.9,.9,.9,.3),fg=(0,0,1,1),wordwrap=7,decal=True,parent=self.model)
        self.tag.setBillboardAxis(2)
        
        self.playground = loader.loadModel('phase_6/models/golf/golf_outdoor_zone.bam')
        self.playground.reparentTo(render)
        
    def moveKeyStateChanged(self, key, newState):
        self.moveKeys[key] = newState

        
    def setupLocalAvatar(self):        
        self.cnp.setCollideMask(BitMask32(0))
        self.cnp.node().setFromCollideMask(BitMask32(1))

        pusher = CollisionHandlerPusher()
        pusher.setInPattern("%in")
        pusher.addCollider(self.cnp, self)
        base.cTrav.addCollider(self.cnp, pusher)
        self.b_pose("walk",5)
        
        self.ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn22 = DirectButton(frameSize=None, text='Sit', image=(self.ButtonImage.find('**/QuitBtn_UP'), \
        self.ButtonImage.find('**/QuitBtn_DN'), self.ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.b_setSit, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.05,-0,.95), text_scale=0.059, borderWidth=(0.13, 0.01), scale=.7)
        self.ImgBtn22.bind(DGG.B3PRESS, self.ImgBtn22.editStart)
        self.ImgBtn22.bind(DGG.B3RELEASE, self.ImgBtn22.editStop)
        
        """self.ImgBtn22 = DirectButton(frameSize=None, text='Create Bot', image=(self.ButtonImage.find('**/QuitBtn_UP'), \
        self.ButtonImage.find('**/QuitBtn_DN'), self.ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.b_makeBot, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.95,-0,.95), text_scale=0.059, borderWidth=(0.13, 0.01), scale=.7)
        self.ImgBtn22.bind(DGG.B3PRESS, self.ImgBtn22.editStart)
        self.ImgBtn22.bind(DGG.B3RELEASE, self.ImgBtn22.editStop)"""
        
        self.b_setSpecies('cat')
        
        self.offset = 3.2375
                 
        
        self.b = DirectEntry(text = "" ,scale=.05,command=self.b_sendMsg,
        initialText="Chatstuff", numLines = 2,focus=1,focusInCommand=self.clearText)
        
        self.headRNG = random.choice(self.headList)

        self.ImgBtn22 = DirectButton(frameSize=None, text='Random Species', image=(self.ButtonImage.find('**/QuitBtn_UP'), \
        self.ButtonImage.find('**/QuitBtn_DN'), self.ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.b_setSpecies, extraArgs=[self.headRNG], text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.05,-0,-.95), text_scale=0.059, borderWidth=(0.13, 0.01), scale=.7)
        self.ImgBtn22.bind(DGG.B3PRESS, self.ImgBtn22.editStart)
        self.ImgBtn22.bind(DGG.B3RELEASE, self.ImgBtn22.editStop)
        
        base.camera.reparentTo(base.w.av)
        base.camera.setPos(0, -10.0 - self.offset, self.offset)
        base.camera.hide()
        self.moveTask = taskMgr.add(self.moveAvatar, 'moveAvatar')
        base.w.av.startPosHprBroadcast()
        
    def clearText(self):
        self.b.enterText('')


    def sendMsg(self, textEntered):
        self.chatbubble = loader.loadModel('phase_3/models/props/chatbox.bam')
        self.chatbubble.reparentTo(self.model)
        self.chatbubble.setPos(0,0,3.5)
        self.chatbubble.setBillboardAxis(1)
        self.chatbubble.setScale(0.3)
        self.chatbubble.find('**/chatBalloon').setPos(0,0.05,0)
        self.chatbubble.find('**/chatBalloon').setSx(0.8)
        self.talk = OnscreenText(scale=.70,font=loader.loadFont('phase_3/models/fonts/ImpressBT.ttf'),pos=(0.9,3),text=textEntered,wordwrap=10,decal=True,parent=self.chatbubble,align=TextNode.ALeft)
        self.tag.hide()
        Sequence(Wait(5),Func(self.chatbubble.removeNode),Func(self.tag.show)).start()
        if textEntered == 'horse':
            self.b_setSpecies('horse')
        if textEntered == 'cat':
            self.b_setSpecies('cat')
        if textEntered == 'duck':
            self.b_setSpecies('duck')
        if textEntered == 'rabbit':
            self.b_setSpecies('rabbit')
        if textEntered == 'bear':
            self.b_setSpecies('bear')
        if textEntered == 'monkey':
            self.b_setSpecies('monkey')
        if textEntered == 'ssnow': #Server Snow
            print "Let it snow-- Later."
        if textEntered == 'gibAdmin': #gib admin pls
            base.w.access = 9999999
            self.straccess = str(base.w.access)
            print "Your access is now "+ self.straccess +"."
            self.chatbubble.removeNode()
            self.tag.show()
        if textEntered == 'ceo' and base.w.access >= 699:
            self.b_spawnBoss('ceo')
        if textEntered == 'devroom' and base.w.access >= 100:
            base.w.changeAvZone(999)
            print "In Developer Room."
        try:
            room = int(textEntered)
            base.w.changeAvZone(room)
            roomStr = str(room)
            print "Went to room "+ roomStr +""
        except ValueError:
            print "k"
    def d_sendMsg(self, msg):
        self.sendUpdate('sendMsg', [msg])
    def b_sendMsg(self, msg):
        self.sendMsg(msg)
        self.d_sendMsg(msg)
    def spawnBoss(self, boss):
        print "Trying to spawn "+ boss +""
        if boss == 'vp':
            vp = 'swag'
            print('placeholder')
        if boss == 'ceo':
            self.ceo = Actor({"head":"phase_12/models/char/bossbotBoss-head-zero.bam", \
            "torso":"phase_12/models/char/bossbotBoss-torso-zero.bam", \
            "legs":"phase_9/models/char/bossCog-legs-zero.bam"}, \
            {"head":{"walk":"phase_9/models/char/bossCog-head-Bb_neutral.bam", \
            "run":"phase_9/models/char/bossCog-head-Bb_neutral.bam"}, \
            "torso":{"walk":"phase_9/models/char/bossCog-torso-Bb_neutral.bam", \
            "run":"phase_9/models/char/bossCog-torso-Bb_neutral.bam"}, \
            "legs":{"walk":"phase_9/models/char/bossCog-legs-Bb_neutral.bam", \
            "run":"phase_9/models/char/bossCog-legs-Bb_neutral.bam"} \
            })
            self.ceo.attach("head", "torso", "joint34")
            self.ceo.attach("torso", "legs", "joint_legs")
            self.ceo.reparentTo(render)
            self.ceo.loop("run")
            self.mypos = self.model.getPos()
            self.ceo.setPos(self.mypos)
    def d_spawnBoss(self, boss):
        self.sendUpdate('spawnBoss', [boss])
    def b_spawnBoss(self, boss):
        self.d_spawnBoss(boss)
        self.spawnBoss(boss)
    def makeBot(self):
        self.bot = self.model.copyTo(render)
        self.myPos = self.model.getPos()
        self.bot.setPos(self.myPos)
    def d_makeBot(self):
        self.sendUpdate('makeBot')
    def b_makeBot(self):
        self.makeBot()
        self.d_makeBot()
    def setSit(self):
        self.model.loop("sit")
    def d_setSit(self):
        self.sendUpdate('setSit')
    def b_setSit(self):
        self.d_setSit()
        self.setSit()

    def setSpecies(self, spcs):
        if spcs == 'horse':
            self.bear.hide()
            self.cat.hide()
            self.duck.hide()
            self.rabbit.hide()
            self.monkey.hide()
            self.horse.show()
        elif spcs == 'bear':
            self.horse.hide()
            self.cat.hide()
            self.duck.hide()
            self.rabbit.hide()
            self.monkey.hide()
            self.bear.show()
        elif spcs == 'cat':
            self.horse.hide()
            self.duck.hide()
            self.rabbit.hide()
            self.bear.hide()
            self.monkey.hide()
            self.cat.show()
        elif spcs == 'monkey':
            self.horse.hide()
            self.cat.hide()
            self.duck.hide()
            self.rabbit.hide()
            self.bear.hide()
            self.monkey.show()
        elif spcs == 'rabbit':
            self.horse.hide()
            self.cat.hide()
            self.duck.hide()
            self.monkey.hide()
            self.bear.hide()
            self.rabbit.show()
        elif spcs == 'duck':
            self.horse.hide()
            self.cat.hide()
            self.rabbit.hide()
            self.monkey.hide()
            self.bear.hide()
            self.duck.show()

        else:
            print "Invalid species"
        print "Now a "+ spcs +""
    def d_setSpecies(self, spcs):
        self.sendUpdate('setSpecies', [spcs])
        print "Now a "+ spcs +""
        
    def b_setSpecies(self, spcs):
        self.setSpecies(spcs)
        self.d_setSpecies(spcs)
    def updateName(self, textEntered):
        self.tag.setText(textEntered)
    def d_updateName(self, textEntered):
        self.sendUpdate('updateName', [textEntered])
    def b_updateName(self, textEntered):
        self.updateName(textEntered)
        self.d_updateName(textEntered)
    def setStanding(self, stand):
        self.standing = stand
        if self.standing == 1: self.still = 0

    def d_setStanding(self, stand):
        self.sendUpdate('setStanding', [stand])

    def b_setStanding(self, stand):
        self.setStanding(stand)
        self.d_setStanding(stand)

    def getStanding(self):
        return self.standing

    def doSmoothTask(self, task):
        now = globalClock.getFrameTime()
        if(self.standing == 0):
            if (self.getPos() == self.previousPos) and (self.getHpr() == self.previousHpr):
                if (self.still == True):
                    if (now > self.standTime + 0.3):
                        self.b_stop()
                        self.b_pose("walk",5)
                        self.b_setStanding(1)
                else:
                    self.standTime = now
                    self.still = True
            else:
                self.still = False
        self.previousPos = self.getPos()
        self.previousHpr = self.getHpr()

        self.smoothPosition()
        return cont

    def loop(self, animName):       
        self.model.loop(animName)

    def d_loop(self, animName):
        self.sendUpdate('loop', [animName])

    def b_loop(self, animName):
        self.model.loop(animName)
        self.d_loop(animName)

    def stop(self):
        self.model.stop()

    def d_stop(self):
        self.sendUpdate('stop',[])

    def b_stop(self):
        self.stop()
        self.d_stop()

    def pose(self, animName, frame=1):
        self.model.pose(animName, frame)

    def d_pose(self, animName, frame=1):
        self.sendUpdate('pose',[animName,frame])

    def b_pose(self, animName, frame=1):
        self.pose(animName,frame)
        self.d_pose(animName,frame)

    def generate(self):
        DistributedSmoothNode.generate(self)

        self.activateSmoothing(True, False)

        self.startSmooth()        
    def announceGenerate(self):
        DistributedSmoothNode.announceGenerate(self)

        self.reparentTo(render)

        self.model.pose("walk",5)
        if(self.getStanding() == 0): 
            self.b_loop("run")

    def disable(self):
        self.stopSmooth()

        self.detachNode()

        DistributedSmoothNode.disable(self)
    def delete(self):
        self.model = None

        DistributedSmoothNode.delete(self)
        
    def moveAvatar(self, task):
        wallBitmask = BitMask32(1)
        floorBitmask = BitMask32(2)
        base.cTrav = CollisionTraverser()
        def getAirborneHeight():
            return offset + 0.025000000000000001
        walkControls = GravityWalker(legacyLifter=True)
        walkControls.setWallBitMask(wallBitmask)
        walkControls.setFloorBitMask(floorBitmask)
        walkControls.setWalkSpeed(self.ToonForwardSpeed, self.ToonJumpForce, self.ToonReverseSpeed, self.ToonRotateSpeed)
        walkControls.initializeCollisions(base.cTrav, self.model, floorOffset=0.025, reach=4.0)
        walkControls.setAirborneHeightFunc(getAirborneHeight)
        walkControls.enableAvatarControls()
        self.model.physControls = walkControls
        

        dt = globalClock.getDt()
        
        if self.moveKeys['arrow_left']:
            base.w.av.setH(base.w.av, dt * self.ToonRotateSpeed)
        elif self.moveKeys['arrow_right']:
            base.w.av.setH(base.w.av, -dt * self.ToonRotateSpeed)

        if self.moveKeys['arrow_up']:
            base.w.av.setY(base.w.av, dt * self.ToonForwardSpeed)
        elif self.moveKeys['arrow_down']:
            base.w.av.setY(base.w.av, -dt * self.ToonReverseSpeed)

        return task.cont

