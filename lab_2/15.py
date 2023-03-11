def merge_lists(*args):
    merged_list = []
    for lst in args:
        merged_list.extend(lst)
    return merged_list
