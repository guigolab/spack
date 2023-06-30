# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Sambamba(MakefilePackage):
    """Sambamba: process your BAM data faster (bioinformatics)"""

    homepage = "https://lomereiter.github.io/sambamba/"
    git = "https://github.com/lomereiter/sambamba.git"

    version("1.0.0", tag="v1.0.0", submodules=True)
    version("0.7.1", tag="v0.7.1", submodules=True)
    version("0.6.6", tag="v0.6.6", submodules=True)

    depends_on("ldc~shared", type=("build", "link"))
    depends_on("python", type="build")
    depends_on("lz4", type=("build","link"))

    resource(name="undeaD", git="https://github.com/dlang/undeaD.git", tag="v1.0.7")

    patch("Makefile.patch", when="@0.6.6")

    build_targets = ['static']

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('bin/sambamba-{}'.format(spec.version), '{}/sambamba'.format(prefix.bin))
