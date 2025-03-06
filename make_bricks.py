def make_bricks(small, big, goal):
    big_bricks_used = min(big, goal // 5)
    
    remaining_goal = goal - big_bricks_used * 5
    
    return remaining_goal <= small
