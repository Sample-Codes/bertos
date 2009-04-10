#
# Copyright 2009 Develer S.r.l. (http://www.develer.com/)
# All rights reserved.
#
# Makefile template for BeRTOS wizard.
#
# Author: Lorenzo Berni <duplo@develer.com>
#
#

# Constants automatically defined by the selected modules
$constants

# Our target application
TRG += $pname

$pname_PREFIX = $prefix

$pname_SUFFIX = $suffix

$pname_$cpuflag = $cpuname

# Files automatically generated by the wizard. DO NOT EDIT, USE $pname_USER_CSRC INSTEAD!
$pname_WIZARD_CSRC = \
	$csrc
	#

# Files included by the user.
$pname_USER_CSRC = \
	$main \
	#

# Automatically generated by the wizard. PLEASE DO NOT EDIT!
$pname_CSRC = $($pname_WIZARD_CSRC) $($pname_USER_CSRC)

# Files automatically generated by the wizard. DO NOT EDIT, USE $pname_USER_PCSRC INSTEAD!
$pname_WIZARD_PCSRC = \
	$pcsrc
	#

# Files included by the user.
$pname_USER_PCSRC = \
	#

# Automatically generated by the wizard. PLEASE DO NOT EDIT!
$pname_PCSRC = $($pname_WIZARD_PCSRC) $($pname_USER_PCSRC)

# Files automatically generated by the wizard. DO NOT EDIT, USE $pname_USER_CPPASRC INSTEAD!
$pname_WIZARD_CPPASRC = \
	$cppasrc
	#

# Files included by the user.
$pname_USER_CPPASRC = \
	#

# Automatically generated by the wizard. PLEASE DO NOT EDIT!
$pname_CPPASRC = $($pname_WIZARD_CPPASRC) $($pname_USER_CPPASRC)

# Files automatically generated by the wizard. DO NOT EDIT, USE $pname_USER_CXXSRC INSTEAD!
$pname_WIZARD_CXXSRC = \
	$cxxsrc
	#

# Files included by the user.
$pname_USER_CXXSRC = \
	#

# Automatically generated by the wizard. PLEASE DO NOT EDIT!
$pname_CXXSRC = $($pname_WIZARD_CXXSRC) $($pname_USER_CXXSRC)

# Files automatically generated by the wizard. DO NOT EDIT, USE $pname_USER_ASRC INSTEAD!
$pname_WIZARD_ASRC = \
	$asrc
	#

# Files included by the user.
$pname_USER_ASRC = \
	#

# Automatically generated by the wizard. PLEASE DO NOT EDIT!
$pname_ASRC = $($pname_WIZARD_ASRC) $($pname_USER_ASRC)

$pname_CFLAGS = $cflags
$pname_LDFLAGS = $ldflags
$pname_CPPFLAGS = $cppflags
$pname_CPPAFLAGS = -D'CPU_FREQ=($cpuclockfreq)' $cppaflags
$pname_CXXFLAGS = $cxxflags
$pname_ASFLAGS = $asflags
$pname_ARFLAGS = $arflags
