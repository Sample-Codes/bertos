#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of bertos.
#
# Bertos is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# As a special exception, you may use this file as part of a free software
# library without restriction.  Specifically, if other files instantiate
# templates or use macros or inline functions from this file, or you compile
# this file and link it with other files to produce an executable, this
# file does not by itself cause the resulting executable to be covered by
# the GNU General Public License.  This exception does not however
# invalidate any other reasons why the executable file might be covered by
# the GNU General Public License.
#
# Copyright 2010 Develer S.r.l. (http://www.develer.com/)
#
# $Id$
#
# Author: Lorenzo Berni <duplo@develer.com>
#

import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from BWizardPage import BWizardPage

from BCpuPage import BCpuPage
from BOutputPage import BOutputPage
from BRoutePage import BRoutePage

import const
import qvariant_converter
from bertos_utils import presetList

class BBoardPage(BWizardPage):
    """
    Initial page of the alternative route. Permit to select one of the
    predefined projects for supported board.
    """
    
    def __init__(self):
        BWizardPage.__init__(self, const.UI_LOCATION + "/board_select.ui")
        self.setTitle(self.tr("Select the board from the predefined ones"))
        self._last_selected = None

    ## Overloaded QWizardPage methods ##

    def isComplete(self):
        """
        Overload of the QWizardPage isComplete method.
        """
        if self.selected:
            _info_dict = qvariant_converter.getDict(self.selected.data(0, Qt.UserRole))
            _type = _info_dict["type"]
            type = qvariant_converter.getString(_type)
            if type == "project":
                self.setProjectInfo("PROJECT_PRESET", qvariant_converter.getString(_info_dict["path"]))
                return True
            else:
                return False
        else:
            return False

    def nextId(self):
        """
        Overload of the QWizardPage nextId method.
        """
        return self.wizard().pageIndex(BRoutePage)

    ####

    ## Overloaded BWizardPage methods ##

    def setupUi(self):
        """
        Overload of the BWizardPage setupUi method.
        """
        pass

    def connectSignals(self):
        """
        Overload of the BWizardPage connectSignals method.
        """
        self.connect(self.pageContent.boardTree, SIGNAL("itemSelectionChanged()"), self, SIGNAL("completeChanged()"))

    def reloadData(self):
        """
        Overload of the BWizardPage reloadData method.
        """
        self._fillPresetTree()

    ####

    ## Slots ##


    ####

    @property
    def selected(self):
        # We can only take the selected item list (not the single item)
        _selected_items = self.pageContent.boardTree.selectedItems()
        if _selected_items:
            return _selected_items[0]
        else:
            return None

    def _fillPresetTree(self):
        self.pageContent.boardTree.clear()
        self.project.loadProjectPresets()
        preset_tree = self.project.info("PRESET_TREE")
        for obj in preset_tree["children"]:
            self._createPresetNode(self.pageContent.boardTree, obj)

    def _createPresetNode(self, parent, obj):
        selected_item_name = self.projectInfo("PROJECT_PRESET")
        item_name = obj["info"].get("name", obj["info"]["filename"])
        item = QTreeWidgetItem(parent, [item_name]) 
        item.setIcon(0, QIcon(self._getNodeIcon(obj)))
        children_dict = obj["children"]
        item.setData(0, Qt.UserRole, qvariant_converter.convertDict(obj["info"]))
        if obj["info"]["path"] == selected_item_name:
            self.pageContent.boardTree.setCurrentItem(item)
        for child in children_dict:
            self._createPresetNode(item, child)

    def _getNodeIcon(self, obj):
        icon_file = os.path.join(obj["info"]["path"], const.PREDEFINED_BOARD_ICON_FILE)
        if os.path.exists(icon_file):
            return icon_file
        elif obj["info"]["type"] == "dir":
            return const.PREDEFINED_BOARD_DEFAULT_DIR_ICON
        else:
            return const.PREDEFINED_BOARD_DEFAULT_PROJECT_ICON