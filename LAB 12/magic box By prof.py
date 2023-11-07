number_of_boxes = 42


def give_item(magic_boxes, item_name):
    if item_name not in magic_boxes and len(magic_boxes) == 42:
        raise Exception(f'All the boxes are full, we can not store {item_name}')
    if item_name not in magic_boxes:
        magic_boxes[item_name] = 1
    else:
        magic_boxes[item_name] += 1


def take_item(magic_boxes, item_name):
    if item_name not in magic_boxes:
        raise Exception(f'The Item {item_name} is not inside any boxes')
    magic_boxes[item_name] -= 1
    if magic_boxes[item_name] == 0:
        magic_boxes.pop(item_name)


def main():
    magic_box = dict()
    with open('actions-fail_bob.txt', 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            if line.startswith('Bob'):
                item_name = line.replace('Bob gives a ', '').strip()
                give_item(magic_box, item_name)
            elif line.startswith('Carl'):
                item_name = line.replace('Carl takes a ', '').strip()
                take_item(magic_box, item_name)


if __name__ == '__main__':
    main()
