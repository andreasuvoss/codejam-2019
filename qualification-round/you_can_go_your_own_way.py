def take_step(direction, coordinates):
    
    if direction == 'E':
        return (direction, (coordinates[0] + 1, coordinates[1]))
    else:
        return (direction, (coordinates[0], coordinates[1] + 1))


if __name__ == '__main__':
    num_of_testcases = int(input())

    for i in range(num_of_testcases):
        maze_dimension = int(input())
        lydia_route = input()

        lydia_coordinate = (0,0)
        our_coordinate = (0,0)

        lydia_route = list(lydia_route)
        our_route = [''] * len(lydia_route)
        lydia_last_move = lydia_route[-1]

        preferred_move = 'E'
        if lydia_last_move == 'S':
            preferred_move = 'S'

        for j, direction in enumerate(lydia_route):
            if our_coordinate == lydia_coordinate and lydia_route[j] == 'E':
                our_route[j], our_coordinate = take_step('S', our_coordinate)
                lydia_route[j], lydia_coordinate = take_step('E', lydia_coordinate)
            elif our_coordinate == lydia_coordinate and lydia_route[j] == 'S':
                our_route[j], our_coordinate = take_step('E', our_coordinate)
                lydia_route[j], lydia_coordinate = take_step('S', lydia_coordinate)
            else:
                if our_coordinate[0] == maze_dimension - 1:
                    our_route[j], our_coordinate = take_step('S', our_coordinate)
                elif our_coordinate[1] == maze_dimension - 1:
                    our_route[j], our_coordinate = take_step('E', our_coordinate)
                else:
                    our_route[j], our_coordinate = take_step(preferred_move, our_coordinate)
                lydia_route[j], lydia_coordinate = take_step(direction, lydia_coordinate)

        print('Case #'+str(i+1)+':', ''.join(our_route).upper())
