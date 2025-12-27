import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser( description="Скрипт обробляє лог-файл та приймає необов'язковий аргумент.")
    # Обов'язковий аргумент: шлях до лог-файлу
    parser.add_argument('log_file_path', type=str, help='Шлях до файлу логів, який потрібно обробити.')
    # Необов'язковий аргумент: додаткова опція (наприклад, рівень логування)
    parser.add_argument( '--level', type=str, default='INFO', # Значення за замовчуванням
        help='Рівень логування (наприклад, DEBUG, INFO, WARNING). За замовчуванням: INFO.')
    args = parser.parse_args()
    # ф-ція для завантаження логів з файлу та отримання списку словників
    def load_logs(file_path: str) -> list:
        path = Path(file_path)
        my_list = []
        try:
            if path.exists():
                with open(path, 'r', encoding='utf-8') as file:
                    for line in file:
                        my_list.append(parse_log_line(line))
                return my_list
        except FileNotFoundError:   
            return print("Файл 'salary_file' не існує ") 
        except (ValueError,IOError):
                    return print("Помилка при обробці файлу")
    # ф-ція для парсингу рядка логу у словник    
    def parse_log_line(line: str) -> dict:
        parts = line.split()
        log_entry = {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": " ".join(parts[3:])
        }
        return log_entry
    # ф-ція для фільтрації логів за рівнем логування
    def filter_logs_by_level(logs: list, level: str) -> list:
        filtered_logs = [log for log in logs if log['level'] == level]
        return filtered_logs
    # ф-ція для підрахунку кількості логів за рівнем та сортування за спаданням
    def count_logs_by_level(logs: list) -> dict:
        counts = {}
        for log in logs:
            level = log['level']
            if level in counts:
                counts[level] += 1
            else:
                counts[level] = 1
        sorted_items_desc = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_items_desc)        
        return sorted_dict
    # ф-ція для виведення підрахунку логів за рівнем у форматованому вигляді та виведення відфільтрованих логів
    def display_log_counts(sorted_dict: dict):
        print(f'{"Рівень логування":<20} {"|":^5} {"Кількість":<15}')
        print(f'{"--------------------"} {"|":^5} {"---------------":<15}')
        for level, count in sorted_dict.items():
            print(f'{level:<20} {"|":^5} {count:<15}')
            

    logs = load_logs(args.log_file_path)
    if args.level :
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        print(f"Деталі логів для рівня '{args.level}':")
        filtered_logs = filter_logs_by_level(logs, args.level)
        for item in filtered_logs:
             print(item)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
if __name__ == "__main__":
    main()


