from typing import List
class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        self.visited = [ False for i in range(num_courses)]
        self.to_mark = [ False for i in range(num_courses)]

        for course, prerequisite in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].push(prerequisite)

        for course in graph:
            # if cycle is found
            if not self.dfs(graph, course):
                return False
        return True


    def dfs(self, graph, course):
        if self.to_mark[course] == True:
            return True
        elif self.visited[course] == True:
            return False

        self.visited[course] = True
        for prerequisite in graph[course]: # 若 vertice 在尾端，不進入該迴圈
            self.dfs(prerequisite)

        self.to_mark[course] = True
        self.visited[course] = False



if __name__ == '__main__':
    numCourses = 2
    prerequisites_a = [[0, 1]]
    prerequisites_b = [[1,0],[0,1]]
