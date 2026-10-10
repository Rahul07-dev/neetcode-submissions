class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        current = grid
        rows, cols = len(grid), len(grid[0])
        elapsed =0
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        fresh = 1
        rotten = 2
        queue =deque()
        tff=0

        for i in range(rows):
            for j in range(cols):
                if current[i][j]==rotten:
                    queue.append((0,i,j));
                elif current[i][j]==fresh:
                    tff+=1;
        
        while queue:
            time,x,y=queue.popleft()
            elapsed=max(time,elapsed)

            for dx,dy in moves:
                nx,ny= x+dx, y+dy
                if (0<= nx<rows) and (0<=ny<cols):
                    if current[nx][ny] == fresh:
                        tff-=1
                        current[nx][ny] =rotten
                        queue.append((time+1,nx,ny))
        
        return elapsed if tff ==0 else -1

    


             
        