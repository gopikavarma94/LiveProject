import openpyxl


class ExcelUtility:
    def __init__(self, file_path):
        # Initialize with the file path to the Excel file
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)


    def get_string_data(self, row, col, sheet_name):
        """Get a string value from a specific cell (row, column)"""
        sheet = self.workbook[sheet_name]
        cell = sheet.cell(row=row, column=col)  # openpyxl uses 1-based indexing
        return str(cell.value)
