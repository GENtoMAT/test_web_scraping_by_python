import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import datetime
from gspread_formatting import *
import os.path


class SpreadSheet:
    # 初期化(認証情報読み込み,ワークブックID指定)
    def __init__(self):
        appsetting = json.load(open("secrets_json/settings.json", "r"))
        self.id = appsetting["gspshiId"]
        self.sheetName = appsetting["sheetName"]
        self.jsonPath = appsetting["credentialJsonPath"]

        base = os.path.dirname(os.path.abspath(__file__))
        json_file = os.path.normpath(os.path.join(base, self.jsonPath))

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # スプレッドシートにアクセス
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
        self.gc = gspread.authorize(credentials)

    # spread sheetへアクセス
    def access(self):
        res = self.gc.open_by_key(self.id)
        return res

    # スプレッドシートのワークシートを開く
    def readSheet(self, sheet: str):
        # アクセス
        book = self.access()
        sheet = book.worksheet(sheet)
        return sheet

    # セルを指定してデータを取得
    def getVal(self, cell: str):
        sheet = self.readSheet(self.sheetName)
        val_cell = sheet.acell(cell).value
        return val_cell

    # １セルの値を更新
    def updateOneCell(self, cell: str, text: str):
        sheet = self.readSheet(self.sheetName)
        sheet.update_acell(cell, text)

    # 任意の場所から任意の列数を追加
    def addColsFromLeft(self, startCols: int, addNum: int):
        sheet = self.readSheet(self.sheetName)
        sheet.insert_cols([[]] * addNum, col=startCols)

    # 取得したデータを複数セルに一括書き込み
    def updateCellsVertical(self, setCol: str, rowStart: int, rowEnd: int, data: list):
        sheet = self.readSheet(self.sheetName)
        cell_list = sheet.range(setCol + str(rowStart) + ":" + setCol + str(rowEnd))
        for i, cell in enumerate(cell_list):
            cell.value = data[i]
        sheet.update_cells(cell_list, value_input_option="USER_ENTERED")


if __name__ == "__main__":
    s = SpreadSheet()
