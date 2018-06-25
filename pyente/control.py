import subprocess


class Control:
    def __init__(self, relaisctl_path='./relaisctl'):
        self.relaisctl_path = relaisctl_path

    def activate(self, machine):
        status, output = subprocess.getstatusoutput(
                '{} {:d}'.format(self.relaisctl_path, machine))
        print('[relaisctl] ' + output)
        if status != 0:
            raise RuntimeError(
                    'Activation failed with status {:d}!'.format(status))
