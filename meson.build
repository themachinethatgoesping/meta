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
  default_options: ['warning_level=2', 'buildtype=release', 'cpp_std=c++20', 'b_lto=true', 'b_lto_mode=thin', 'b_thinlto_cache=true', 'b_staticpic=true'],
  meson_version: '>=1.3.2' #first version with  clang-cl openmp support
)

projectnamespace = 'themachinethatgoesping'

# --- add dependency ---
meta_dep = declare_dependency(
  )

# add python src
subdir('python')

