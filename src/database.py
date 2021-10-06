def prefix_matches(line, pattern):
  if len(line) > len(pattern) and line[:len(pattern)] == pattern:
    return True
  else:
    return False


class Database:

  def __init__(self,
               datafile,
               row_delimeter='\n',
               col_delimeter='\t',
               comment_prefix='##',
               colomnset_prefix='#'):
    self._row_delimeter = row_delimeter
    self._col_delimeter = col_delimeter

    with open(datafile) as df:
      data = df.read()
      lines = data.split(row_delimeter)

      # preprocess
      self._comments = []
      linenum = 0
      while linenum < len(lines):
        line = lines[linenum]
        if prefix_matches(line, comment_prefix):
          lines.remove(line)
          self._comments.append(line)
        else:
          linenum += 1

      # get column's infomation
      for line in lines:
        if prefix_matches(line, colomnset_prefix):
          self._cols_info = line.split(col_delimeter)
          self._total_cols = len(self._cols_info)

      # get fixed column's infomation
      self._total_fixed_cols = 9

      # build database
      self._indexes = None
      self._rows = [line.split(col_delimeter) for line in lines]

  def __iter__(self):
    current = 0
    while current < self._total_cols:
      yield self.__getitem__(current)
      current += 1

  def __getitem__(self, key):
    row = self._rows[key]
    if not self._indexes:
      return self._col_delimeter.join(row)
    else:
      selected_row = [row[i] for i in self._indexes]
      return self._col_delimeter.join(selected_row)

  def set_filter(self, keys):
    indexes = [self._cols_info.index(key) for key in keys]
    self._indexes = list(range(0, self._total_fixed_cols))
    self._indexes.extend(indexes)