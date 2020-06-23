# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


def create_formatter(fmt):
    'Returns a table formatter for the specified type'
    if 'txt' == fmt:
        return TextTableFormatter()
    elif 'csv' == fmt:
        return CsvTableFormatter()
    elif 'html' == fmt:
        return HtmlTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

class TextTableFormatter(TableFormatter):
    'Emit a table in plain-text format'
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CsvTableFormatter(TableFormatter):
    'Emit a table in csv format'
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HtmlTableFormatter(TableFormatter):
    'emit a table in html format'
    def headings(self, headers):
        print(f'<th><td>{"</td><td>".join(headers)}</td></th>')

    def row(self, rowdata):
        print(f'<tr><td>{"</td><td>".join(rowdata)}</td></th>')