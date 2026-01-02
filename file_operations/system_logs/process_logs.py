


all_log_path="file_operations\\system_logs\\all_logs.txt"
error_log_path="file_operations\\system_logs\\error.txt"
wraning_log_path="file_operations\\system_logs\\warning.txt"
info_log_path="file_operations\\system_logs\\info.txt"

fr_log=open(all_log_path,"r")

fw_error=open(error_log_path,"w")

fw_info=open(info_log_path,"w")

fw_waring=open(wraning_log_path,"w")



for line in fr_log:

    log_type=line.rstrip("\n").split(" ")[2].casefold()

    if log_type=="error":   
    

        fw_error.write(line)
    
    elif log_type=="info":

        fw_info.write(line)

    elif log_type=="warning":

        fw_waring.write(line)

    