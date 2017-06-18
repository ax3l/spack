##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
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


class Libwebsockets(CMakePackage):
    """C library for lightweight websocket clients and servers."""

    homepage = "https://github.com/warmcat/libwebsockets"
    url      = "https://github.com/warmcat/libwebsockets/archive/v2.1.0.tar.gz"

    version('2.1.0', '4df3be57dee43aeebd54a3ed56568f50')
    version('2.0.3', 'a025156d606d90579e65d53ccd062a94')
    version('1.7.9', '7b3692ead5ae00fd0e1d56c080170f07')

    variant('zlib', default=True, description='Include zlib support (required for extensions)')
    variant('libevent', default=True, description='Compile with support for libevent (for callbacks)')
    variant('openssl', default=True, description='Include SSL support (default OpenSSL)')

    depends_on('zlib', when='+zlib')
    depends_on('libevent', when='+libevent')
    depends_on('openssl', when='+openssl')

    def cmake_args(self):
        spec = self.spec

        cmake_args = [
            '-DLWS_WITH_SSL:BOOL={0}'.format((
                'ON' if '+openssl' in spec else 'OFF')),
            '-DLWS_WITH_LIBEVENT:BOOL={0}'.format((
                'ON' if '+libevent' in spec else 'OFF')),
            '-DLWS_WITH_ZLIB:BOOL={0}'.format((
                'ON' if '+zlib' in spec else 'OFF')),
            '-DLWS_WITHOUT_EXTENSIONS:BOOL={0}'.format((
                'ON' if '-zlib' in spec else 'OFF')),
        ]
        return cmake_args
