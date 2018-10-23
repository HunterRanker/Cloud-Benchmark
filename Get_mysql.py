# db = pymysql.connect(host="192.168.199.129",user="xiangmu", password="123456", database="xiangmu", charset="utf8", port = 3306)
import Get_info
class Get_mysql(object):

    def __init__(self,host="127.0.0.1",user="server", password="server", database="xiangmu", charset="utf8", port = 3306):
        import pymysql
        self.db = pymysql.connect(host=host,user=user, password=password, database=database, charset=charset, port = port)

    def get_cpu(self,cpu):
        cpu_name = cpu['cpu_name']
        l = 'cpu.cpu_name,cpu.cpu_marks,cpu.level,cpu_xiangxi.Socket,cpu_xiangxi.Clockspeed,cpu_xiangxi.No_of_Cores,cpu_xiangxi.Max_TDP,cpu_xiangxi.Thread,cpu_xiangxi.Turbo_Speed'
        sql_str = ('SELECT ' + l + ' from cpu,cpu_xiangxi where cpu.cpu_name like "%%%s%%" and cpu.cpu_id=cpu_xiangxi.cpu_id;')%cpu_name.replace(' ','%')
        cursor = self.db.cursor()
        cursor.execute(sql_str)
        p = cursor.fetchone()
        cpu = {}
        for i in map(lambda i,j:(i,j),l.split(','),p):
            cpu[i[0].split('.')[1]] = i[1]
        return cpu

    def get_video(self,video):
        video_name = video['video_name']
        l = 'Videocard_Name,Price,G3D_Mark,Videocard_Value,G2D_Mark,TDP,Power_Perf,Test_Date,Category,Bus_Interface,Max_Memory,Core_Clock,Mem_Clock,Rank,Samples'
        sql_str = ('SELECT ' + l + ' from videos where Videocard_Name like "%%%s%%";')%video_name.replace(' ','%')
        cursor = self.db.cursor()
        cursor.execute(sql_str)
        p = cursor.fetchone()
        video = {}
        for i in map(lambda i,j:(i,j),l.split(','),p):
            video[i[0]] = i[1]
        return video


    def get_hard(self,hard):
        s = len(hard['hard_name'])
        hard_name = hard['hard_name']
        size = hard['hard_size']
        l = 'Name,Disk_Rating,Rank'
        hard = {}
        for i in range(s):
            sql_str = ('SELECT ' + l + ' from hard where Name like "%%%s%%";')%hard_name[i].replace(' ','%')
            cursor = self.db.cursor()
            cursor.execute(sql_str)
            p = cursor.fetchone()
            
            for i in map(lambda i,j:(i,j),l.split(','),p):
                if i[0] in hard:
                    hard[i[0]].append(i[1])
                else:
                    hard[i[0]] = [i[1]]
        hard['hard_size'] = size
        return hard

    def get_bank(self,bank):
        s = len(bank['bank_name'])
        bank_name = bank['bank_name']
        l = 'Name,Read_Uncached,Writee,DDR'
        ban = {}
        for i in range(s):
            sql_str = ('SELECT ' + l + ' from bank where Name like "%%%s%%";')%bank_name[i].replace(' ','%')
            cursor = self.db.cursor()
            cursor.execute(sql_str)
            p = cursor.fetchone()
            for i in map(lambda i,j:(i,j),l.split(','),p):
                if i[0] in ban:
                    ban[i[0]].append(i[1])
                else:
                    ban[i[0]] = [i[1]]
        bank['bank_size'] = bank['bank_size']
        return bank
        
        

if __name__ == '__main__':
    sql = Get_mysql(host="123.207.6.194")
    info = Get_info.Get_Info()

    cpu = info.get_info_cpu()
    video = info.get_info_video()
    hard = info.get_info_hard()
    bank = info.get_info_bank()

    # print(hard)
    # print(cpu)
    # print(video)
    # print(bank)

    print(sql.get_video(video))
    print(sql.get_cpu(cpu))
    print(sql.get_hard(hard))
    print(sql.get_bank(bank))


    


