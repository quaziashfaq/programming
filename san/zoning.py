#!/usr/bin/env python3

import sys

print(len(sys.argv))

# 1st is host file
hosts_alias = open(sys.argv[1]).readlines()
storage_alias = open(sys.argv[2]).readlines()

hosts_alias = [x.strip() for x in hosts_alias]
storage_alias = [x.strip() for x in storage_alias]

print(hosts_alias)
print(storage_alias)
print('')

s = ''
zonenames = []
for host in hosts_alias:
    zonename = 'Z_' + host + '__' + storage_alias[0]
    zonenames.append(zonename)
    s = 'zonecreate ' + zonename  + ', "' + host + '; '
    aliases = '; '.join(storage_alias[1:])
    s += aliases + '"'
    print(s)

print('')
print('Zone names:',  '; '.join(zonenames))
