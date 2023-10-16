# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping_meta',
  'cpp',
  license: 'MPL-2.0',

  version: '0.1.8',
  default_options: ['warning_level=2', 'buildtype=release', 'cpp_std=c++20'],
  meson_version: '>=1.1' #first meson version to support c++20 with clang
)

projectnamespace = 'themachinethatgoesping'

# --- add dependency ---
meta_dep = declare_dependency(
  )

# add python src
subdir('python')

