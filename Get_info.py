import os
import re


class Get_Info(object):
    
    def __init__(self):
        PATH = ((os.path.abspath('.'))+'\\info_config')
        os.system('dxdiag /t '+PATH)
        with open(PATH+'.txt','rb') as f:
            l = f.read().decode('gb2312')
        os.remove(PATH+'.txt')
        self.info = l

    def get_info_cpu(self): 
        cpu_name = re.sub(r'(\().*?(\))','',re.findall(r'Processor: .*',self.info)[0][11:-1]).split()
        if cpu_name[0] == 'Intel':
            cpu_name = ' '.join(cpu_name[:3])+' @ '+cpu_name[cpu_name.index('@')+1] 
        else:
            cpu_name = ' '.join(cpu_name[:3]) 
        return {'cpu_name':cpu_name}

    def get_info_video(self):
        video_name = ''
        try:
            video_name = ' '.join(re.findall(r'Chip type: .*',self.info)[0][11:-1].split())
        except:
            pass
        return {'video_name':video_name}

    def get_info_hard(self):     
        # 获得硬盘信息
        size = os.popen('wmic DISKDRIVE get size').read()
        hard_size = re.findall(r'\w.+\w',size)[1:]
        name = os.popen('wmic DISKDRIVE get Caption').read()
        hard_name = re.findall(r'\w.+\w',name)[1:]
        
        return {'hard_size':hard_size,'hard_name':hard_name}

    def get_info_bank(self):
        # 获取内存信息
        name = os.popen('wmic memorychip get PartNumber').read()
        bank_name = re.findall(r'\w.+\w',name)[1:]
        size = os.popen('wmic memorychip get Capacity').read() 
        bank_size = re.findall(r'\w.+\w',size)[1:]

        return {'bank_name' : bank_name, 'bank_size':bank_size}

if __name__ == '__main__':
    info = Get_Info()
    print(info.get_info_hard())
    print(info.get_info_bank())
    print(info.get_info_cpu())
    print(info.get_info_video())
