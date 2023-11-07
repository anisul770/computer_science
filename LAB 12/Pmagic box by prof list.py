import csv

number_of_boxes = 42


def give_item(magic_boxes, item_name):
    in_a_box = False
    box_with_item = None
    for box in magic_boxes:
        if item_name in box:
            in_a_box = True
            box_with_item = box
    empty_box = 0
    last_empty_box = None
    for box in magic_boxes:
        if len(box) == 0:
            empty_box += 1
            last_empty_box = box
    if empty_box == 0 and not in_a_box:
        raise Exception('Error with bob')
    if not in_a_box:
        last_empty_box.append(item_name)
    else:
        box_with_item.append(item_name)


def take_item(magic_boxes, item_name):
    in_a_box = False
    box_with_item = None
    for box in magic_boxes:
        if item_name in magic_boxes:
            in_a_box = True
            box_with_item = box
    if not in_a_box:
        raise Exception("Carl not take")
    box_with_item.pop()


def main():
    log_file_name = 'log.csv'
    log_file = open(log_file_name, 'w')
    log_writer = csv.writer(log_file)
    log_writer.writerow(['Actor', 'Action', 'Item'])
    magic_box = list()
    for i in range(number_of_boxes):
        magic_box.append(list())
    with open('actions.txt', 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            if line.startswith('Bob'):
                item_name = line.replace('Bob gives a ', '').strip()
                log_writer.writerow(['Bob', 'give', item_name])
                try:
                    give_item(magic_box, item_name)
                except Exception as e:
                    log_writer.writerow(['Bob', 'Error', item_name])
                    raise e
            elif line.startswith('Carl'):
                item_name = line.replace('Carl takes a ', '').strip()
                log_writer.writerow(['Carl', 'take', item_name])
                try:
                    take_item(magic_box, item_name)
                except Exception as e:
                    log_writer.writerow(['Carl', 'Error', item_name])
                    raise e


if __name__ == '__main__':
    main()
