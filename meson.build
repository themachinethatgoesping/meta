# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping_meta',
  'cpp',
  license: 'MPL-2.0',

  version: '0.2.0',
  default_options: ['warning_level=0', 'buildtype=release', 'cpp_std=c++20'],
  meson_version: '>=1.8.1' #there is a problem with meson 1.8.0 so just use a higher version
)

projectnamespace = 'themachinethatgoesping'

# --- add dependency ---
meta_dep = declare_dependency(
  )

# add python src
subdir('python')

