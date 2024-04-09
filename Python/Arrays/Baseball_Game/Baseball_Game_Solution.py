class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum_record = 0
        for i, operation in enumerate(operations):
            if operation == '+':
                prev = record[-1]
                bef_prev = record[-2]
                record.append(prev+bef_prev)
                sum_record += prev+bef_prev
            elif operation == 'D':
                prev = record[-1]
                record.append(prev*2)
                sum_record += prev*2
            elif operation == 'C':
                sum_record -= record[-1]
                record.pop()
            else:
                record.append(int(operation))
                sum_record += int(operation)
        return sum_record
