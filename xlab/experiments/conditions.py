# BSD 3-Clause License
# 
# Copyright (c) 2018, DEMCON advanced mechatronics
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
import collections
import itertools
import random
import sys
import warnings

class Conditions(collections.OrderedDict):
    def __init__(self, *args, **kwargs):
        if sys.version_info < (3, 6) and kwargs:
            warnings.warn('Initializing a Conditions object using keyword '
                          'arguments results in undefined order of the '
                          'variables when using Python < 3.6', 
                          RuntimeWarning)
                
        super().__init__(*args, **kwargs)
        
    def __repr__(self):
        return (
            'Conditions(\n' +
            ''.join('    %s=%r,\n' % x for x in self) +
            '    )'
            )
            
    def __iter__(self):
        return iter(self.items())

    def product(self):
        '''
        Create the product (all combinations of the given variable values)
        
        Returns a new Conditions object
        '''
        variables, values = zip(*self)
        values = itertools.product(*values)
        return Conditions(zip(variables, zip(*list(values))))
    
    def random(self):
        '''
        Randomize the order in which the conditions are measured
        
        Returns a new Conditions object
        '''
        variables, values = zip(*self)
        values = list(zip(*values))
        random.shuffle(values)
        return Conditions(zip(variables, zip(*values)))

if __name__ == '__main__':
    def test():
        cond = Conditions(vset=[1, 2, 3], iset=[3, 4, 6], test=['a', 'b', 'c']) 
       
        print(cond, cond.product(), cond.random(), cond.product().random(), sep='\n')

    test()
