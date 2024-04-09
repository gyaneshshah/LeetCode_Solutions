class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ind = 0
        time = 0
        people = len(tickets)
        while tickets[k]>0:
            if ind == people:
                ind = 0
            ticket = tickets[ind]
            if ticket!=0:
                tickets[ind]-=1
                time+=1
            ind+=1
        return time
