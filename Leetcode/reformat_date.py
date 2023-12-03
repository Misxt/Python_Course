class Solution:
    def reformatDate(self, date: str) -> str:
        list_of_dates = date.split(" ")
        reformatted_date = list_of_dates[2] + "-" + self.month(list_of_dates[1]) + "-" + self.day(list_of_dates[0])
        return reformatted_date
#can be th, st, nd
    def day(self, day):
        txt = day.replace("th", "")
        txt = txt.replace("st", "")
        txt = txt.replace("nd", "")
        txt = txt.replace("rd", "")
        txt = txt
        if len(txt) == 1:
            txt = "0" + txt
        return txt
    
    def month(self, month):
        date_converter = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}
        return date_converter[month]
