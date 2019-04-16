import argparse

def quick_sort(array, left, right):
    print(array)
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[left] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="please input num,split by space")
    parse.add_argument("num",type=int,nargs='+')
    args = parse.parse_args()
    quick_sort(args.num,0,len(args.num) -1)