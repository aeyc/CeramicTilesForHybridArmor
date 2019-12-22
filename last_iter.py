import random
import math
import timeit

EDGE = 20
X_LIMIT = 360
Y_LIMIT = 600
TOTAL_AREA = 425 * 650


# frame = Frame(width=500, height=200, bg='blue')
# canvas = Canvas(frame, bg='white')
# frame.pack(fill = BOTH, expand = YES)


def hex_points(x, y):
    points = (
    x + EDGE, y - EDGE, x, y, x + EDGE, y + EDGE, x + 2 * EDGE, y + EDGE, x + 3 * EDGE, y, x + 2 * EDGE, y - EDGE)
    return points


def hex_area(x):
    area = 0.0
    area = math.sqrt(3) * x * x / 4
    return area


def square_points(x, y):
    points = (x, y, x, y + EDGE, x + EDGE, y + EDGE, x + EDGE, y)
    return points


def square_area(x):
    area = 0.0
    return x * x


start_time = timeit.default_timer()  # timer initialization
# Q = []  # later process, Q matrix of the whole models for comparing actions and scores
# model_count = 0
# best_actions_states = []
# rem_areas = []  #dummy list just keptfor time efficiency
k = [2, 5, 10, 50, 100]
for j in range(10, 100, 10):
    Q = []  # later process, Q matrix of the whole models for comparing actions and scores
    model_count = 0
    best_actions_states = []
    rem_areas = []  # dummy list just keptfor time efficiency
    print("-------------------------------------------------------------------------------------------------")
    print("k = ", j)
    for i in range(0, j):
        moves = []  # keeps the data of the iteration count, shape selection and the coordinate selection
        used_points = []  # keeps the data of used points(coordinates), to avoid overlapping
        count = 0  # number of iterations of the loop for a single model
        appeared = False  # a controller flag to find whether random coordinate is already used or not
        remaining_area = TOTAL_AREA  # the area which will represent the score variable for reinforcement learning

        print("For Model number:", model_count + 1)
        if model_count > 1:
            index = rem_areas.index(min(rem_areas))  # find the position of bestmodel
            # print("index",index)
            # print("q-len",len(Q))
            # print("Q[index][0]",(Q[index])[0])
            moves.append((Q[index])[0:model_count - 1])
            print("Best model so far: ", index, "th model")

            # print("moves",moves)
            for i in range(0, model_count - 1):
                remaining_area = (moves[0])[-1][3]
            count += model_count
            print("Beginning from", count, "th iteration")
        while count < 100:
            choice = random.randint(0, 2)
            appeared = False
            tmp_points = []  # tmp points stores the randomly selected points and based on the shape, other coordinates that will added to this list
            if choice == 1:
                # print("choice 1")
                x = random.randint(0, X_LIMIT)
                y = random.randint(EDGE, Y_LIMIT)

                # rectangular area
                for i in range(x + EDGE, x + 2 * EDGE):
                    for j in range(y - EDGE, y + EDGE):
                        tmp_points.append((i, j))

                # triangular area-up left
                tmp_k = x
                for j in range(y, y + EDGE):
                    for i in range(tmp_k, x + EDGE):
                        tmp_points.append((i, j))
                    tmp_k += 1

                # triangular area-down left
                tmp_k = x
                for j in range(y, y - EDGE, -1):
                    for i in range(tmp_k, x + EDGE):
                        tmp_points.append((i, j))
                    tmp_k += 1

                # triangular area-up right
                tmp_k = x + 2 * EDGE
                for j in range(y, y + EDGE):
                    for i in range(tmp_k, x + 3 * EDGE):
                        tmp_points.append((i, j))
                    tmp_k += 1

                # triangular area-down right
                tmp_k = x + 2 * EDGE
                for j in range(y, y - EDGE, -1):
                    for i in range(tmp_k, x + 3 * EDGE):
                        tmp_points.append((i, j))
                    tmp_k += 1

                for i in used_points:
                    for j in tmp_points:
                        if j == i:
                            appeared = True
                if not appeared:
                    hexagon_points = hex_points(x, y)  # range of hexagon (x>=0, y>=20)
                    # print("hex created")
                    for i in tmp_points:
                        used_points.append(i)
                    remaining_area -= hex_area(EDGE)
                    moves.append((count, choice, (x, y), remaining_area))

                    # print("remaining area", remaining_area)
            elif choice == 0:
                # print("choice 0")
                x = random.randint(0, X_LIMIT)
                y = random.randint(EDGE, Y_LIMIT)
                for i in range(x, x + EDGE):
                    for j in range(y, y + EDGE):
                        tmp_points.append((i, j))
                for i in used_points:
                    for j in tmp_points:
                        if j == i:
                            appeared = True
                if not appeared:
                    s_points = square_points(x, y)
                    # print("square created")
                    for i in range(x, x + EDGE):
                        for j in range(y, y + EDGE):
                            used_points.append((i, j))
                    remaining_area -= square_area(EDGE)
                    moves.append((count, choice, (x, y), remaining_area))

                    # print("remaining area", remaining_area)
            count += 1
            # print("count",count)
        rem_areas.append(remaining_area)

        Q.append(moves)
        print("Q-Matrix (state,shape choice,coordinate pair choice, remaining area)\n", Q)
        # print("moves",moves)
        # print("Q",Q)
        # print("Q[0]",Q[0])
        # print("Q[0][1]",(Q[0])[1])
        # print("Q[0][2]",Q[0][2])
        # print("Q[0][3]",Q[0][3])
        model_count += 1
        print(("For given k = {} best model's remaining area: {}").format(k, rem_areas))
        # canvas.delete("all")

    # count = 1
    # for i in model_analytic:
    #    print(count, "th model:")
    #    print("Remaining Area:",i[0])
    #    count+=1
print("\n--------------------------------------------------END--------------------------------------------------")
print("Best model remaining area:", rem_areas)
elapsed = timeit.default_timer() - start_time
print(elapsed)

