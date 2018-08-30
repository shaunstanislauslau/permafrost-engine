#
#  This file is part of Permafrost Engine. 
#  Copyright (C) 2018 Eduard Permyakov 
#
#  Permafrost Engine is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Permafrost Engine is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
#  Linking this software statically or dynamically with other modules is making 
#  a combined work based on this software. Thus, the terms and conditions of 
#  the GNU General Public License cover the whole combination. 
#  
#  As a special exception, the copyright holders of Permafrost Engine give 
#  you permission to link Permafrost Engine with independent modules to produce 
#  an executable, regardless of the license terms of these independent 
#  modules, and to copy and distribute the resulting executable under 
#  terms of your choice, provided that you also meet, for each linked 
#  independent module, the terms and conditions of the license of that 
#  module. An independent module is a module which is not derived from 
#  or based on Permafrost Engine. If you modify Permafrost Engine, you may 
#  extend this exception to your version of Permafrost Engine, but you are not 
#  obliged to do so. If you do not wish to do so, delete this exception 
#  statement from your version.
#

import pf
from constants import *
import map
import globals
import mouse_events

from math import cos, pi

import view_controllers.terrain_tab_vc as ttvc
import view_controllers.objects_tab_vc as otvc
import view_controllers.tab_bar_vc as tbvc
import view_controllers.menu_vc as mvc

import views.tab_bar_window as tbw
import views.terrain_tab_window as ttw
import views.objects_tab_window as otw
import views.menu_window as mw

############################################################
# Global settings                                          #
############################################################

pf.set_ambient_light_color([1.0, 1.0, 1.0])
pf.set_emit_light_color([1.0, 1.0, 1.0])
pf.set_emit_light_pos([1024.0, 512.0, 256.0])

pf.new_game_string(globals.active_map.pfmap_str())
pf.set_minimap_position(UI_LEFT_PANE_WIDTH + MINIMAP_PX_WIDTH/cos(pi/4)/2 + 10, 
    pf.get_resolution()[1] - MINIMAP_PX_WIDTH/cos(pi/4)/2 - 10)
pf.disable_unit_selection()

mouse_events.install()

############################################################
# Setup UI                                                 #
############################################################

terrain_tab_vc = ttvc.TerrainTabVC(ttw.TerrainTabWindow())
objects_tab_vc = otvc.ObjectsVC(otw.ObjectsTabWindow())

tab_bar_vc = tbvc.TabBarVC(tbw.TabBarWindow())
tab_bar_vc.push_child("Terrain", terrain_tab_vc)
tab_bar_vc.push_child("Objects", objects_tab_vc)
tab_bar_vc.activate()
tab_bar_vc.view.show()

menu = mw.Menu()
menuvc = mvc.MenuVC(menu)
menuvc.activate()

mb = mw.MenuButtonWindow(menu)
mb.show()

