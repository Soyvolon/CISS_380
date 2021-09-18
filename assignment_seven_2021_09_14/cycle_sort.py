def cycle_sort(data: list):
    cap = len(data)
    for start in range(0, cap - 1):
        # get item
        item = data[start]
        # get new pos for said item
        pos = start
        for i in range(start + 1, cap):
            if data[i] < item:
                pos += 1
        # if there isnt a new pos, skip this, we don't move it
        if start == pos:
            continue
        # skip past any any duplicates
        while data[pos] == item:
            pos += 1
        # set the item to the pos
        # and get the next item to move
        data[pos], item = item, data[pos]

        # take the new item and move
        # it backwards until
        # it is in its correct spot
        while pos != start:
            pos = start
            # get the new pos value
            for i in range(start + 1, cap):
                if data[i] < item:
                    pos += 1
            # skip duplicates
            while data[pos] == item:
                pos += 1
            # and place item at data[pos] and prep
            # data[pos] to be moved to the next spot
            data[pos], item = item, data[pos]
