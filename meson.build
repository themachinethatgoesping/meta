# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping_meta',
  'cpp',
  license: 'MPL-2.0',

  version: '0.1.2',
  default_options: ['warning_level=2', 'buildtype=release', 'cpp_std=c++17'],
  meson_version: '>=1.0' #last meson version that was tested
)

projectnamespace = 'themachinethatgoesping'

# --- add dependency ---
meta_dep = declare_dependency(
  )

# add python src
subdir('python')

