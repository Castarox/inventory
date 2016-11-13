import csv


def display_inventory(inventory):
    ''' function to display inventory'''
    print('\nInventory:')
    sum = 0 
    for key, value in inventory.items() :
        print(value, key)
        sum += int(value) #sum number of items in inventory
    print('Total number of items: %d' % (sum))


def add_to_inventory(inventory, items):
    ''' add new thigs(list) to inventory'''
    for item in items:
        exist = 0
        for key in inventory:
            if item == key: # if item is allready in our inv increase count
                inventory[key] += 1
                exist += 1
        if exist == 0:
            inventory[item] = 1 #if not add it and set to 1
    return inventory


def print_table(inventory, order=''):
    ''' print inv as table sorted in any order '''
    d_view = [ (value, key) for key, value in inventory.items() ] #conver dic to list
    count_lenght = 5 # count have 5 letter 
    name_length = 9 # item_name ... 
    if order == 'count,desc':  # check in which order display table
        d_view.sort(reverse=True)
    elif order == 'count,asc':
        d_view.sort()
    for items in range(len(d_view)): #search for the longest string or number
        if len(str(d_view[items][0])) > count_lenght:
            count_lenght = len(str(d_view[items][0]))
        if len(d_view[items][1]) > name_length:
            name_length = len(d_view[items][1])
    count_lenght += 2 # add 2 spaces
    name_length += 4 # add 4 spaces
    sum = count_lenght + name_length # number of underline
    print('\n{:>{width}}{:>{swidth}}'.format('count', 'item name', width = count_lenght, swidth = name_length))  # print table
    for underline in range(sum):
        print('_', end='')
    print('\n')
    for value, key in d_view:
        print('{:>{width}}{:>{swidth}}'.format(value, key, width = count_lenght, swidth = name_length))
    

def import_inventory(inventory, filename = 'import_inventory.csv'):
    ''' import inv from file '''
    try: #check file exist
        inv_file = open(filename)
    except IOError:
        print('\nsory you don\'t have any inventory')
    else: #if exist import and add to our inv
        temp_dict = {}
        read = csv.reader(inv_file)
        for row in read:
            if row[0] != 'item_name':
                temp_dict[row[0]] = row[1]
        new_things = {}
        for key_inv, val_inv in inventory.items(): 
            for key_temp, val_temp in temp_dict.items():
                if key_temp == key_inv:
                    inventory[key_inv] = int(val_inv) + int(val_temp) # sum existing items 
                elif val_temp.isdigit():
                    new_things[key_temp] = val_temp # create list of new items
        inventory = {**inventory, **new_things}
        inv_file.close()
    return inventory


def export_inventory(inventory, filename = 'export_inventory.csv'):
    ''' save our inv to filename '''
    exp_file = open(filename, 'w')
    writer = csv.writer(exp_file)
    for key, value in inventory.items():
       writer.writerow([key, value])
    exp_file.close()

def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(inv)
    loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    print('Here is your loot')
    print(loot)
    inv = add_to_inventory(inv, loot)
    display_inventory(inv)
    print_table(inv, 'count,desc')
    inv = import_inventory(inv)
    display_inventory(inv)
    export_inventory(inv)

if __name__ == '__main__':
    main()
