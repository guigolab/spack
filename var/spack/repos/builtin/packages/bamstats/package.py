# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install bamstats
#
# You can edit this file again by typing:
#
#     spack edit bamstats
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Bamstats(Package):
    """A command line tool to compute mapping statistics from a BAM file."""

    homepage = "https://github.com/guigolab/bamstats"
    url = "https://github.com/guigolab/bamstats/archive/refs/tags/v0.3.5.tar.gz"

    maintainers("emi80")

    version("0.3.5", sha256="0b397c0b09c4a944e564dd9e92eb5e9e8408e97cf1a54af07dced8783342b977")
    version("0.3.4", sha256="1b849a78f997e1232ba8c20036fc1e92c7f10f907791f5dfa74bf648546e2340")

    depends_on("go@1.18:")

    def install(self, spec, prefix):
        flags = f'LDFLAGS=-ldflags "-s -w -X main.version={spec.version}"'
        make('install', flags)
