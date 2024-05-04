class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int: 
        people.sort(reverse=True)
        no_of_boats = 0
        if people == 1:
            return 1
        while people:
            if len(people)>1:
                if people[0]+people[-1]<=limit:
                    people.pop()
            people.pop(0)
            no_of_boats +=1
        return no_of_boats   
