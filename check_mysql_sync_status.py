#!/bin/python
# -*- coding: UTF-8 -*-
import subprocess


# 对比如下信息 是否符合规定
# Master_Log_File     == Relay_Master_Log_File
# Read_Master_Log_Pos == Exec_Master_Log_Pos
# Slave_IO_Running    == Yes
# Slave_SQL_Running   == Yes
# 状态码描述 status : { 0:OK , 1 : WARN  , 2 :CRITICAL  , 3: UNKOWN }


def main():
    #     result = os.popen("mysql -u root -p 'xxxx' -e 'show slave status \G;'").read().split("\n")
    cmd = 'mysql -uroot -p123456 -e "show slave status \G;"'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = result.stdout.read()

    slave_status = {}
    for row in result.split('\n'):
        # print(row)
        # row = row.strip()
        if ":" not in row:
            continue
        k, v = row.split(":", 1)
        k = k.strip()
        v = v.strip()
        # print( "key is " , k , "value is " , v)
        slave_status[k] = v

    status = 3
    try:
        if slave_status["Master_Log_File"] == slave_status["Relay_Master_Log_File"] and slave_status[
            "Read_Master_Log_Pos"] == slave_status["Exec_Master_Log_Pos"] and slave_status[
            "Slave_IO_Running"] == "Yes" and slave_status["Slave_SQL_Running"] == "Yes":
            # OK
            status = 0


        elif slave_status["Slave_IO_Running"] != "Yes" and slave_status["Slave_SQL_Running"] != "Yes":
            # replace slave Error
            status = 2

        elif slave_status["Master_Log_File"] == slave_status["Relay_Master_Log_File"] and slave_status[
            "Read_Master_Log_Pos"] != slave_status["Exec_Master_Log_Pos"] and slave_status[
            "Slave_IO_Running"] == "Yes" and slave_status["Slave_SQL_Running"] == "Yes":
            if int(slave_status["Read_Master_Log_Pos"]) < int(slave_status["Exec_Master_Log_Pos"]) + 10000:
                # OK
                status = 0
            else:
                # Slow_Exec_Master_Log
                status = 1

        elif slave_status["Master_Log_File"] != slave_status["Relay_Master_Log_File"]:
            # Slow_Exec_Master_Log
            status = 2
    except:
        pass
    return status


if __name__ == '__main__':
    print(main())
