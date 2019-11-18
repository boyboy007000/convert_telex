import re
import sys
import os
#ref: sangnd.wordpress.com
patterns = {
#     '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
#     '[đ]': 'd',
#     '[èéẻẽẹêềếểễệ]': 'e',
#     '[ìíỉĩị]': 'i',
#     '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
#     '[ùúủũụưừứửữự]': 'u',
#     '[ỳýỷỹỵ]': 'y'
'[á]':'as','[ó]':'os','[ú]':'us','[é]':'es',
'[à]':'af','[ò]':'of','[ù]':'uf','[è]':'ef',
'[ả]':'ar','[ỏ]':'or','[ủ]':'ur','[ẹ]':'ej',
'[ạ]':'aj','[ọ]':'oj','[ụ]':'uj','[ẻ]':'er',
'[ã]':'ax','[õ]':'ox','[ũ]':'ux','[ẽ]':'ex',
'[â]':'aa','[ô]':'oo','[ư]':'uw','[ê]':'ee',
'[ă]':'aw','[ơ]':'ow','[ứ]':'uws','[ể]':'eer',
'[ấ]':'aas','[ố]':'oos','[ừ]':'uwf','[ễ]':'eex',
'[ầ]':'aaf','[ồ]':'oof','[ử]':'uwr','[ế]':'ees',
'[ậ]':'aaj','[ộ]':'ooj','[ữ]':'uwx','[ề]':'eef',
'[ẩ]':'aar','[ổ]':'oor','[ự]':'uwj','[ệ]':'eej',
'[ẫ]':'aax','[ỗ]':'oox','[đ]':'dd','[ý]':'ys',
'[ắ]':'aws','[ớ]':'ows','[í]':'is','[ỳ]':'yf',
'[ằ]':'awf','[ờ]':'owf','[ì]':'if','[ỷ]':'yr',
'[ặ]':'awj','[ợ]':'owj','[ị]':'ij','[ỹ]':'yx',
'[ẳ]':'awr','[ở]':'owr','[ỉ]':'ir','[ỵ]':'yj',
'[ẵ]':'awx','[ỡ]':'owx','[ĩ]':'ix',

}

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    
    
    output = text
   
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output
str=input('nhap chuoi ' )

print(convert(str))
scr=('/home/anguyen/Speech_recognition/words/wav/male1/')
dst=('/home/anguyen/Speech_recognition/words/wav/male1/unmark/')
for filename in os.listdir(scr):
   # print(convert(filename))
    temp=scr+filename
    temp2=convert(filename)
    dst=scr+temp2
    os.rename(temp, dst, src_dir_fd=None, dst_dir_fd=None)
f=open('/home/anguyen/Speech recognition/words/wav/t.txt','r')
a=open('/home/anguyen/Speech recognition/words/wav/ta.txt','w')
for i in f:
    print(i)
    print(convert(i))
    a.write(convert(i))
a.close()
f.close()

