import json


def open_file(text):
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)


def check_state_and_sorted(date):
    """Проверка на успешность операции с удалением не успешной операции, удалением пустых значений
    и сортировка данных по дате в обратном порядке"""
    for i in reversed(range(len(date))):
        if 0 == len(date[i]) or date[i]["state"] == "CANCELED":
            date.remove(date[i])
    date.sort(key=lambda x: x['date'])
    date.reverse()
    return date


def output_last_operations(date):
    """Вывод последних 5 операций"""
    last_operations = []
    for i in range(5):
        if 'from' in date[i] and 'Счет' in date[i]['from'] and 'Счет' in date[i]['to']:
            """"Перевод со счета на счет"""
            last_operations.append(f"""{date[i]["date"][8:10] + "." + date[i]['date'][5:7] + '.' + date[i]['date'][:4]} \
{date[i]['description']} 
{date[i]['from'][:5] + "**" + date[i]['from'][-4:]} -> \
{date[i]['to'][:5] + "**" + date[i]['to'][-4:]}
{date[i]['operationAmount']['amount']} {date[i]['operationAmount']['currency']['name']}\n""")
        elif 'from' in date[i] and 'Счет' not in date[i]['from'] and 'Счет' in date[i]['to']:
            """Перевод с карточки на счет"""
            last_operations.append(f"""{date[i]["date"][8:10] + "." + date[i]['date'][5:7] + '.' + date[i]['date'][:4]} \
{date[i]['description']} {date[i]['from'][:-17]}
{date[i]['from'][-16:-12] + " " + date[i]['from'][-12:-10] + "** **** " + date[i]['from'][-4:]} -> \
{date[i]['to'][:5] + "**" + date[i]['to'][-4:]}
{date[i]['operationAmount']['amount']} {date[i]['operationAmount']['currency']['name']}\n""")
        elif 'from' in date[i] and 'Счет' not in date[i]['from'] and 'Счет' not in date[i]['to']:
            """Перевод с карточки на карточку"""
            last_operations.append(f"""{date[i]["date"][8:10] + "." + date[i]['date'][5:7] + '.' + date[i]['date'][:4]} \
{date[i]['description']} {date[i]['from'][:-17]}
{date[i]['from'][-16:-12] + " " + date[i]['from'][-12:-10] + "** **** " + date[i]['from'][-4:]} -> \
{date[i]['to'][:-17]} {date[i]['to'][-16:-12] + " " + date[i]['to'][-12:-10] + "** **** " + date[i]['to'][-4:]} 
    {date[i]['operationAmount']['amount']} {date[i]['operationAmount']['currency']['name']}\n""")
        else:
            """Открытие вклада"""
            last_operations.append(f"""{date[i]["date"][8:10] + "." + date[i]['date'][5:7] + '.' + date[i]['date'][:4]}\
 {date[i]['description']}
{date[i]['to'][:5] + "**" + date[i]['to'][-4:]}
{date[i]['operationAmount']['amount']} {date[i]['operationAmount']['currency']['name']}\n""")
    return last_operations