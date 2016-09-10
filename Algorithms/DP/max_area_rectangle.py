"""
max sub area rectangle in a given matrix
"""

def max_rectangle_area(histogram):
    """Find the area of the largest rectangle that fits entirely under
    the histogram.
    """
    stack = []
    top = lambda: stack[-1]
    max_area = 0
    pos = 0  # current position in the histogram
    for pos, height in enumerate(histogram):
        start = pos  # position where rectangle starts
        while True:
            if not stack or height > top()[1]:
                stack.append((start, height))  # push
            elif stack and height < top()[1]:
                max_area = max(max_area, top()[1] * (pos - top()[0]))
                start, _ = stack.pop()
                continue
            break  # height == top().height goes here

    pos += 1
    for start, height in stack:
        max_area = max(max_area, height * (pos - start))

    return max_area

if __name__ == '__main__':
    histogram = [6, 4, 2, 1, 3, 4, 5, 2, 6]
    print (max_rectangle_area(histogram))