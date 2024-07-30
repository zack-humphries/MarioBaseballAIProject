# SPDX-License-Identifier: MIT
'''
This file is based on Yoshi2's dolphin-memory-lib
https://github.com/RenolY2/dolphin-memory-lib
  Copyright (c) 2022 Yoshi2, NerduMiner

The find_dolphin function is based on WindowsDolphinProcess::findPID() from
aldelaro5's Dolphin memory engine
https://github.com/aldelaro5/Dolphin-memory-engine
  Copyright (c) 2017 aldelaro5

This file is based on sms's sup-dolphin-memory-lib

https://forgejo.sup39.dev/sms/sup-dolphin-memory-lib
  Copyright (c) 2022 sup39

'''

import os
from psutil import process_iter
from struct import pack, unpack, calcsize
from multiprocessing.shared_memory import SharedMemory

dolphinProcNames = \
  ('Dolphin.exe', 'DolphinQt2.exe', 'DolphinWx.exe', 'Project Rio.exe') if os.name == 'nt' \
  else ('dolphin-emu', 'dolphin-emu-qt2', 'dolphin-emu-wx')

def find_dolphin(self=None):
  return [
    proc.pid
    for proc in process_iter()
    if proc.name() in dolphinProcNames
  ][::-1] # newest to oldest

'''
@typedef {(int|str) | [(int|str), ...int[]]} Addr
  -- address or symbol name with arbitrary offsets
  -- e.g. 0x8040A378, 'gpMarioOriginal',
  --      (0x8040A2A8, 0x54), ('gpMap', 0x10, 0x04)
'''

