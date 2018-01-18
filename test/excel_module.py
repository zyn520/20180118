import xlrd

class ExcelUit():
    def __init__(self,excelPath,sheetName):
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        #获取第一行作为Key的值
        self.keys=self.table.row_values(0)
        print(self.keys)
        #获取总行数
        self.row=self.table.nrows
        #获取总列数
        self.col=self.table.ncols

    def dict_data(self):
        if self.row<=1:
            print("总行数小于一")
        else:
            r=[]
            j=1
            for i in range(self.row-1):
                d={}
                #从第二行取对应的value值
                values=self.table.row_values(j)
                for x in range(self.col):
                    d[self.keys[x]]=values[x]
                r.append(d)
                j+=1
            return r
if __name__ == '__main__':
    filepath=r'F:\test_login.xlsx'
    sheet='Sheet1'
    name=ExcelUit(filepath,sheet)
    print(name.dict_data())

