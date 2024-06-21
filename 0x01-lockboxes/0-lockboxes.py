#!/usr/bin/python3
""" Lockboxes using Graph theory """


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return True
    visited_boxes = set()
    boxes_to_visit = [0]

    while boxes_to_visit:
        current = boxes_to_visit.pop()
        visited_boxes.add(current)
        if len(visited_boxes) == len(boxes):
            return True

        current_keys = boxes[current]
        for key in current_keys:
            if key < len(boxes) and key not in visited_boxes:
                boxes_to_visit.append(key)

    return len(visited_boxes) == len(boxes)
