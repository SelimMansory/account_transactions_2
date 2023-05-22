import utils


text = "src/operations.json"
date = utils.open_file(text)
date = utils.check_state_and_sorted(date)

for i in utils.output_last_operations(date):
    print(i)