class Dolphin():
  def __init__(self):
    self.pid = None
    self.memory = None
  def reset(self):
    self.pid = None
    self.memory = None
  def hook(self, pids=None):
    '''
      @params pids {None|int|Iterable<int>}
        -- pid or pid array of dolphin
      @returns {int|None}
        -- pid of hooked dolphin
    '''
    self.memory = None
    # init pids
    if pids is None: # auto-detect
      pids = Dolphin.find_dolphin()
    elif type(pids) is int: # pid -> [pid]
      pids = [pids]
    ## no process found
    if len(pids) == 0: return None
    # init memory
    for pid in pids:
      memory = Dolphin.init_shared_memory(pid)
      if memory is not None:
        self.pid = pid
        self.memory = memory
        return pid
    ## no memory found
    print("ERROR")
    return None

  # virtual methods
  def get_symb_addr(self, name):
    '''
      @params {str} name
        -- name of the symbol
      @returns {int|never}
        -- addr of the symbol
    '''
    raise NotImplemented

  # private methods
  def _get_slice(self, addr, size):
    '''
      @params {int} addr
        -- memory address
      @params {int} size
        -- size of memory slice
      @returns {slice|never}
        -- slice object for self.memory at the address
    '''
    idx = addr - 0x8000_0000
    assert 0 <= idx < 0x0180_0000
    return slice(idx, idx+size)
  def _read_bytes(self, addr, size=1):
    '''
      @params {int} addr
        -- memory address
      @params {int} size
        -- size to read
      @returns {bytes|never}
        -- bytes at the address
    '''
    return self.memory.buf[self._get_slice(addr, size)].tobytes()
  def _write_bytes(self, addr, data):
    '''
      @params {int} addr
        -- memory address
      @params {bytes} data
        -- bytes to write
    '''
    self.memory.buf[self._get_slice(addr, len(data))] = data

  # public methods
  def try_resolve_addr(self, addr):
    '''
      @params {Addr} addr
        -- address or symbol name with arbitrary offsets
      @returns {int|None}
        -- (resolved address) or (None if NullPointerException occurred)
    '''
    try: addr, *offsets = addr
    except TypeError: offsets = []
    # resolve base
    if type(addr) == str:
      addr = self.get_symb_addr(addr)
    # offset
    for off in offsets:
      # dereference
      addr = unpack('>I', self._read_bytes(addr, 4))[0]
      # check nullptr
      if addr == 0: return None
      # add offset
      addr += off
    return addr
  def read_bytes(self, addr, size=1):
    '''
      @params {Addr} addr
        ## See `addr` of `try_resolve_addr()`
      @params {int} size
        -- size to read
      @returns {bytes|None}
        -- (bytes at addr) or (None if NullPointerException occurred)
    '''
    addr = self.try_resolve_addr(addr)
    if addr is None: return None
    return self._read_bytes(addr, size)
  def write_bytes(self, addr, data):
    '''
      @params {Addr} addr
        ## See `addr` of `try_resolve_addr()`
      @params {bytes} data
        -- bytes to write
      @returns {int|None}
        -- (written address) or (None if NullPointerException occurred)
    '''
    addr = self.try_resolve_addr(addr)
    if addr is None: return None
    self._write_bytes(addr, data)
    return addr
  def read_struct(self, addr, fmt):
    '''
      @params {Addr} addr
        ## See `addr` of `try_resolve_addr()`
      @params {int} size
        -- size to read
      @returns {bytes|None}
        ## See `addr` of `read_bytes()`
    '''
    data = self.read_bytes(addr, calcsize(fmt))
    return None if data is None else unpack(fmt, data)
  def write_struct(self, addr, fmt, *args):
    '''
      @params {Addr} addr
        ## See `addr` of `try_resolve_addr()`
      @params {str} fmt
        -- format string for struct.pack
      @params {...} *args
        -- args for struct.pack(fmt, *args)
      @returns {int|None}
        ## See `addr` of `write_bytes()`
    '''
    return self.write_bytes(addr, pack(fmt, *args))

  ## read single value from memory
  '''
    @params {Addr} addr
      ## See `addr` of `try_resolve_addr()`
    @returns {bytes|None}
      ## See `addr` of `read_bytes()`
  '''
  def read_uint32(self, addr): return self.read_struct(addr, '>I')[0]
  def read_uint16(self, addr): return self.read_struct(addr, '>H')[0]
  def read_uint8(self, addr): return self.read_struct(addr, '>B')[0]
  def read_int32(self, addr): return self.read_struct(addr, '>i')[0]
  def read_int16(self, addr): return self.read_struct(addr, '>h')[0]
  def read_int8(self, addr): return self.read_struct(addr, '>b')[0]
  def read_float(self, addr): return self.read_struct(addr, '>f')[0]


  def read(self, addr, type: str):
    if type == 'int8':
      return self.read_struct(addr, '>b')[0]
    elif type == 'uint8':
      return self.read_struct(addr, '>B')[0]
    elif type == 'float':
      return self.read_struct(addr, '>f')[0]
    elif type == 'int16':
      return self.read_struct(addr, '>h')[0]
    elif type == 'uint16':
      return self.read_struct(addr, '>H')[0]
    elif type == 'int32':
      return self.read_struct(addr, '>i')[0]
    elif type == 'uint32':
      return self.read_struct(addr, '>I')[0]
    return AttributeError

  ## write single value to memory
  '''
    @params {Addr} addr
      ## See `addr` of `try_resolve_addr()`
    @params {...} val
      -- value to write
    @returns {int|None}
      ## See `addr` of `write_bytes()`
  '''
  def write_uint32(self, addr, val): return self.write_struct(addr, '>I', val)
  def write_uint16(self, addr, val): return self.write_struct(addr, '>H', val)
  def write_uint8(self, addr, val): return self.write_struct(addr, '>B', val)
  def write_int32(self, addr, val): return self.write_struct(addr, '>i', val)
  def write_int16(self, addr, val): return self.write_struct(addr, '>h', val)
  def write_int8(self, addr, val): return self.write_struct(addr, '>b', val)
  def write_float(self, addr, val): return self.write_struct(addr, '>f', val)

  def write(self, addr, type: str, val):
    if type == 'int8':
      return self.write_struct(addr, '>b', val)[0]
    elif type == 'uint8':
      return self.write_struct(addr, '>B', val)[0]
    elif type == 'float':
      return self.write_struct(addr, '>f', val)[0]
    elif type == 'int16':
      return self.write_struct(addr, '>h', val)[0]
    elif type == 'uint16':
      return self.write_struct(addr, '>H', val)[0]
    elif type == 'int32':
      return self.write_struct(addr, '>i', val)[0]
    elif type == 'uint32':
      return self.write_struct(addr, '>I', val)[0]
    return AttributeError


  # static methods
  def init_shared_memory(pid):
    try: return SharedMemory('dolphin-emu.'+str(pid))
    except FileNotFoundError: return None
  find_dolphin = find_dolphin


def main():
  dolphin = Dolphin()

  while True:
    if dolphin.hook():
      print(str(dolphin.read_int8(0x803c77b8)) + "   " + str(dolphin.read_int8(0x803c77b9)))
    else:
      break

if __name__ == '__main__':
  main()
