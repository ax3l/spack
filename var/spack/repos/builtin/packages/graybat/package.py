##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Graybat(CMakePackage):
    """Graph Approach for Highly Generic Communication Schemes Based on Adaptive Topologies"""

    homepage = "https://github.com/ComputationalRadiationPhysics/graybat"
    url      = "https://github.com/ComputationalRadiationPhysics/graybat/archive/1.2.0.tar.gz"

    version('dev', branch='remove_grpc',
            git='https://github.com/fabian-jung/graybat.git')
    version('master', branch='master',
            git='https://github.com/ComputationalRadiationPhysics/graybat.git')
    version('1.2.0', 'd47200e99d712d33e6e6a5f0ad946c6a')

    build_targets = ['all', 'signaling']

    # C++14
    conflicts('%gcc@:5')
    conflicts('%clang@:3.4')

    variant('mpi', default=True,
            description='Enable MPI communication policy')
    variant('zeromq', default=True,
            description='Enable ZeroMQ communication policy')
    variant('metis', default=False,
            description='Enable graph partitioning mapping')

    depends_on('cmake@3.0.2:', type='build')
    depends_on('boost@1.61.0:1.62.0~mpi', type='link', when='~mpi')
    depends_on('boost@1.61.0:1.62.0+mpi', type='link', when='+mpi')
    depends_on('mpi', type='link', when='+mpi')
    depends_on('zeromq@4.2.2:', when='+zeromq')
    # should be included in upcoming 4.2.2+
    depends_on('cppzmq@develop', when='+zeromq')
    depends_on('metis@5.1.0:', type='link', when='+metis')
    depends_on('protobuf', when='@:1.2.0')
    depends_on('grpc@develop', when='@:1.2.0')
