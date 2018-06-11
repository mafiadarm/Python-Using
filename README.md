---
运用在生产环境的实例
---

# Python-Using

check_table_project

​	人资使用，打卡机导出打卡资料，对比员工信息及上下班信息等，汇成最终的excel报表

copy_data_backup

​	服务器数据库备份定期复制到其他网络映射盘

e_mail_send_payroll

​	人资使用，根据员工邮箱信息，批量通过邮件发工资条

data_views

​	数据可视化的尝试性使用，对公司数据进行分析



dataBase_Form_import_export.py

​	sqlserver的python包的尝试性使用

ListeRaid.py

​	监控raid状态

Single_Process_copy_data.py

​	早期使用的单线程拷贝文件到指定位置

threading_pool_copy_data.py

​	多线程拷贝文件到指定位置，受制于内存大小

split_copy_data.py

​	优化后的多线程拷贝文件，把大小文件分开，小文件使用多线程，大文件使用单线程，保证同等内存大小的情况下，能最优化的运行