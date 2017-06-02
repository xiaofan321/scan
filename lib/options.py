# coding=utf-8
# import config
from optparse import OptionParser,OptionGroup

def oparser():
    # 处理参数
    parser = OptionParser(usage="python main.py [options]", version="1.0")

    # 必选参数
    group = OptionGroup(parser, 'target(need)') 
    group.add_option("-u", dest="urls", action="store", 
                        help="-u URL| -u  URLFILE") 
    group.add_option("-r", dest="pocfile", action="store", 
                        help="a file | a directory")

    # 可选参数
    group2 = OptionGroup(parser, "other(select)") 
    group2.add_option("-t", dest="thread", action="store", type="int", default=30,
                       help="-t 30 thread number(default 30)") 
    group2.add_option("-o", dest="out", action="store", 
                        help="-u URL| -u  URLFILE") 

    parser.add_option_group(group) 
    parser.add_option_group(group2) 

    (options,args)=parser.parse_args()

    if not options.urls or not options.pocfile:  
        parser.error("options -u or -r are need")  

    return options

if __name__ == "__main()__":
    oparser()