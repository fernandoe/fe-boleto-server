from cnab400.layout.remessa import HEADER


class ArquivoRemessa(object):
    def __init__(self, data_header, default_values):
        self.header = HEADER
        self.data_header = data_header

    def initialize_header(self):
        row = ''
        for key in self.header.keys():
            t = self.header[key]['tipo']
            x, y = self.header[key]['posicao']
            length = (y + 1) - x
            if t == 'X':
                row += ''.ljust(length)
            else:
                row += '%0{D}d'.format(D=length) % 0
        return row
