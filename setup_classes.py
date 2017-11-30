class DBBase:
    _counter = None
    _open_msg = None
    _close_msg = None

    def __init__(self):
        """Creates an instance"""
        self.count = self._counter
        type(self)._counter += 1
        print(f'\n\n###################### {self._open_msg}: {self.count}')

    def close(self):
        """Closes instance"""
        print(f'\n\n###################### {self._close_msg}: {self.count}')


class Connection(DBBase):
    _counter = 1
    _open_msg = 'Opening Costly DB Connection'
    _close_msg = 'Closing Costly DB Connection'


class Session(DBBase):
    _counter = 1
    _open_msg = 'Opening Cheap DB Session'
    _close_msg = 'Rolling Back Cheap DB Session'


if __name__ == '__main__':
    db_objects = [Connection() for i in range(3)]
    db_objects.extend([Session() for i in range(3)])
    for conn in db_objects:
        conn.close()
