"""Find all unique pairs of maximum and second maximum elements
over all sub - arrays in O(NlogN)"""


def pairs(arr):
    st = [];
    pairs = [];

    # Push first element into stack
    st.append(arr[0]);

    # For each element 'X' in arr,
    # pop the stack while top Element
    # is smaller than 'X' and form a pair.
    # If the stack is not empty after
    # the previous operation, create
    # a pair. Push X into the stack.
    for i in range(1, len(arr)):
        if arr[i] > st[-1]:
            pairs.append((st[-1], arr[i]));
            st.pop();

        if len(st) != 0:
            pairs.append((min(st[-1], arr[i]),
                          max(st[-1], arr[i])));

        st.append(arr[i]);

    return pairs;


print(pairs([1, 2, 6, 4, 5]))

# (1, 2) (2, 6) (4, 5) (4, 6) (5, 6)

