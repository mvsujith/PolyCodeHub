package Java;

import java.io.*;

static long solve(int N, int start, int finish, int[] ticket_cost) {
    // write your code here

    // Convert start and finish to 0-based indexing
    start = (start - 1) % N;
    finish = (finish - 1) % N;

    // Calculate clockwise and counter-clockwise costs
    long clockwiseCost = 0;
    long counterClockwiseCost = 0;

    // Calculate clockwise cost
    for (int i = start; i != finish; i = (i + 1) % N) {
        clockwiseCost += ticket_cost[i];
    }

    // Calculate counter-clockwise cost
    for (int i = start; i != finish; i = (i - 1 + N) % N) {
        counterClockwiseCost += ticket_cost[(i - 1 + N) % N];
    }

    // Return the minimum of the two costs
    long result = Math.min(clockwiseCost, counterClockwiseCost);
    return result;
}
