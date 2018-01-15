import xlrd
import sqlite3

capital_city_dict = {
    '北京': 1, '天津': 2, '上海': 3, '重庆': 4, '石家庄': 5,
    '郑州': 6, '武汉': 7, '长沙': 8, '南京': 9, '南昌': 10,
    '沈阳': 11, '长春': 12, '哈尔滨': 13, '西安': 14, '太原': 15,
    '济南': 16, '成都': 17, '西宁': 18, '合肥': 19, '海口': 20,
    '广州': 21, '贵阳': 22, '杭州': 23, '福州': 24, '兰州': 25,
    '昆明': 26, '拉萨': 27, '银川': 28, '南宁': 29, '乌鲁木齐': 30,
    '呼和浩特': 31
}

def isCapital(cityName):

    for key in capital_city_dict:
        if key == cityName:
            return True
    else:
        return False

def main():

    # inputexcel = 'G:\\code\\newfolder\\static\\capital_city_train_station_code - 副本.xlsx'
    inputexcel = '..\\static\\capital_city_train_station_code - 副本.xlsx'

    workbook = xlrd.open_workbook(inputexcel)
    booksheet = workbook.sheet_by_index(0)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('create table capital_city_train_station_sim (stationName varchar(20), teleCode varchar(10), cityName varchar(20))')
    deleteSql = """delete from capital_city_train_station_sim"""
    cursor.execute(deleteSql)


    for row in range(0, booksheet.nrows):
        row_data = []
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            val = str(val)
            row_data.append(val)
        # if isCapital(row_data[6]):
        #     stationId = row_data[0]
        #     stationName = row_data[1]
        #     pinYin = row_data[2]
        #     pinYinHead = row_data[3]
        #     firstLetter = row_data[4]
        #     teleCode = row_data[5]
        #     cityName = row_data[6]
        #     longitude = row_data[7]
        #     latitude = row_data[8]
        #     cursor.execute(
        #             "insert into capital_city_train_station(stationId, stationName, pinYin, pinYinHead, firstLetter, teleCode, cityName, longitude, latitude) values(?, ?, ?, ?, ?, ?, ?, ?, ?)",
        #             (stationId, stationName, pinYin, pinYinHead, firstLetter, teleCode, cityName, longitude, latitude))
        #     conn.commit()

        stationName = row_data[1]
        teleCode = row_data[5]
        cityName = row_data[6]

        cursor.execute("insert into capital_city_train_station_sim(stationName, teleCode, cityName) values(?, ?, ?)",
                        (stationName, teleCode, cityName))
        conn.commit()
    cursor.close()

    conn.close()
    print('finished')
if __name__ == '__main__':
    main()