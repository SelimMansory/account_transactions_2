import json
from src import utils


date = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2019-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  }]

test_date = date
test_date.sort(key=lambda x: x['date'])
test_date.reverse()

with open("operations.json", encoding="utf-8") as file:
    text = json.load(file)
test_text = 'tests/operations.json'
def test_open_file():
  assert utils.open_file(test_text) == text

def test_check_state_and_sorted():
    assert utils.check_state_and_sorted([{}]) == []
    assert utils.check_state_and_sorted(date) == test_date

def test_output_last_operations():
    assert utils.output_last_operations(test_date) == ['26.08.2019 Перевод организации Maestro\n'
 '1596 83** **** 5199 -> Счет **9589\n'
 '31957.58 руб.\n',
 '19.08.2019 Перевод с карты на карту Visa Classic\n'
 '6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229 \n'
 '    56883.54 USD\n',
 '12.07.2019 Перевод организации \nСчет **4368 -> Счет **8358\n51463.70 USD\n',
 '03.07.2019 Перевод организации MasterCard\n'
 '7158 30** **** 6758 -> Счет **5560\n'
 '8221.37 USD\n',
 '23.03.2019 Перевод со счета на счет \n'
 'Счет **4719 -> Счет **1160\n'
 '43318.34 руб.\n']