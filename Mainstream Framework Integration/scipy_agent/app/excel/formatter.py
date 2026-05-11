import aspose.cells as cells
from aspose.pydrawing import Color


class Formatter:

    def highlight_cell_red(self, sheet, row, col):
        cell = sheet.cells.get(row, col)

        style = cell.get_style()
        style.pattern = cells.BackgroundType.SOLID
        style.foreground_color = Color.red

        cell.set_style(style)