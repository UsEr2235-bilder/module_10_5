import time
from multiprocessing import Pool

def read_info(name):
    """Функция для чтения данных из файла построчно."""
    all_data = []
    try:
        with open(name, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line.strip())
    except Exception as e:
        print(f"Ошибка при чтении файла {name}: {e}")

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейное время выполнения: {linear_duration:.2f} секунд")
#Линейное время выполнения: 6.24 секунд

    # Многопроцессный вызов
    start_time = time.time()
    with Pool(processes=8) as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.time() - start_time
    print(f"Многопроцессное время выполнения: {parallel_duration:.2f} секунд")
#Многопроцессное время выполнения: 2.47 секунд