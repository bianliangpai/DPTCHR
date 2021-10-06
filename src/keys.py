class Keys:

  def __init__(self, filepath, delimeter='\n'):
    self._fp = filepath

    with open(self._fp) as keysfile:
      data = keysfile.read()
      self._keys = data.split(delimeter)
      self._total = len(self._keys)

  def __iter__(self):
    current = 0
    while current < self._total:
      yield self._keys[current]
      current += 1

  def __getitem__(self, key):
    return self._keys[key]