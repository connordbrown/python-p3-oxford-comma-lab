def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    elif len(items) == 3:
        return ", ".join(items[0:2]) + ", and " + items[2]
    else:
        return ", ".join(items[0 : len(items)-1]) + ", and " + items[-1]
    
