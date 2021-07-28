a1 = [[1, 3], [2, 6], [8, 10], [15, 18]]


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    st = []  # make stack

    intervals.sort()
    for x in intervals:
        if len(st) == 0:
            st.append(x)
        else:
            t = st.pop()
            if t[1] >= x[0]:  # check if possible to merge
                st.append([t[0], max(t[1], x[1])])
            else:  # if not possible to merge
                st.append(t)
                st.append(x)
    return st


print(merge(a1))  # [[1, 6], [8, 10], [15, 18]]
