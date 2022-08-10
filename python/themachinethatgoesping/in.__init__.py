# SPDX-FileCopyrightText: 2022 GEOMAR Helmholtz Centre for Ocean Research Kiel
# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: MPL-2.0

"""
themachinethatgoesping
**********************
Enable quantitative processing of multibeam and singlebeam echosounder systems
"""

@PYDEV_SRC_PATH@
@PYDEV_MODULES@

@PYDEV_INSTALL@

#import the module functions into the current namespace
modules_installed = []

#TODO: add warnings for installed packages with missing dependcies

try:
  from themachinethatgoesping import tools
  modules_installed.append("tools")
except:
  pass

try:
  from themachinethatgoesping import tools_ext
  modules_installed.append("tools_ext")
except:
  pass

try:
  from themachinethatgoesping import navigation
  modules_installed.append("navigation")
except:
  pass


try:
  from themachinethatgoesping import gridding
  modules_installed.append("gridding")
except:
  pass
