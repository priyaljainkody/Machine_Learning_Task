# import time 
# import multiprocessing

# def calc_square(numbers):
#     print("calculate sqaure: ")
#     for n in numbers:
#         time.sleep(5)
#         print('square: ' + str(n*n))

# def calc_cube(numbers):
#     print("calculate cube: ")
#     for n in numbers:
#         time.sleep(5)
#         print('cube: ' + str(n*n*n))
        
# if __name__ == "__main__":
#     arr = [2,3,8,9]
#     p1 = multiprocessing.Process(target=calc_square, args = (arr,))
#     p2 = multiprocessing.Process(target=calc_cube, args = (arr,))
    
#     t = time.time()
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
#     print("time it took: ", time.time() - t)


# import time
# import threading 
# def calc_square(numbers):
#     # print("debug 1")
#     print("calculate sqaure: ")
#     for n in numbers:
#         # t = time.time()
#         time.sleep(5)
#         print('square: ', n*n)
#         # print("time it took: ", time.time() - t)

# def calc_cube(numbers):
#     # print("debug 2")
#     print("calculate cube: ")
#     for n in numbers:
#         time.sleep(5)
#         print('cube: ', n*n*n)

# arr = [2,3,8,9]
# t = time.time()
# t1 = threading.Thread(target=calc_square, args = (arr,))
# t2 = threading.Thread(target=calc_cube, args = (arr,))
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("time it took: ", time.time() - t)


import threading 
import time 


def worker():
    time.sleep(2)
    print("DONE")

#these are individual independent thread
t1= threading.Thread(target=worker)
t1.start()
t2= threading.Thread(target=worker)
t2.start()
t3= threading.Thread(target=worker)
t3.start()
t4= threading.Thread(target=worker)
t4.start()
t5= threading.Thread(target=worker)
t5.start()
t6= threading.Thread(target=worker)
t6.start()
