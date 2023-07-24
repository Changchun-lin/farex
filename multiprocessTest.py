from multiprocessing import Process
def fuc1(name):
    print('测试%s多进程' %name)

if __name__ == '__main__':
    process_list = []
    for i in range(5):
        p = Process(target=fuc1, args=(i,))
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()

    print('结束测试')
